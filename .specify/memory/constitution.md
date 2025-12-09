<!--
Sync Impact Report
==================
Version change: 1.0.0 → 1.1.0 (Added Documentation Standards section)
Modified principles: None
Added sections:
  - Documentation Standards (new section with emoji, status bar, version table requirements)
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ No changes required (generic template)
  - .specify/templates/spec-template.md: ✅ No changes required (generic template)
  - .specify/templates/tasks-template.md: ✅ No changes required (generic template)
Follow-up TODOs: None
-->

# Agentic AI Design Pattern Demos Constitution

## Core Principles

### I. Demonstration Clarity

Each demo script MUST be a standalone, self-contained Python file that clearly
illustrates exactly one agentic AI design pattern. Demos MUST NOT combine multiple
patterns in a single file. Each script MUST run end-to-end successfully in under
30 seconds with no external dependencies beyond those declared in requirements.txt.

**Rationale**: The primary purpose is educational demonstration. Mixing patterns
or creating complex interdependencies defeats the learning objective.

### II. Structured Output Protocol

All demo output MUST follow the structured logging format for Streamlit parsing:
- Use clear delimiters: `[AGENT THINKING]`, `[TOOL CALL]`, `[TOOL RESPONSE]`,
  `[AGENT OUTPUT]`, `[TURN N]`, `[THOUGHT]`, `[ACTION]`, `[OBSERVATION]`
- Emit both JSON-parseable output and human-readable formatted text
- Use progress indicators (✓, ⧗, ⏳, →) for visual clarity
- Include small delays (0.3-0.5s) between steps for readability in recordings
- Each logical block (thinking → action → observation) MUST print atomically

**Rationale**: Output consistency enables the Streamlit viewer to parse and render
demos uniformly. Screen recording and embedding require predictable, timed output.

### III. Mocked Tool Realism

All tools MUST be mocked but MUST return realistic, well-structured JSON responses.
Tool schemas MUST include:
- Descriptive `name` field
- Clear `description` explaining the tool's purpose
- Complete `parameters` object with JSON Schema type definitions
- Example responses that mirror real-world API patterns

Tools MUST NOT require actual API keys or external service calls during demo execution.

**Rationale**: Realistic mocking teaches correct integration patterns without
requiring environment setup or incurring costs during demonstrations.

### IV. Pattern Fidelity

Each demo MUST faithfully implement its designated agentic pattern:
- **Agent-Executor**: Clear tool selection, invocation, and response synthesis
- **ReAct Loop**: Explicit think→action→observation cycles with minimum 3 turns
- **Multi-Agent Orchestration**: Distinct specialist agents with coordinator routing
- **Planning+Execution**: Visible plan generation, validation checkpoint, step-by-step execution

Demos MUST NOT oversimplify patterns to the point where the architectural insight is lost.

**Rationale**: Demonstrations serve as reference implementations. Pattern integrity
ensures viewers learn correct agentic architectures.

### V. Simplicity Over Sophistication

Demos MUST prioritize readability and understandability over production-grade
complexity. YAGNI applies strictly:
- No unnecessary abstractions or design patterns beyond the demonstrated concept
- No configuration systems; hardcode reasonable defaults
- No extensive error handling unless it illustrates the pattern
- Keep each script under 300 lines of code (excluding comments)

**Rationale**: These are teaching tools, not production systems. Complexity obscures
the learning objective.

## Output Standards

All demo scripts MUST implement the `log_step` helper function:

```python
def log_step(step_type: str, content: str) -> None:
    """Print structured output for Streamlit parsing."""
    output = {"type": step_type, "content": content}
    print(json.dumps(output))
    print(f"\n[{step_type.upper()}]\n{content}\n")
```

Step types MUST be one of: `thinking`, `action`, `observation`, `response`, `error`,
`routing`, `summary`, `planning`, `execution`, `checkpoint`.

JSON output MUST precede human-readable output for each step.

## Documentation Standards

All documentation files (README.md, guides, specs) MUST include the following elements:

### 📋 Required Elements

1. **Emojis**: Use descriptive emojis to enhance visual scanning and section identification:
   - 🚀 Getting Started / Quick Start
   - 📦 Installation / Dependencies
   - 🔧 Configuration / Setup
   - 📖 Usage / Examples
   - 🧪 Testing
   - ⚠️ Warnings / Important Notes
   - ✅ Success / Completed
   - ❌ Errors / Failures
   - 💡 Tips / Best Practices
   - 🔗 References / Links

2. **Status Bar**: Every document MUST include a status bar at the top showing current state:
   ```
   | Status | Description |
   |--------|-------------|
   | 🟢 Ready | Document is complete and approved |
   | 🟡 Draft | Document is in progress |
   | 🔴 Blocked | Document requires resolution |
   | 🔵 Review | Document awaiting review |
   ```

3. **Version Table**: Every document MUST include a version history table:
   ```
   | Version | Date | Author | Changes |
   |---------|------|--------|---------|
   | 1.0.0 | YYYY-MM-DD | Name | Initial release |
   | 1.1.0 | YYYY-MM-DD | Name | Added feature X |
   ```

**Rationale**: Visual elements improve document discoverability and scanability. Status bars
provide immediate context. Version tables enable change tracking and accountability.

## Development Workflow

1. **File Naming**: Demo scripts MUST use snake_case matching the pattern name:
   - `agent_executor.py`
   - `react_loop.py`
   - `agent_orchestration.py`
   - `planning_execution.py`

2. **Documentation**: README.md MUST include:
   - Setup instructions with exact commands
   - Expected output samples for each demo
   - Streamlit viewer usage instructions
   - Status bar and version table (per Documentation Standards)

3. **Dependencies**: requirements.txt MUST list all dependencies with pinned versions.
   Prefer `autogen` or `autogen-agentchat` for Microsoft Agent Framework integration.

4. **Viewer Integration**: The optional `streamlit_viewer.py` MUST:
   - Accept JSON output via stdin or file
   - Render formatted cards with appropriate animations
   - Support all defined step types

## Governance

This constitution supersedes informal conventions for this demonstration project.
Amendments require:
1. Clear rationale for the change
2. Impact assessment on existing demos
3. Version increment following semantic versioning

All pull requests MUST verify demos still execute within the 30-second limit and
produce parseable structured output.

Complexity beyond these principles MUST be explicitly justified in code comments
referencing the specific principle being relaxed and why.

**Version**: 1.1.0 | **Ratified**: 2025-12-08 | **Last Amended**: 2025-12-08
