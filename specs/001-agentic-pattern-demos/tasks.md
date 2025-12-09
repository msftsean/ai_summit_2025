# Tasks: Agentic AI Design Pattern Demos

| Status | 🟡 Draft |
|--------|----------|

| Version | Date       | Author | Changes         |
|---------|------------|--------|-----------------|
| 1.0.0   | 2025-12-08 | Claude | Initial tasks   |

**Input**: Design documents from `/specs/001-agentic-pattern-demos/`
**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅, contracts/ ✅

**Tests**: Tests are NOT explicitly requested in the specification. Demos are self-validating.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each demo pattern.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4, US5)
- Include exact file paths in descriptions

## Path Conventions

Based on plan.md structure:
```
src/
├── agent_executor.py       # US1
├── react_loop.py           # US2
├── agent_orchestration.py  # US3
├── planning_execution.py   # US4
├── streamlit_viewer.py     # US5
└── common/
    ├── __init__.py
    ├── output.py
    └── llm_provider.py
```

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure: src/, src/common/
- [x] T002 Create requirements.txt with pinned dependencies (autogen-agentchat>=0.4.0, requests>=2.31.0, ollama>=0.3.0, streamlit>=1.29.0)
- [x] T003 [P] Create src/common/__init__.py with package exports

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Implement log_step() function in src/common/output.py with JSON+human-readable dual output format
- [x] T005 [P] Implement LLM auto-detection in src/common/llm_provider.py (Ollama check at localhost:11434, LM Studio check at localhost:1234, mock fallback)
- [x] T006 [P] Create MockLLMProvider class in src/common/llm_provider.py with scripted responses
- [x] T007 Add step type constants to src/common/output.py (thinking, action, observation, response, error, routing, summary, planning, execution, checkpoint)
- [x] T008 Add delay helper function to src/common/output.py (0.3-0.5s configurable delay)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Agent-Executor Demo (Priority: P1) 🎯 MVP

**Goal**: Create customer support agent demo showing tool selection and invocation for refunds and password resets

**Independent Test**: Run `python src/agent_executor.py` - should complete in <30s showing 2+ customer interactions with [AGENT THINKING], [TOOL CALL], [TOOL RESPONSE], [AGENT OUTPUT] sections

### Implementation for User Story 1

- [x] T009 [US1] Define refund_processor tool schema in src/agent_executor.py (name, description, parameters with order_id and reason)
- [x] T010 [P] [US1] Define password_reset tool schema in src/agent_executor.py (name, description, parameters with email)
- [x] T011 [US1] Implement mock_refund_processor() function in src/agent_executor.py returning realistic JSON response
- [x] T012 [P] [US1] Implement mock_password_reset() function in src/agent_executor.py returning realistic JSON response
- [x] T013 [US1] Implement CustomerSupportAgent class in src/agent_executor.py with tool selection logic
- [x] T014 [US1] Implement run_refund_scenario() function showing complete refund flow with structured output
- [x] T015 [US1] Implement run_password_reset_scenario() function showing complete password reset flow
- [x] T016 [US1] Add main() function in src/agent_executor.py that runs both scenarios sequentially
- [x] T017 [US1] Add if __name__ == "__main__" block to src/agent_executor.py

**Checkpoint**: User Story 1 complete - Agent-Executor demo runs independently

---

## Phase 4: User Story 2 - ReAct Loop Demo (Priority: P1) 🎯 MVP

**Goal**: Create research agent demo showing think→action→observation cycles for investigating AI frameworks

**Independent Test**: Run `python src/react_loop.py` - should complete in <30s showing 3+ ReAct turns with [TURN N], [THOUGHT], [ACTION], [OBSERVATION] sections and [FINAL ANSWER]

### Implementation for User Story 2

- [x] T018 [US2] Define search tool schema in src/react_loop.py (name, description, parameters with query)
- [x] T019 [US2] Implement mock_search() function in src/react_loop.py with staged search results for AI frameworks topic
- [x] T020 [US2] Implement ReActAgent class in src/react_loop.py with thought/action/observation cycle
- [x] T021 [US2] Implement run_react_turn() function that outputs [TURN N], [THOUGHT], [ACTION], [OBSERVATION]
- [x] T022 [US2] Implement research_ai_frameworks() function running 3-4 ReAct turns
- [x] T023 [US2] Add final answer synthesis outputting [FINAL ANSWER] section
- [x] T024 [US2] Add main() function and __main__ block to src/react_loop.py

**Checkpoint**: User Story 2 complete - ReAct Loop demo runs independently

---

## Phase 5: User Story 3 - Multi-Agent Orchestration Demo (Priority: P2)

**Goal**: Create order fulfillment demo with coordinator routing to Inventory, Payment, and Shipping specialist agents

**Independent Test**: Run `python src/agent_orchestration.py` - should complete in <30s showing routing to 3 specialist agents with [COORDINATOR ROUTING], individual agent responses, and [COORDINATOR SUMMARY]

### Implementation for User Story 3

- [x] T025 [US3] Implement InventoryAgent class in src/agent_orchestration.py with check_inventory() method
- [x] T026 [P] [US3] Implement PaymentAgent class in src/agent_orchestration.py with process_payment() method
- [x] T027 [P] [US3] Implement ShippingAgent class in src/agent_orchestration.py with arrange_shipping() method
- [x] T028 [US3] Implement CoordinatorAgent class in src/agent_orchestration.py with route_to_specialists() logic
- [x] T029 [US3] Implement mock responses for each specialist agent returning realistic JSON
- [x] T030 [US3] Implement process_order() function showing full orchestration flow with routing output
- [x] T031 [US3] Add summary aggregation outputting [COORDINATOR SUMMARY] with success/failure indicators
- [x] T032 [US3] Add main() function and __main__ block to src/agent_orchestration.py

**Checkpoint**: User Story 3 complete - Multi-Agent Orchestration demo runs independently

---

## Phase 6: User Story 4 - Planning + Execution Demo (Priority: P2)

**Goal**: Create content migration demo showing plan generation, validation checkpoint, and step-by-step execution with progress

**Independent Test**: Run `python src/planning_execution.py` - should complete in <30s showing [PLANNING PHASE] with numbered plan, [CHECKPOINT], and [EXECUTION PHASE] with progress indicators (✓ ⧗ ⏳)

### Implementation for User Story 4

- [x] T033 [US4] Define Plan and PlanStep data classes in src/planning_execution.py matching data-model.md
- [x] T034 [US4] Implement PlanningAgent class in src/planning_execution.py with generate_plan() method
- [x] T035 [US4] Implement generate_migration_plan() returning 5-step plan for video migration
- [x] T036 [US4] Implement output_planning_phase() showing [PLANNING PHASE] with numbered steps
- [x] T037 [US4] Implement output_checkpoint() showing [CHECKPOINT] validation message
- [x] T038 [US4] Implement execute_plan() function with simulated step execution and progress tracking
- [x] T039 [US4] Implement output_execution_step() showing step number, status indicator (✓ ⧗ ⏳), and progress percentage
- [x] T040 [US4] Add main() function and __main__ block to src/planning_execution.py

**Checkpoint**: User Story 4 complete - Planning+Execution demo runs independently

---

## Phase 7: User Story 5 - Streamlit Viewer (Priority: P3)

**Goal**: Create Streamlit app that renders demo JSON output as formatted cards with visual styling per step type

**Independent Test**: Run any demo and pipe to viewer, or load saved JSON - viewer should display styled cards for each step type

### Implementation for User Story 5

- [x] T041 [US5] Create basic Streamlit app structure in src/streamlit_viewer.py with page config
- [x] T042 [US5] Implement JSON line parser for reading structured output
- [x] T043 [US5] Define card styling mapping for each step type (colors: thinking=blue, action=orange, observation=green, etc.)
- [x] T044 [US5] Implement render_step_card() function displaying styled card with icon and content
- [x] T045 [US5] Add file input option for loading saved demo output
- [x] T046 [US5] Add stdin reading support for piped demo output
- [x] T047 [US5] Add CSS animations for card appearance (fade-in effect)
- [x] T048 [US5] Add main() and Streamlit entry point to src/streamlit_viewer.py

**Checkpoint**: User Story 5 complete - Streamlit viewer renders all demo outputs

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Documentation and final validation

- [x] T049 [P] Create README.md with status bar, version table, emojis per constitution Documentation Standards
- [x] T050 [P] Add 🚀 Getting Started section to README.md with installation commands
- [x] T051 [P] Add 📖 Usage section to README.md with example commands for each demo
- [x] T052 Add expected output samples for each demo to README.md
- [x] T053 Add 🖥️ Streamlit Viewer section to README.md with usage instructions
- [x] T054 Add 🤖 Local LLM Setup section to README.md (Ollama and LM Studio instructions)
- [x] T055 Add ⚠️ Troubleshooting section to README.md
- [x] T056 Validate all demos complete in <30 seconds
- [x] T057 Validate all demos produce parseable JSON output
- [x] T058 Run quickstart.md validation - ensure all documented commands work

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - US1 and US2 are both P1 - can run in parallel
  - US3 and US4 are both P2 - can run in parallel after P1 if desired
  - US5 (P3) can start after Foundational but benefits from having demo output to test with
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

- **US1 (Agent-Executor)**: Depends only on Phase 2 - No dependencies on other stories
- **US2 (ReAct Loop)**: Depends only on Phase 2 - No dependencies on other stories
- **US3 (Multi-Agent)**: Depends only on Phase 2 - No dependencies on other stories
- **US4 (Planning)**: Depends only on Phase 2 - No dependencies on other stories
- **US5 (Streamlit)**: Depends only on Phase 2 - Can use any demo's output for testing

### Within Each User Story

- Tool schemas before mock implementations
- Mock implementations before agent classes
- Agent classes before scenario functions
- Scenario functions before main()

### Parallel Opportunities

- T002 and T003 can run in parallel (Phase 1)
- T005 and T006 can run in parallel (Phase 2)
- T009 and T010 can run in parallel (US1 tool schemas)
- T011 and T012 can run in parallel (US1 mock implementations)
- T025, T026, T027 can run in parallel (US3 specialist agents)
- T049, T050, T051 can run in parallel (README sections)
- All user stories (US1-US5) can run in parallel after Phase 2

---

## Parallel Example: User Story 1

```bash
# Launch tool schema tasks together:
Task: "T009 [US1] Define refund_processor tool schema in src/agent_executor.py"
Task: "T010 [P] [US1] Define password_reset tool schema in src/agent_executor.py"

# Launch mock implementation tasks together:
Task: "T011 [US1] Implement mock_refund_processor() function in src/agent_executor.py"
Task: "T012 [P] [US1] Implement mock_password_reset() function in src/agent_executor.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1 + 2)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Agent-Executor)
4. **VALIDATE**: Run `python src/agent_executor.py` - confirm <30s, structured output
5. Complete Phase 4: User Story 2 (ReAct Loop)
6. **VALIDATE**: Run `python src/react_loop.py` - confirm <30s, 3+ turns
7. 🎯 **MVP COMPLETE**: Two foundational patterns working

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add US1 (Agent-Executor) → Test → Demo ready (minimal MVP)
3. Add US2 (ReAct Loop) → Test → Two patterns (P1 complete)
4. Add US3 (Multi-Agent) → Test → Three patterns
5. Add US4 (Planning) → Test → All four core patterns (P2 complete)
6. Add US5 (Streamlit) → Test → Full visualization (P3 complete)
7. Polish → README, validation → Release ready

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: US1 (Agent-Executor) + US3 (Multi-Agent)
   - Developer B: US2 (ReAct Loop) + US4 (Planning)
   - Developer C: US5 (Streamlit) + Polish
3. All stories complete and run independently

---

## Notes

- [P] tasks = different files, no dependencies on incomplete tasks
- [Story] label maps task to specific user story for traceability
- Each user story produces one independently runnable demo script
- Demos are self-validating (no separate test suite required)
- Commit after each task or logical group
- Stop at any checkpoint to validate demo independently
- Constitution limits: <300 LOC per script, <30s execution
