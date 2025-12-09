"""
Planning + Execution Pattern Demo

Demonstrates a content migration system that first creates a plan,
shows a validation checkpoint, then executes step-by-step with progress.

Pattern: Planning + Execution (Decompose, Validate, Execute)
"""

import json
import time
import sys
sys.path.insert(0, '.')

from common.output import log_step, step_delay

# =============================================================================
# Data Classes (T033)
# =============================================================================

class PlanStep:
    """Represents a single step in an execution plan."""

    def __init__(self, number: int, title: str, description: str = ""):
        self.number = number
        self.title = title
        self.description = description
        self.status = "pending"  # pending, in_progress, completed, failed
        self.progress = 0
        self.duration = None

    def to_dict(self) -> dict:
        return {
            "number": self.number,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "progress": self.progress,
            "duration": self.duration
        }


class Plan:
    """Represents a generated execution plan."""

    def __init__(self, task: str):
        self.task = task
        self.steps: list[PlanStep] = []
        self.total_steps = 0

    def add_step(self, title: str, description: str = "") -> PlanStep:
        step = PlanStep(len(self.steps) + 1, title, description)
        self.steps.append(step)
        self.total_steps = len(self.steps)
        return step

    def to_dict(self) -> dict:
        return {
            "task": self.task,
            "steps": [s.to_dict() for s in self.steps],
            "total_steps": self.total_steps
        }


# =============================================================================
# Planning Agent (T034)
# =============================================================================

class PlanningAgent:
    """Agent that generates execution plans for complex tasks."""

    def __init__(self):
        self.name = "PlanningAgent"

    def generate_plan(self, task: str) -> Plan:
        """Generate a plan for the given task."""
        log_step("thinking", f"[AGENT ANALYZING TASK]\n\"{task}\"\n\nDecomposing into executable steps...")
        step_delay()

        plan = Plan(task)
        return plan


# =============================================================================
# Migration Plan Generator (T035)
# =============================================================================

def generate_migration_plan(agent: PlanningAgent, video_count: int = 100) -> Plan:
    """Generate a 5-step plan for video migration."""
    task = f"Migrate {video_count} YouTube videos to course platform"
    plan = agent.generate_plan(task)

    # Add 5 migration steps
    plan.add_step(
        "Fetch video metadata from YouTube",
        f"Retrieve titles, descriptions, and thumbnails for all {video_count} videos"
    )
    plan.add_step(
        "Download video files",
        f"Download {video_count} videos in highest available quality"
    )
    plan.add_step(
        "Transcode to platform format",
        "Convert videos to HLS format with multiple quality levels"
    )
    plan.add_step(
        "Upload to course platform",
        "Upload transcoded videos with metadata to target platform"
    )
    plan.add_step(
        "Verify and generate report",
        "Validate all uploads and create migration summary report"
    )

    return plan


# =============================================================================
# Output Functions (T036, T037, T039)
# =============================================================================

def output_planning_phase(plan: Plan):
    """Display the planning phase with numbered steps (T036)."""
    output = "[PLANNING PHASE]\n\n"
    output += f"Task: {plan.task}\n\n"
    output += "Generated Plan:\n"

    for step in plan.steps:
        output += f"  {step.number}. {step.title}\n"
        if step.description:
            output += f"     {step.description}\n"

    log_step("planning", output)
    step_delay()


def output_checkpoint(plan: Plan):
    """Display the validation checkpoint (T037)."""
    output = "[CHECKPOINT]\n\n"
    output += f"Plan validation for: {plan.task}\n\n"
    output += f"  Total steps: {plan.total_steps}\n"
    output += f"  Estimated items: 100 videos\n"
    output += f"  Dependencies: All clear\n\n"
    output += "Status: Plan validated and ready for execution"

    log_step("checkpoint", output)
    step_delay()


def get_status_indicator(status: str) -> str:
    """Get visual indicator for step status."""
    indicators = {
        "pending": "⏳",
        "in_progress": "⧗",
        "completed": "✓",
        "failed": "❌"
    }
    return indicators.get(status, "?")


def output_execution_step(step: PlanStep, progress_pct: int):
    """Display execution step with status indicator and progress (T039)."""
    indicator = get_status_indicator(step.status)

    output = f"[STEP {step.number}/{5}] {indicator} {step.title}\n"

    if step.status == "in_progress":
        # Show progress bar
        filled = int(progress_pct / 10)
        bar = "█" * filled + "░" * (10 - filled)
        output += f"  Progress: [{bar}] {progress_pct}%"
    elif step.status == "completed":
        output += f"  Duration: {step.duration}\n"
        output += f"  Status: Complete"
    elif step.status == "pending":
        output += f"  Status: Waiting..."

    log_step("execution", output)


# =============================================================================
# Plan Execution (T038)
# =============================================================================

def execute_plan(plan: Plan):
    """Execute the plan with simulated step execution and progress tracking (T038)."""
    log_step("execution", "[EXECUTION PHASE]\n\nBeginning plan execution...")
    step_delay()

    # Simulated execution times for each step
    step_durations = ["12s", "45s", "38s", "22s", "8s"]

    for i, step in enumerate(plan.steps):
        # Mark step as in progress
        step.status = "in_progress"

        # Simulate progress updates
        for progress in [0, 25, 50, 75, 100]:
            step.progress = progress
            output_execution_step(step, progress)
            step_delay(0.2)

        # Mark step complete
        step.status = "completed"
        step.progress = 100
        step.duration = step_durations[i]
        output_execution_step(step, 100)
        step_delay(0.3)

    # Final summary
    output_final_summary(plan)


def output_final_summary(plan: Plan):
    """Display execution summary."""
    completed = sum(1 for s in plan.steps if s.status == "completed")
    failed = sum(1 for s in plan.steps if s.status == "failed")

    output = "[EXECUTION SUMMARY]\n\n"
    output += f"Task: {plan.task}\n\n"
    output += f"Results:\n"
    output += f"  ✓ Steps completed: {completed}/{plan.total_steps}\n"

    if failed > 0:
        output += f"  ❌ Steps failed: {failed}\n"

    output += f"\nStep Details:\n"
    for step in plan.steps:
        indicator = get_status_indicator(step.status)
        output += f"  {indicator} Step {step.number}: {step.title}"
        if step.duration:
            output += f" ({step.duration})"
        output += "\n"

    if completed == plan.total_steps:
        output += "\n✓ Migration completed successfully!"
    else:
        output += "\n⚠ Migration completed with issues"

    log_step("summary", output)


# =============================================================================
# Main Entry Point (T040)
# =============================================================================

def main():
    """Run the Planning + Execution demo."""
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "="*60)
    print("PLANNING + EXECUTION PATTERN DEMO")
    print("   Content Migration with Plan Generation & Progress")
    print("="*60 + "\n")

    # Create planning agent
    agent = PlanningAgent()

    # Phase 1: Generate plan
    plan = generate_migration_plan(agent, video_count=100)

    # Phase 2: Output planning phase
    output_planning_phase(plan)

    # Phase 3: Validation checkpoint
    output_checkpoint(plan)

    # Phase 4: Execute plan
    execute_plan(plan)

    print("\n" + "="*60)
    print("Demo complete!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
