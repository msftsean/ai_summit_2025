# Agentic AI Design Pattern Demos

| Status | 🟢 Ready |
|--------|----------|

| Version | Date       | Author | Changes                    |
|---------|------------|--------|----------------------------|
| 1.0.0   | 2025-12-08 | Claude | Initial release            |

## 📖 Overview

Working demonstrations of 4 foundational agentic AI design patterns. Each demo produces structured output (JSON + human-readable) optimized for learning and screen recording.

### 🎯 Patterns Included

| Demo | Pattern | Description |
|------|---------|-------------|
| `agent_executor.py` | Agent-Executor | Customer support agent with tool selection |
| `react_loop.py` | ReAct Loop | Research agent with think→action→observe cycles |
| `agent_orchestration.py` | Multi-Agent | Coordinator routing to specialist agents |
| `planning_execution.py` | Planning+Execution | Plan generation with checkpoint validation |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ (recommended: 3.11)
- pip (included with Python)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd ai_summit

# Install dependencies
pip install -r requirements.txt
```

### Dependencies

```
autogen-agentchat>=0.4.0
requests>=2.31.0
ollama>=0.3.0
streamlit>=1.29.0
```

---

## 📖 Usage

Run any demo from the project root:

### 1️⃣ Agent-Executor Demo (Customer Support)

```bash
python src/agent_executor.py
```

Shows tool selection and invocation for refunds and password resets.

### 2️⃣ ReAct Loop Demo (Research Agent)

```bash
python src/react_loop.py
```

Demonstrates iterative reasoning with think→action→observation cycles.

### 3️⃣ Multi-Agent Orchestration Demo (Order Fulfillment)

```bash
python src/agent_orchestration.py
```

Shows coordinator routing to Inventory, Payment, and Shipping specialists.

### 4️⃣ Planning + Execution Demo (Content Migration)

```bash
python src/planning_execution.py
```

Demonstrates plan generation, validation checkpoint, and step-by-step execution.

---

## 📋 Expected Output Samples

### Agent-Executor Output

```
============================================================
🤖 AGENT-EXECUTOR PATTERN DEMO
   Customer Support with Tool Selection
============================================================

[AGENT THINKING]
Analyzing customer request: "I want a refund for order #12345"
Intent: REFUND_REQUEST
Selected tool: refund_processor

[TOOL CALL: refund_processor]
Parameters:
  order_id: ORD-12345
  reason: not as described

[TOOL RESPONSE]
{
  "status": "success",
  "refund_id": "REF-12345-...",
  "amount": 99.99,
  "processing_time": "3-5 business days"
}

[AGENT OUTPUT]
I've processed your refund for order #12345. You'll receive $99.99
back to your original payment method within 3-5 business days.
```

### ReAct Loop Output

```
============================================================
🔄 REACT LOOP PATTERN DEMO
   Research Agent with Think-Action-Observation Cycle
============================================================

[TURN 1]

[THOUGHT]
I need to research the latest AI frameworks. Let me search for recent developments.

[ACTION: search]
Query: "latest AI agent frameworks 2024"

[OBSERVATION]
Found 3 results about AI frameworks including AutoGen, LangChain, and CrewAI...

[TURN 2]
...

[FINAL ANSWER]
Based on my research, the top AI agent frameworks are:
1. AutoGen - Microsoft's multi-agent framework
2. LangChain - Popular for LLM application development
3. CrewAI - Role-based agent orchestration
```

### Multi-Agent Orchestration Output

```
============================================================
🔀 MULTI-AGENT ORCHESTRATION PATTERN DEMO
   Order Fulfillment with Coordinator + Specialists
============================================================

[COORDINATOR ROUTING]
→ Step 1: Check inventory (Inventory Agent)
→ Step 2: Process payment (Payment Agent)
→ Step 3: Arrange shipping (Shipping Agent)

→ Routing to InventoryAgent
[InventoryAgent RESPONSE]
  ✓ Widget A: 2 requested, 50 available
  ✓ Widget B: 1 requested, 25 available

→ Routing to PaymentAgent
[PaymentAgent RESPONSE]
  ✓ Charged $249.97 to card ending in 4242
  Transaction: TXN-...

→ Routing to ShippingAgent
[ShippingAgent RESPONSE]
  ✓ Shipping arranged via FastShip Express
  Tracking: SHIP-...

[COORDINATOR SUMMARY]
Order ID: ORD-...
✓ Order fulfilled successfully!
```

### Planning + Execution Output

```
============================================================
📋 PLANNING + EXECUTION PATTERN DEMO
   Content Migration with Plan Generation & Progress
============================================================

[PLANNING PHASE]
Task: Migrate 100 YouTube videos to course platform

Generated Plan:
  1. Fetch video metadata from YouTube
  2. Download video files
  3. Transcode to platform format
  4. Upload to course platform
  5. Verify and generate report

[CHECKPOINT]
Plan validation for: Migrate 100 YouTube videos
  Total steps: 5
  Dependencies: All clear
Status: Plan validated and ready for execution

[EXECUTION PHASE]
[STEP 1/5] ✓ Fetch video metadata (12s)
[STEP 2/5] ✓ Download video files (45s)
[STEP 3/5] ✓ Transcode to platform format (38s)
[STEP 4/5] ✓ Upload to course platform (22s)
[STEP 5/5] ✓ Verify and generate report (8s)

✓ Migration completed successfully!
```

---

## 🖥️ Streamlit Viewer

The Streamlit viewer renders demo output as styled cards with animations.

### Running the Viewer

```bash
streamlit run src/streamlit_viewer.py
```

### Features

- 📁 Upload JSON output files
- 📋 Paste JSON content directly
- 🎨 Color-coded cards by step type
- 🔍 Filter by step type
- ✨ Fade-in animations for recording

### Saving Demo Output

Capture demo output to a file for the viewer:

```bash
python src/agent_executor.py > demo_output.json 2>&1
```

Then upload `demo_output.json` to the Streamlit viewer.

---

## 🤖 Local LLM Setup

Demos auto-detect local LLM availability. If not found, they use mocked responses.

### Option A: Ollama (Recommended)

1. Download from https://ollama.com/download
2. Install and start Ollama
3. Pull a model: `ollama pull llama2` or `ollama pull mistral`
4. Ollama runs on `localhost:11434`

### Option B: LM Studio

1. Download from https://lmstudio.ai/
2. Install and load a model
3. Start the local server (runs on `localhost:1234`)

### Verification

```bash
# Check Ollama
curl http://localhost:11434/api/tags

# Check LM Studio
curl http://localhost:1234/v1/models
```

---

## ⚠️ Troubleshooting

### Import Errors

```
ModuleNotFoundError: No module named 'common'
```

**Solution**: Run from the project root directory:
```bash
cd ai_summit
python src/agent_executor.py
```

### Streamlit Not Found

```
streamlit: command not found
```

**Solution**: Ensure Streamlit is installed:
```bash
pip install streamlit>=1.29.0
```

### Demos Run Too Fast

Demos include 0.3-0.5 second delays between steps for readability. If running in automated testing, these can be adjusted in `src/common/output.py`.

### No LLM Available

Demos work without a local LLM - they automatically fall back to mocked/scripted responses. The mock mode demonstrates the same patterns.

### JSON Parsing Errors in Viewer

Ensure the input is valid JSON. Each line should be a complete JSON object:
```json
{"type": "thinking", "content": "...", "timestamp": 123}
```

---

## 📁 Project Structure

```
ai_summit/
├── src/
│   ├── agent_executor.py      # Agent-Executor demo
│   ├── react_loop.py          # ReAct Loop demo
│   ├── agent_orchestration.py # Multi-Agent demo
│   ├── planning_execution.py  # Planning+Execution demo
│   ├── streamlit_viewer.py    # Output viewer
│   └── common/
│       ├── __init__.py
│       ├── output.py          # Structured output utilities
│       └── llm_provider.py    # LLM auto-detection
├── specs/                     # Feature specifications
├── requirements.txt
└── README.md
```

---

## 📄 License

MIT License - See LICENSE file for details.
