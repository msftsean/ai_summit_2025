# Demo Script: Agentic AI Design Patterns

| Status | 🟢 Ready for Recording |
|--------|------------------------|

| Version | Date       | Author | Changes        |
|---------|------------|--------|----------------|
| 1.0.0   | 2025-12-08 | Claude | Initial script |

## 📋 Pre-Recording Checklist

### Environment Setup

- [ ] Python 3.8+ installed and in PATH
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Terminal font supports Unicode (for checkmarks ✓, arrows →, progress bars █░)
- [ ] Terminal window sized appropriately (recommend 120 cols x 40 rows)
- [ ] VS Code or terminal theme with good contrast for recording

### Optional: Local LLM

- [ ] Ollama running at localhost:11434 (or)
- [ ] LM Studio running at localhost:1234 (or)
- [ ] Azure AI Foundry Local running at localhost:5272
- [ ] If no LLM available, demos will use mock responses (still works!)

### Test Run

```bash
cd c:\Users\segayle\repos\ai_summit
python src/agent_executor.py
```

If this runs without errors, you're ready to record.

---

## 🎬 Demo 1: Agent-Executor Pattern

**Duration**: ~15 seconds
**File**: `src/agent_executor.py`
**Pattern**: Tool Selection & Invocation

### What to Say

> "This demo shows the Agent-Executor pattern - the foundation of agentic AI. Watch how the agent analyzes a customer request, selects the appropriate tool, and processes the response."

### Command

```bash
python src/agent_executor.py
```

### Key Points to Highlight

1. **[THINKING]** - Agent analyzes the request and available tools
2. **[ACTION]** - Agent selects and calls the `refund_processor` tool
3. **[OBSERVATION]** - Tool returns structured JSON response
4. **[RESPONSE]** - Agent formats a human-friendly answer

### Expected Output Preview

```
============================================================
AGENT-EXECUTOR PATTERN DEMO
   Customer Support Agent with Tool Selection
============================================================

[THINKING]
Analyzing user request: "I want a refund for order 12345..."
Available tools: ['refund_processor', 'password_reset']

[THINKING]
Selected tool: refund_processor

[ACTION]
Function: refund_processor
Params: {
  "order_id": "12345",
  "reason": "not as described"
}

[OBSERVATION]
{
  "status": "success",
  "refund_id": "REF-12345-...",
  "amount": 99.99,
  ...
}

[RESPONSE]
✓ Refund processed successfully!
  Refund ID: REF-12345-...
  Amount: $99.99 USD
```

### Talking Points

- "Notice the structured output - both JSON for machines and human-readable text"
- "The agent chose `refund_processor` over `password_reset` based on intent analysis"
- "This pattern is the building block for all other agentic patterns"

---

## 🎬 Demo 2: ReAct Loop Pattern

**Duration**: ~20 seconds
**File**: `src/react_loop.py`
**Pattern**: Think → Action → Observation Cycle

### What to Say

> "The ReAct pattern shows iterative reasoning. The agent thinks, takes an action, observes the result, then thinks again. This cycle continues until it has enough information to answer."

### Command

```bash
python src/react_loop.py
```

### Key Points to Highlight

1. **[TURN N]** - Each reasoning cycle is numbered
2. **[THOUGHT]** - Agent's internal reasoning
3. **[ACTION]** - Search or tool invocation
4. **[OBSERVATION]** - Results from the action
5. **[FINAL ANSWER]** - Synthesized response after multiple turns

### Expected Output Preview

```
============================================================
REACT LOOP PATTERN DEMO
   Research Agent with Think->Action->Observation Cycle
============================================================

──────────────────────────────────────────────────
[THINKING]
Turn 1 Thought:
I need to research the latest AI frameworks...

[ACTION]
Action: search("Claude vs GPT-4 capabilities")

[OBSERVATION]
Found 5 results:
  1. Claude excels at nuanced reasoning...
  2. GPT-4 has strong multimodal capabilities...

──────────────────────────────────────────────────
[THINKING]
Turn 2 Thought:
I should also look at open-source alternatives...

... (continues for 3 turns) ...

[RESPONSE]
[FINAL ANSWER]
Based on my research, here are the latest AI frameworks in 2025:
• Claude (Anthropic) - Known for nuanced reasoning
• GPT-4 Turbo (OpenAI) - Multimodal with vision
...
```

### Talking Points

- "Each turn builds on previous observations"
- "The agent decides when it has enough information to stop"
- "This is how agents solve complex, multi-step research tasks"

---

## 🎬 Demo 3: Multi-Agent Orchestration Pattern

**Duration**: ~20 seconds
**File**: `src/agent_orchestration.py`
**Pattern**: Coordinator + Specialist Agents

### What to Say

> "Multi-agent orchestration shows how a coordinator agent routes tasks to specialists. Here we have Inventory, Payment, and Shipping agents working together to fulfill an order."

### Command

```bash
python src/agent_orchestration.py
```

### Key Points to Highlight

1. **[COORDINATOR ROUTING]** - Shows the execution plan
2. **→ Routing to [Agent]** - Handoff to specialist
3. **[Agent RESPONSE]** - Each specialist's output
4. **[COORDINATOR SUMMARY]** - Aggregated results

### Expected Output Preview

```
============================================================
MULTI-AGENT ORCHESTRATION PATTERN DEMO
   Order Fulfillment with Coordinator + Specialists
============================================================

[PLANNING]
[COORDINATOR ROUTING]
→ Step 1: Check inventory (Inventory Agent)
→ Step 2: Process payment (Payment Agent)
→ Step 3: Arrange shipping (Shipping Agent)

[ROUTING]
→ Routing to InventoryAgent

[OBSERVATION]
[InventoryAgent RESPONSE]
  ✓ Widget A: 2 requested, 50 available
  ✓ Widget B: 1 requested, 25 available

[ROUTING]
→ Routing to PaymentAgent

[OBSERVATION]
[PaymentAgent RESPONSE]
  ✓ Charged $249.97 to card ending in 4242
  Transaction: TXN-...

[ROUTING]
→ Routing to ShippingAgent

[OBSERVATION]
[ShippingAgent RESPONSE]
  ✓ Shipping arranged via FastShip Express
  Tracking: SHIP-...

[SUMMARY]
[COORDINATOR SUMMARY]
Order ID: ORD-...
✓ Order fulfilled successfully!
```

### Talking Points

- "The coordinator doesn't do the work - it delegates to specialists"
- "Each agent has domain expertise (inventory, payments, shipping)"
- "If inventory fails, the coordinator stops - no payment processed"
- "This is how enterprise workflows are built with agents"

---

## 🎬 Demo 4: Planning + Execution Pattern

**Duration**: ~25 seconds
**File**: `src/planning_execution.py`
**Pattern**: Plan Generation → Checkpoint → Step Execution

### What to Say

> "The Planning + Execution pattern shows how agents handle complex tasks. First, the agent creates a plan. Then there's a validation checkpoint. Finally, it executes each step with progress tracking."

### Command

```bash
python src/planning_execution.py
```

### Key Points to Highlight

1. **[PLANNING PHASE]** - Generated plan with numbered steps
2. **[CHECKPOINT]** - Validation before execution
3. **[STEP N/5]** - Progress indicators (⧗ in-progress, ✓ complete)
4. **Progress bars** - Visual feedback [██████░░░░]
5. **[EXECUTION SUMMARY]** - Final status report

### Expected Output Preview

```
============================================================
PLANNING + EXECUTION PATTERN DEMO
   Content Migration with Plan Generation & Progress
============================================================

[PLANNING]
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

[EXECUTION]
[STEP 1/5] ⧗ Fetch video metadata from YouTube
  Progress: [██████████] 100%

[EXECUTION]
[STEP 1/5] ✓ Fetch video metadata from YouTube
  Duration: 12s

... (steps 2-5) ...

[SUMMARY]
[EXECUTION SUMMARY]
✓ Steps completed: 5/5
✓ Migration completed successfully!
```

### Talking Points

- "The plan is generated BEFORE any execution begins"
- "The checkpoint allows for human review or automated validation"
- "Progress bars show real-time status - great for long-running tasks"
- "This pattern is essential for reliable automation"

---

## 🎬 Demo 5: Streamlit Viewer (Optional)

**Duration**: ~30 seconds
**File**: `src/streamlit_viewer.py`
**Pattern**: Visualization of Agent Output

### What to Say

> "The Streamlit viewer renders agent output as styled cards. This is great for presentations, debugging, or building dashboards around your agents."

### Command

```bash
streamlit run src/streamlit_viewer.py
```

### Steps to Show

1. Browser opens automatically to localhost:8501
2. Click "Sample Data" in sidebar to load example output
3. Show color-coded cards for different step types
4. Demonstrate filtering by step type
5. Show file upload option

### Talking Points

- "Each step type has its own color and icon"
- "You can filter to focus on specific step types"
- "Upload any demo's JSON output for visualization"
- "Great for creating polished recordings or dashboards"

---

## 🎯 Quick Reference: All Commands

```bash
# Demo 1: Agent-Executor
python src/agent_executor.py

# Demo 2: ReAct Loop
python src/react_loop.py

# Demo 3: Multi-Agent Orchestration
python src/agent_orchestration.py

# Demo 4: Planning + Execution
python src/planning_execution.py

# Demo 5: Streamlit Viewer
streamlit run src/streamlit_viewer.py
```

---

## 🎥 Recording Tips

### Terminal Setup

1. **Font Size**: 14-16pt for readability
2. **Theme**: Dark background with light text (high contrast)
3. **Window Size**: Wide enough to avoid line wrapping
4. **Clear screen** before each demo: `cls` (Windows) or `clear` (Mac/Linux)

### Pacing

- Pause 2-3 seconds after running command before speaking
- Let the output finish before explaining
- Point out specific sections as they appear

### If Something Goes Wrong

- Demos use mock responses - no external API needed
- If Unicode fails, the UTF-8 wrapper will replace characters
- Each demo is independent - one failure doesn't affect others

### Saving Output for Later

```bash
# Save to file for Streamlit viewer
python src/agent_executor.py > demo1_output.txt 2>&1
python src/react_loop.py > demo2_output.txt 2>&1
python src/agent_orchestration.py > demo3_output.txt 2>&1
python src/planning_execution.py > demo4_output.txt 2>&1
```

---

## ✅ Post-Recording Checklist

- [ ] All 4 demos recorded successfully
- [ ] Audio is clear and synced with output
- [ ] Key sections highlighted/annotated
- [ ] Streamlit viewer shown (optional)
- [ ] Output files saved for reference
