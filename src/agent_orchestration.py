"""
Multi-Agent Orchestration Pattern Demo

Demonstrates an order fulfillment system with a coordinator routing to
Inventory, Payment, and Shipping specialist agents.

Pattern: Multi-Agent Orchestration (Coordinator + Specialists)
"""

import json
import time
import sys
sys.path.insert(0, '.')

from common.output import log_step, step_delay

# =============================================================================
# Specialist Agent Implementations (T025, T026, T027)
# =============================================================================

class InventoryAgent:
    """Specialist agent for inventory management."""

    def __init__(self):
        self.name = "InventoryAgent"
        # Mock inventory data
        self.inventory = {
            "Widget A": 50,
            "Widget B": 25,
            "Widget C": 100,
            "Gadget X": 10,
            "Gadget Y": 0  # Out of stock
        }

    def check_inventory(self, items: list) -> dict:
        """Check availability of requested items."""
        results = []
        all_available = True

        for item in items:
            product = item["product"]
            quantity = item["quantity"]
            available = self.inventory.get(product, 0)

            if available >= quantity:
                results.append({
                    "product": product,
                    "requested": quantity,
                    "available": available,
                    "status": "available"
                })
            else:
                all_available = False
                results.append({
                    "product": product,
                    "requested": quantity,
                    "available": available,
                    "status": "insufficient" if available > 0 else "out_of_stock"
                })

        return {
            "agent": self.name,
            "status": "success" if all_available else "partial",
            "all_available": all_available,
            "items": results
        }


class PaymentAgent:
    """Specialist agent for payment processing."""

    def __init__(self):
        self.name = "PaymentAgent"

    def process_payment(self, amount: float, card_last_four: str = "4242") -> dict:
        """Process payment for an order."""
        # Simulate payment processing
        transaction_id = f"TXN-{int(time.time())}"

        return {
            "agent": self.name,
            "status": "success",
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": "USD",
            "card_last_four": card_last_four,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }


class ShippingAgent:
    """Specialist agent for shipping arrangements."""

    def __init__(self):
        self.name = "ShippingAgent"

    def arrange_shipping(self, items: list, address: str = "123 Main St") -> dict:
        """Arrange shipping for order items."""
        tracking_number = f"SHIP-{int(time.time())}"

        return {
            "agent": self.name,
            "status": "success",
            "tracking_number": tracking_number,
            "carrier": "FastShip Express",
            "estimated_delivery": "2-3 business days",
            "items_count": len(items),
            "shipping_address": address
        }


# =============================================================================
# Coordinator Agent (T028)
# =============================================================================

class CoordinatorAgent:
    """Coordinator that routes tasks to specialist agents."""

    def __init__(self):
        self.name = "Coordinator"
        self.inventory_agent = InventoryAgent()
        self.payment_agent = PaymentAgent()
        self.shipping_agent = ShippingAgent()

    def route_to_specialists(self, order: dict) -> dict:
        """Route order to appropriate specialist agents in sequence."""
        results = {
            "order_id": f"ORD-{int(time.time())}",
            "inventory": None,
            "payment": None,
            "shipping": None,
            "success": False
        }

        items = order["items"]
        total_amount = sum(item.get("price", 49.99) * item["quantity"] for item in items)

        # Step 1: Check Inventory
        log_step("routing", f"→ Routing to {self.inventory_agent.name}",
                metadata={"agent_name": self.inventory_agent.name})
        step_delay(0.3)

        inventory_result = self.inventory_agent.check_inventory(items)
        results["inventory"] = inventory_result

        inv_output = f"[{self.inventory_agent.name} RESPONSE]\n"
        for item in inventory_result["items"]:
            status_icon = "✓" if item["status"] == "available" else "✗"
            inv_output += f"  {status_icon} {item['product']}: {item['requested']} requested, {item['available']} available\n"

        log_step("observation", inv_output)
        step_delay()

        if not inventory_result["all_available"]:
            results["success"] = False
            return results

        # Step 2: Process Payment
        log_step("routing", f"→ Routing to {self.payment_agent.name}",
                metadata={"agent_name": self.payment_agent.name})
        step_delay(0.3)

        payment_result = self.payment_agent.process_payment(total_amount)
        results["payment"] = payment_result

        pay_output = f"[{self.payment_agent.name} RESPONSE]\n"
        pay_output += f"  ✓ Charged ${payment_result['amount']:.2f} to card ending in {payment_result['card_last_four']}\n"
        pay_output += f"  Transaction: {payment_result['transaction_id']}"

        log_step("observation", pay_output)
        step_delay()

        # Step 3: Arrange Shipping
        log_step("routing", f"→ Routing to {self.shipping_agent.name}",
                metadata={"agent_name": self.shipping_agent.name})
        step_delay(0.3)

        shipping_result = self.shipping_agent.arrange_shipping(items)
        results["shipping"] = shipping_result

        ship_output = f"[{self.shipping_agent.name} RESPONSE]\n"
        ship_output += f"  ✓ Shipping arranged via {shipping_result['carrier']}\n"
        ship_output += f"  Tracking: {shipping_result['tracking_number']}\n"
        ship_output += f"  Estimated delivery: {shipping_result['estimated_delivery']}"

        log_step("observation", ship_output)
        step_delay()

        results["success"] = True
        return results


# =============================================================================
# Mock Responses Helper (T029)
# =============================================================================

def format_agent_response(agent_name: str, result: dict) -> str:
    """Format agent response for display."""
    return json.dumps(result, indent=2)


# =============================================================================
# Orchestration Flow (T030, T031)
# =============================================================================

def process_order(order: dict) -> dict:
    """Process an order through the multi-agent orchestration flow."""
    coordinator = CoordinatorAgent()

    # Show incoming request
    items_str = ", ".join([f"{item['quantity']}x {item['product']}" for item in order["items"]])
    log_step("thinking", f"[INCOMING REQUEST]\nUser: \"I want to order {items_str}\"")
    step_delay()

    # Show coordinator routing plan
    log_step("planning", "[COORDINATOR ROUTING]\n"
                        "→ Step 1: Check inventory (Inventory Agent)\n"
                        "→ Step 2: Process payment (Payment Agent)\n"
                        "→ Step 3: Arrange shipping (Shipping Agent)")
    step_delay()

    # Route to specialists
    results = coordinator.route_to_specialists(order)

    # Generate summary
    summary = generate_summary(results)
    log_step("summary", summary)

    return results


def generate_summary(results: dict) -> str:
    """Generate coordinator summary with success/failure indicators (T031)."""
    summary = f"[COORDINATOR SUMMARY]\n"
    summary += f"Order ID: {results['order_id']}\n\n"

    if results["success"]:
        summary += "✓ Order fulfilled successfully!\n\n"
        summary += "Steps completed:\n"
        summary += "  ✓ Inventory verified\n"
        summary += f"  ✓ Payment processed (${results['payment']['amount']:.2f})\n"
        summary += f"  ✓ Shipping arranged ({results['shipping']['tracking_number']})\n"
        summary += f"\nEstimated delivery: {results['shipping']['estimated_delivery']}"
    else:
        summary += "✗ Order could not be fulfilled\n\n"
        if results["inventory"] and not results["inventory"]["all_available"]:
            summary += "Issue: Some items not available in inventory\n"
            for item in results["inventory"]["items"]:
                if item["status"] != "available":
                    summary += f"  ✗ {item['product']}: Only {item['available']} available (requested {item['requested']})\n"

    return summary


# =============================================================================
# Main Entry Point (T032)
# =============================================================================

def main():
    """Run the Multi-Agent Orchestration demo."""
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "="*60)
    print("MULTI-AGENT ORCHESTRATION PATTERN DEMO")
    print("   Order Fulfillment with Coordinator + Specialists")
    print("="*60 + "\n")

    # Sample order
    order = {
        "customer": "John Doe",
        "items": [
            {"product": "Widget A", "quantity": 2, "price": 49.99},
            {"product": "Widget B", "quantity": 1, "price": 149.99}
        ],
        "shipping_address": "123 Main St, Anytown, USA"
    }

    process_order(order)

    print("\n" + "="*60)
    print("Demo complete!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
