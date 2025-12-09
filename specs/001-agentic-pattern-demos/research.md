# Research: Agentic AI Design Pattern Demos

| Status | 🟢 Ready |
|--------|----------|

| Version | Date       | Author | Changes              |
|---------|------------|--------|----------------------|
| 1.0.0   | 2025-12-08 | Claude | Initial research     |

## 🔍 Research Summary

This document captures technology decisions and best practices research for implementing the 4 agentic AI design pattern demos.

---

## 📦 Microsoft Agent Framework Selection

### Decision: Use `autogen-agentchat` (AutoGen 0.4+)

**Rationale**: AutoGen is Microsoft's official agentic AI framework, actively maintained, and provides the building blocks for all 4 patterns without requiring cloud API keys when using local LLMs.

**Alternatives Considered**:

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| autogen-agentchat | Official MS framework, pattern support, active development | Learning curve | ✅ Selected |
| semantic-kernel | MS framework, enterprise focus | More complex, overkill for demos | ❌ Rejected |
| langchain | Popular, many examples | Not MS framework (per spec) | ❌ Rejected |
| Custom implementation | Full control | More code, harder to maintain | ❌ Rejected |

---

## 🤖 LLM Provider Strategy

### Decision: Auto-detect with Ollama priority, mock fallback

**Implementation Approach**:
1. Check if Ollama is running (HTTP request to `localhost:11434/api/tags`)
2. Check if LM Studio is running (HTTP request to `localhost:1234/v1/models`)
3. Fall back to scripted/mocked responses if neither available

**Rationale**: Provides real LLM experience when available while ensuring demos always work offline.

**Code Pattern**:
```python
def get_llm_provider():
    """Auto-detect available LLM provider."""
    # Try Ollama first
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=1)
        if response.ok:
            return OllamaProvider()
    except:
        pass

    # Try LM Studio
    try:
        response = requests.get("http://localhost:1234/v1/models", timeout=1)
        if response.ok:
            return LMStudioProvider()
    except:
        pass

    # Fall back to mock
    return MockProvider()
```

---

## 📤 Structured Output Protocol

### Decision: Dual-format output (JSON + Human-readable)

**Format Specification**:
```python
def log_step(step_type: str, content: str) -> None:
    """Emit structured output for both parsing and display."""
    import json
    import time

    # JSON for Streamlit parsing
    output = {"type": step_type, "content": content, "timestamp": time.time()}
    print(json.dumps(output))

    # Human-readable for terminal
    print(f"\n[{step_type.upper()}]\n{content}\n")

    # Delay for readability
    time.sleep(0.4)
```

**Valid Step Types** (per Constitution):
- `thinking` - Agent reasoning process
- `action` - Tool invocation or decision
- `observation` - Result from tool or environment
- `response` - Final agent output
- `error` - Error conditions
- `routing` - Multi-agent delegation
- `summary` - Aggregated results
- `planning` - Plan generation
- `execution` - Plan step execution
- `checkpoint` - Progress milestone

---

## 🛠️ Tool Schema Standard

### Decision: JSON Schema format with realistic responses

**Tool Definition Pattern**:
```python
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
    }
]
```

**Mock Response Pattern**:
```python
def mock_refund_processor(order_id: str, reason: str) -> dict:
    """Return realistic refund response."""
    return {
        "status": "success",
        "refund_id": f"REF-{order_id}-{int(time.time())}",
        "amount": 99.99,
        "currency": "USD",
        "processing_time": "3-5 business days",
        "confirmation_email_sent": True
    }
```

---

## 🎯 Pattern Implementation Guidelines

### Pattern 1: Agent-Executor

**Key Elements**:
- Single agent with tool access
- Clear tool selection reasoning
- Tool invocation with parameters
- Response synthesis from tool output

**Demo Scenario**: Customer support agent handling refund and password reset requests.

### Pattern 2: ReAct Loop

**Key Elements**:
- Explicit Thought → Action → Observation cycle
- Minimum 3-4 turns showing iteration
- Progressive information gathering
- Final answer synthesis

**Demo Scenario**: Research agent investigating "latest AI frameworks 2025".

### Pattern 3: Multi-Agent Orchestration

**Key Elements**:
- Coordinator agent for routing
- 3+ specialist agents (Inventory, Payment, Shipping)
- Visible delegation and response aggregation
- Summary with success/failure indicators

**Demo Scenario**: Order fulfillment with multi-step coordination.

### Pattern 4: Planning + Execution

**Key Elements**:
- Distinct planning phase with numbered steps
- Validation checkpoint before execution
- Step-by-step execution with progress indicators
- Progress percentage tracking

**Demo Scenario**: Content migration (100 videos to course platform).

---

## 📊 Streamlit Viewer Design

### Decision: Card-based rendering with step type styling

**Implementation Approach**:
- Read JSON lines from stdin or file
- Parse each line as structured output
- Render as styled cards based on step_type
- Add subtle animations for screen recording

**Card Styling by Type**:

| Step Type | Color | Icon |
|-----------|-------|------|
| thinking | Blue | 🤔 |
| action | Orange | ⚡ |
| observation | Green | 👁️ |
| response | Purple | 💬 |
| error | Red | ❌ |
| routing | Cyan | 🔀 |
| summary | Gold | 📊 |
| planning | Indigo | 📋 |
| execution | Teal | ▶️ |
| checkpoint | Yellow | ✅ |

---

## 📋 Dependencies

### Final Dependency List

```text
# Core
autogen-agentchat>=0.4.0
requests>=2.31.0

# Optional LLM providers
ollama>=0.3.0

# Viewer (optional)
streamlit>=1.29.0

# Development
pytest>=7.4.0  # Optional for testing
```

---

## ✅ Research Complete

All technical decisions resolved. Ready for Phase 1 design artifacts.
