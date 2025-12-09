# Feature Specification: Agentic AI Design Pattern Demos

| Status | 🟢 Complete |
|--------|-------------|

| Version | Date       | Author | Changes                          |
|---------|------------|--------|----------------------------------|
| 0.1.0   | 2025-12-08 | Claude | Initial draft                    |
| 0.2.0   | 2025-12-08 | Claude | Added clarifications (LLM mode)  |
| 1.0.0   | 2025-12-08 | Claude | Implementation complete - all demos working |
| 1.1.0   | 2025-12-08 | Claude | Added Live Watch mode for side-by-side recording |

**Feature Branch**: `001-agentic-pattern-demos`
**Created**: 2025-12-08
**Status**: Complete
**Input**: User description: "Create working demos for 4 agentic AI design patterns using Microsoft Agent Framework"

## 🔍 Clarifications

### Session 2025-12-08

- Q: How should demos handle LLM calls? → A: Auto-detect local LLM (Ollama/LM Studio): use if available, fall back to mocked responses if not

## 📖 User Scenarios & Testing

### User Story 1 - Run Basic Agent-Executor Demo (Priority: P1)

As a developer learning agentic AI patterns, I want to run a customer support agent demo that uses tools to handle refunds and password resets, so that I can understand how agents select and invoke tools based on user requests.

**Why this priority**: The Agent-Executor pattern is the foundational building block for all agentic systems. Understanding tool selection and invocation is essential before exploring more complex patterns.

**Independent Test**: Can be fully tested by running a single script that processes 2-3 customer support requests and produces structured output showing the agent's thinking, tool calls, and responses.

**Acceptance Scenarios**:

1. **Given** the agent_executor.py script exists, **When** the user runs it, **Then** the demo completes within 30 seconds showing at least 2 customer interaction examples
2. **Given** a simulated refund request, **When** the agent processes it, **Then** the output shows `[AGENT THINKING]`, `[TOOL CALL]`, `[TOOL RESPONSE]`, and `[AGENT OUTPUT]` sections in sequence
3. **Given** the demo is running, **When** each step completes, **Then** both JSON-formatted and human-readable output are printed for each logical block

---

### User Story 2 - Run ReAct Loop Demo (Priority: P1)

As a developer learning agentic AI patterns, I want to run a research agent demo that shows the think-action-observation cycle, so that I can understand how agents reason iteratively and refine their approach based on observations.

**Why this priority**: The ReAct pattern is essential for understanding how agents reason about problems. It demonstrates the iterative nature of agentic problem-solving and is required before understanding multi-agent orchestration.

**Independent Test**: Can be fully tested by running a single script that researches a topic through 3-4 reasoning turns and produces clearly labeled thought/action/observation output.

**Acceptance Scenarios**:

1. **Given** the react_loop.py script exists, **When** the user runs it, **Then** the demo completes within 30 seconds showing at least 3 ReAct turns
2. **Given** a research topic (e.g., "latest AI frameworks"), **When** the agent processes it, **Then** each turn shows `[TURN N]`, `[THOUGHT]`, `[ACTION]`, and `[OBSERVATION]` sections
3. **Given** the demo completes all turns, **When** the final answer is produced, **Then** it is labeled with `[FINAL ANSWER]` and synthesizes information from previous observations

---

### User Story 3 - Run Multi-Agent Orchestration Demo (Priority: P2)

As a developer learning agentic AI patterns, I want to run an order fulfillment demo with a coordinator and specialist agents, so that I can understand how multiple agents collaborate and how a coordinator routes tasks and aggregates results.

**Why this priority**: Multi-agent systems build on the single-agent patterns. Understanding orchestration is valuable but requires foundational knowledge from P1 patterns first.

**Independent Test**: Can be fully tested by running a single script that processes an order through inventory, payment, and shipping agents with visible routing and aggregation.

**Acceptance Scenarios**:

1. **Given** the agent_orchestration.py script exists, **When** the user runs it, **Then** the demo completes within 30 seconds showing one end-to-end order flow
2. **Given** an incoming order request, **When** the coordinator processes it, **Then** the output shows routing to at least 3 specialist agents (Inventory, Payment, Shipping)
3. **Given** all specialist agents respond, **When** the coordinator summarizes, **Then** a `[COORDINATOR SUMMARY]` section shows aggregated results with success/failure indicators

---

### User Story 4 - Run Planning + Execution Demo (Priority: P2)

As a developer learning agentic AI patterns, I want to run a content migration demo that first creates a plan then executes it with checkpoints, so that I can understand how agents decompose complex tasks and track execution progress.

**Why this priority**: Planning+Execution is an advanced pattern that builds on understanding how agents think (ReAct) and how tasks are broken down. It's essential for complex agentic workflows.

**Independent Test**: Can be fully tested by running a single script that generates a visible plan, shows a validation checkpoint, then executes steps with progress indicators.

**Acceptance Scenarios**:

1. **Given** the planning_execution.py script exists, **When** the user runs it, **Then** the demo completes within 30 seconds showing planning and execution phases
2. **Given** a content migration task (e.g., migrate 100 videos), **When** the planning phase runs, **Then** a numbered plan of 3-5 steps is displayed under `[PLANNING PHASE]`
3. **Given** the plan is generated, **When** execution begins, **Then** each step shows progress with status indicators (✓ complete, ⧗ in-progress, ⏳ pending)

---

### User Story 5 - View Demos in Streamlit Viewer (Priority: P3)

As a developer or presenter, I want to run demos through a Streamlit viewer that renders the output as formatted cards with animations, so that I can create screen recordings or embed videos that clearly show each pattern.

**Why this priority**: The viewer enhances presentation but is not required to understand the patterns. The core demos (P1/P2) provide full value without it.

**Independent Test**: Can be fully tested by piping any demo's JSON output to the viewer and verifying it renders cards for each step type.

**Acceptance Scenarios**:

1. **Given** the streamlit_viewer.py script exists, **When** a user pipes demo output to it, **Then** the viewer displays formatted cards for each step
2. **Given** JSON output from any demo, **When** the viewer processes it, **Then** different step types (thinking, action, observation, etc.) are visually distinguished
3. **Given** the viewer is running, **When** new output arrives, **Then** cards appear with appropriate animations for screen recording

---

### User Story 6 - Live Watch Mode for Side-by-Side Recording (Priority: P3)

As a presenter, I want to view agent output in real-time as styled cards while the demo runs in a terminal, so that I can record side-by-side videos showing both the terminal output and the visual dashboard.

**Why this priority**: Live Watch enhances presentation for screen recordings but is not required to understand the patterns.

**Independent Test**: Can be fully tested by running a demo with output redirected to a file while Streamlit watches the file and renders cards in real-time.

**Acceptance Scenarios**:

1. **Given** Streamlit viewer is in Live Watch mode, **When** a demo writes output to the watch file, **Then** the viewer displays cards within 1-2 seconds
2. **Given** the watch file contains mixed JSON and text content, **When** the parser processes it, **Then** only valid JSON objects are rendered as cards (text lines are ignored)
3. **Given** Live Watch stops displaying cards, **When** the user follows the Quick Reset Procedure, **Then** the viewer resumes displaying cards correctly

---

### ⚠️ Edge Cases

- What happens when a demo script encounters an import error? The script should fail fast with a clear error message indicating missing dependencies
- What happens when output exceeds terminal buffer? Each step should be atomic and self-contained; partial output should still be parseable
- What happens when the Streamlit viewer receives malformed JSON? The viewer should display an error card indicating the parsing failure without crashing
- What happens when a mocked tool returns an unexpected response format? The agent should handle gracefully and continue with error indication in output

## ✅ Requirements

### Functional Requirements

- **FR-001**: Each demo MUST be a standalone Python script that can be executed independently without requiring the other demos
- **FR-002**: Each demo MUST complete execution in under 30 seconds
- **FR-003**: All demo output MUST include both JSON-formatted and human-readable text for each logical step
- **FR-004**: Each demo MUST use clear delimiters to separate logical sections (`[AGENT THINKING]`, `[TOOL CALL]`, etc.)
- **FR-005**: All tools in demos MUST be mocked and return realistic JSON responses
- **FR-016**: Demos MUST auto-detect local LLM availability (Ollama/LM Studio) and use it if present; otherwise fall back to mocked/scripted agent responses
- **FR-006**: Tool definitions MUST include name, description, and parameters with JSON Schema types
- **FR-007**: Demo output MUST use progress indicators (✓, ⧗, ⏳, →) for visual clarity
- **FR-008**: Each demo MUST include small delays (0.3-0.5 seconds) between steps for readability
- **FR-009**: The Agent-Executor demo MUST show at least 2 customer interaction examples (refund and password reset)
- **FR-010**: The ReAct Loop demo MUST show at least 3 complete think-action-observation turns
- **FR-011**: The Multi-Agent Orchestration demo MUST include a coordinator and at least 3 specialist agents
- **FR-012**: The Planning+Execution demo MUST show a distinct planning phase followed by step-by-step execution with progress tracking
- **FR-013**: A README MUST be provided with setup instructions, usage examples, and expected output samples
- **FR-014**: A requirements.txt MUST list all dependencies with pinned versions
- **FR-015**: The optional Streamlit viewer MUST accept JSON output and render formatted cards for all defined step types
- **FR-017**: The Streamlit viewer MUST support a Live Watch mode that polls a file for new content and auto-refreshes
- **FR-018**: The Live Watch mode MUST parse mixed JSON/text content, extracting only valid JSON objects for rendering
- **FR-019**: A DEMO_SCRIPT.md MUST be provided with recording instructions, troubleshooting guide, and talking points for each demo

### 📦 Key Entities

- **Demo Script**: A standalone Python file implementing one agentic pattern; has a name, pattern type, and produces structured output
- **Tool**: A mocked function with a schema (name, description, parameters) and returns realistic JSON responses; used by agents to perform actions
- **Step Output**: A logical unit of demo output containing a type (thinking, action, observation, etc.) and content; emitted in both JSON and human-readable format
- **Agent**: A simulated AI entity that processes requests, selects tools, and produces responses; each pattern demonstrates different agent behaviors
- **Coordinator**: A specialized agent that routes tasks to other agents and aggregates their responses; used in orchestration pattern
- **Specialist Agent**: An agent with domain-specific capabilities (inventory, payment, shipping); responds to coordinator requests

### 💡 Assumptions

- Users have Python 3.8+ installed on their system
- Users are familiar with running Python scripts from the command line
- The Microsoft Agent Framework (autogen or autogen-agentchat) is the preferred library for agent implementation
- Mocked tool responses represent realistic patterns that would come from actual APIs
- Small delays in output are acceptable for educational/demonstration purposes
- The Streamlit viewer is optional and not required for core demo functionality

## 🎯 Success Criteria

### Measurable Outcomes

- **SC-001**: All 4 demo scripts execute successfully and complete in under 30 seconds each
- **SC-002**: A first-time user can set up and run all demos within 5 minutes using only the README instructions
- **SC-003**: Demo output is parseable by the Streamlit viewer with zero parsing errors
- **SC-004**: Each demo produces at least 5 distinct step outputs that can be visually distinguished
- **SC-005**: Developers watching the demos can identify the unique characteristics of each agentic pattern within the first 30 seconds of output
- **SC-006**: All demos run without requiring cloud API keys; local LLM (Ollama/LM Studio) is optional but utilized when available
- **SC-007**: The output format allows for easy creation of screen recordings or video embeds for presentations

## 📋 Implementation Summary

### Files Created

| File | Description |
|------|-------------|
| `src/agent_executor.py` | Agent-Executor pattern demo (customer support with tool selection) |
| `src/react_loop.py` | ReAct Loop pattern demo (research agent with think-action-observation) |
| `src/agent_orchestration.py` | Multi-Agent Orchestration demo (coordinator + specialist agents) |
| `src/planning_execution.py` | Planning+Execution pattern demo (plan generation + progress tracking) |
| `src/streamlit_viewer.py` | Streamlit viewer with Live Watch mode for real-time visualization |
| `src/common/output.py` | Shared output utilities (log_step, step_delay) |
| `requirements.txt` | Python dependencies |
| `README.md` | Setup instructions and usage guide |
| `DEMO_SCRIPT.md` | Recording script with talking points and troubleshooting |

### Key Features Implemented

1. **All 4 demo patterns** execute in under 30 seconds with structured output
2. **Mock responses** - no cloud API keys required
3. **UTF-8 encoding fix** for Windows terminal compatibility
4. **Streamlit viewer** with 4 input modes: Upload, Paste JSON, Sample Data, Live Watch
5. **Live Watch mode** with file polling, JSON extraction, and auto-refresh
6. **Comprehensive troubleshooting guide** in DEMO_SCRIPT.md

### Architecture

```
src/
├── common/
│   └── output.py          # Shared utilities (log_step, step_delay)
├── agent_executor.py      # Demo 1: Agent-Executor
├── react_loop.py          # Demo 2: ReAct Loop
├── agent_orchestration.py # Demo 3: Multi-Agent Orchestration
├── planning_execution.py  # Demo 4: Planning+Execution
└── streamlit_viewer.py    # Demo 5-6: Viewer + Live Watch
```

### Live Watch Architecture

```
Demo Script ──► output/live_demo.txt ──► Streamlit Viewer
   (writes)          (file)              (polls & renders)
```
