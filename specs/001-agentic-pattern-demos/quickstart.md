# 🚀 Quickstart: Agentic AI Design Pattern Demos

| Status | 🟢 Ready |
|--------|----------|

| Version | Date       | Author | Changes         |
|---------|------------|--------|-----------------|
| 1.0.0   | 2025-12-08 | Claude | Initial guide   |

## 📦 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Ollama or LM Studio for local LLM support

## 🔧 Installation

```bash
# Clone or navigate to the repository
cd ai_summit

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 📖 Running the Demos

### Pattern 1: Agent-Executor

```bash
python src/agent_executor.py
```

**Expected Output**:
```
{"type": "thinking", "content": "Analyzing user request: 'I want a refund for order 12345'", ...}

[THINKING]
Analyzing user request: 'I want a refund for order 12345'

{"type": "action", "content": "Calling refund_processor", ...}

[ACTION]
Function: refund_processor
Params: {"order_id": "12345", "reason": "customer request"}

[TOOL RESPONSE]
{"status": "success", "refund_amount": 99.99, "processing_time": "3-5 days"}

[AGENT OUTPUT]
✓ Refund processed successfully. You'll see $99.99 back in 3-5 days.
```

---

### Pattern 2: ReAct Loop

```bash
python src/react_loop.py
```

**Expected Output**:
```
[TURN 1]
[THOUGHT] I need to research latest AI frameworks. Let me start with a search.
[ACTION] search("latest AI frameworks 2025")
[OBSERVATION] Found references to Claude, GPT-4, Llama 3, Gemini

[TURN 2]
[THOUGHT] I got some names but need more depth on capabilities.
[ACTION] search("Claude vs GPT-4 capabilities comparison")
[OBSERVATION] Found detailed comparison...

[FINAL ANSWER]
Based on research, the latest frameworks are...
```

---

### Pattern 3: Multi-Agent Orchestration

```bash
python src/agent_orchestration.py
```

**Expected Output**:
```
[INCOMING REQUEST]
User: "I want to order 2x Widget A and 1x Widget B"

[COORDINATOR ROUTING]
→ Checking inventory (Inventory Agent)
→ Processing payment (Payment Agent)
→ Arranging shipping (Shipping Agent)

[INVENTORY AGENT RESPONSE]
✓ Widget A: 2 units available
✓ Widget B: 1 unit available

[PAYMENT AGENT RESPONSE]
✓ Charged $249.99 to card ending in 4242

[SHIPPING AGENT RESPONSE]
✓ Estimated delivery: 2-3 business days. Tracking: SHIP123456

[COORDINATOR SUMMARY]
✓ Order #ORD789 fulfilled. All steps complete.
```

---

### Pattern 4: Planning + Execution

```bash
python src/planning_execution.py
```

**Expected Output**:
```
[PLANNING PHASE]
Task: Migrate 100 YouTube videos to course platform

Generated Plan:
1. Fetch video metadata from YouTube (100 videos)
2. Transform metadata to course format
3. Upload videos to platform
4. Create course structure
5. Validate all uploads

[CHECKPOINT]
👉 Plan ready for execution

[EXECUTION PHASE]
[1/5] Fetching metadata... ✓ (25s)
[2/5] Transforming metadata... ✓ (15s)
[3/5] Uploading videos... ⧗ (45s elapsed, 35% complete)
[4/5] Creating course structure... ⏳ (pending)
[5/5] Validating uploads... ⏳ (pending)

Progress: 35% complete
```

---

## 🖥️ Streamlit Viewer (Optional)

View demos with formatted cards and animations:

```bash
# Run a demo and pipe to viewer
python src/agent_executor.py | python src/streamlit_viewer.py

# Or run viewer standalone and load output file
python src/agent_executor.py > output.json
streamlit run src/streamlit_viewer.py -- --input output.json
```

---

## 🤖 Local LLM Setup (Optional)

### Using Ollama

```bash
# Install Ollama (https://ollama.ai)
# Pull a model
ollama pull llama3.2

# Start Ollama (runs on localhost:11434)
ollama serve

# Run demo - it will auto-detect Ollama
python src/agent_executor.py
```

### Using LM Studio

1. Download LM Studio from https://lmstudio.ai
2. Load a model and start the local server (localhost:1234)
3. Run any demo - it will auto-detect LM Studio

**Note**: If no local LLM is detected, demos fall back to mocked responses automatically.

---

## ⚠️ Troubleshooting

### Import Errors
```bash
# Ensure you're in the virtual environment
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Demo Takes Too Long
- Demos are designed to complete in <30 seconds
- If using local LLM, ensure it's responding quickly
- Fall back to mocked mode by stopping Ollama/LM Studio

### Streamlit Viewer Issues
```bash
# Install streamlit if missing
pip install streamlit

# Run with explicit port
streamlit run src/streamlit_viewer.py --server.port 8501
```

---

## 💡 Tips

- **Screen Recording**: Add `--slow` flag (if implemented) for longer delays between steps
- **JSON Only**: Redirect stderr to get clean JSON: `python src/agent_executor.py 2>/dev/null`
- **Multiple Demos**: Run demos in sequence for a full pattern comparison

---

## 🔗 Next Steps

- Review [spec.md](spec.md) for full requirements
- Check [data-model.md](data-model.md) for entity definitions
- See [contracts/](contracts/) for JSON schemas
