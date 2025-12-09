"""
Agent-Executor Pattern Demo

Demonstrates a customer support agent that uses tools to handle refunds and
password resets. Shows how agents select and invoke tools based on user requests.

Pattern: Agent-Executor (Basic Tool-Using Agent)
"""

import json
import time
import sys
sys.path.insert(0, '.')

from common.output import log_step, step_delay, format_tool_call, format_tool_response

# =============================================================================
# Tool Definitions (T009, T010)
# =============================================================================

TOOLS = [
    {
        "name": "refund_processor",
        "description": "Process a customer refund for an order",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "The order ID to refund"
                },
                "reason": {
                    "type": "string",
                    "description": "Reason for the refund"
                }
            },
            "required": ["order_id", "reason"]
        }
    },
    {
        "name": "password_reset",
        "description": "Send a password reset email to a customer",
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "format": "email",
                    "description": "Customer email address"
                }
            },
            "required": ["email"]
        }
    }
]


# =============================================================================
# Mock Tool Implementations (T011, T012)
# =============================================================================

def mock_refund_processor(order_id: str, reason: str) -> dict:
    """Return realistic refund response."""
    return {
        "status": "success",
        "refund_id": f"REF-{order_id}-{int(time.time())}",
        "order_id": order_id,
        "amount": 99.99,
        "currency": "USD",
        "reason": reason,
        "processing_time": "3-5 business days",
        "confirmation_email_sent": True
    }


def mock_password_reset(email: str) -> dict:
    """Return realistic password reset response."""
    return {
        "status": "success",
        "email": email,
        "reset_link_sent": True,
        "expires_in": "24 hours",
        "message": f"Password reset email sent to {email}"
    }


# =============================================================================
# Agent Implementation (T013)
# =============================================================================

class CustomerSupportAgent:
    """Customer support agent with tool selection logic."""

    def __init__(self):
        self.tools = {tool["name"]: tool for tool in TOOLS}
        self.tool_functions = {
            "refund_processor": mock_refund_processor,
            "password_reset": mock_password_reset
        }

    def analyze_request(self, user_request: str) -> tuple:
        """
        Analyze user request and select appropriate tool.
        Returns (tool_name, params) or (None, None) if no tool matches.
        """
        request_lower = user_request.lower()

        if "refund" in request_lower:
            # Extract order ID (mock extraction)
            order_id = "ORD-12345"
            if "order" in request_lower:
                # Try to find order number
                words = request_lower.split()
                for i, word in enumerate(words):
                    if word == "order" and i + 1 < len(words):
                        potential_id = words[i + 1].strip(".,!?")
                        if potential_id.isdigit() or potential_id.startswith("ord"):
                            order_id = potential_id.upper()
                            break

            reason = "customer request"
            if "not as described" in request_lower:
                reason = "not as described"
            elif "damaged" in request_lower:
                reason = "item damaged"
            elif "wrong" in request_lower:
                reason = "wrong item received"

            return "refund_processor", {"order_id": order_id, "reason": reason}

        elif "password" in request_lower or "reset" in request_lower:
            # Extract email (mock extraction)
            email = "customer@example.com"
            words = user_request.split()
            for word in words:
                if "@" in word and "." in word:
                    email = word.strip(".,!?")
                    break

            return "password_reset", {"email": email}

        return None, None

    def execute_tool(self, tool_name: str, params: dict) -> dict:
        """Execute the selected tool with given parameters."""
        if tool_name in self.tool_functions:
            return self.tool_functions[tool_name](**params)
        return {"status": "error", "message": f"Unknown tool: {tool_name}"}

    def process_request(self, user_request: str) -> str:
        """Process a user request end-to-end."""
        # Step 1: Thinking - analyze the request
        log_step("thinking", f"Analyzing user request: \"{user_request}\"\n"
                            f"Available tools: {list(self.tools.keys())}")
        step_delay()

        # Step 2: Tool selection
        tool_name, params = self.analyze_request(user_request)

        if tool_name is None:
            log_step("response", "I'm sorry, I couldn't determine how to help with that request. "
                                "I can help with refunds and password resets.")
            return "No matching tool found"

        log_step("thinking", f"Selected tool: {tool_name}")
        step_delay()

        # Step 3: Tool call
        log_step("action", format_tool_call(tool_name, params),
                metadata={"tool_name": tool_name, "tool_params": params})
        step_delay()

        # Step 4: Tool response
        result = self.execute_tool(tool_name, params)
        log_step("observation", format_tool_response(result))
        step_delay()

        # Step 5: Final response
        if result.get("status") == "success":
            if tool_name == "refund_processor":
                response = (f"✓ Refund processed successfully!\n"
                           f"  Refund ID: {result['refund_id']}\n"
                           f"  Amount: ${result['amount']:.2f} {result['currency']}\n"
                           f"  Processing time: {result['processing_time']}")
            else:
                response = (f"✓ Password reset initiated!\n"
                           f"  {result['message']}\n"
                           f"  Link expires in: {result['expires_in']}")
        else:
            response = f"❌ Error: {result.get('message', 'Unknown error')}"

        log_step("response", response)
        return response


# =============================================================================
# Demo Scenarios (T014, T015)
# =============================================================================

def run_refund_scenario():
    """Run the refund request scenario."""
    print("\n" + "="*60)
    print("SCENARIO 1: Customer Refund Request")
    print("="*60 + "\n")

    agent = CustomerSupportAgent()
    agent.process_request("I want a refund for order 12345, the item was not as described")


def run_password_reset_scenario():
    """Run the password reset scenario."""
    print("\n" + "="*60)
    print("SCENARIO 2: Password Reset Request")
    print("="*60 + "\n")

    agent = CustomerSupportAgent()
    agent.process_request("I need to reset my password for john.doe@email.com")


# =============================================================================
# Main Entry Point (T016, T017)
# =============================================================================

def main():
    """Run the Agent-Executor demo with multiple scenarios."""
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "="*60)
    print("AGENT-EXECUTOR PATTERN DEMO")
    print("   Customer Support Agent with Tool Selection")
    print("="*60)

    # Run both scenarios
    run_refund_scenario()
    step_delay(0.5)
    run_password_reset_scenario()

    print("\n" + "="*60)
    print("Demo complete!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
