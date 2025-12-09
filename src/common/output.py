"""Structured output utilities for Agentic AI Design Pattern Demos."""

import json
import time
from typing import Optional

# Step type constants (per Constitution II. Structured Output Protocol)
STEP_TYPES = {
    "thinking": "THINKING",
    "action": "ACTION",
    "observation": "OBSERVATION",
    "response": "RESPONSE",
    "error": "ERROR",
    "routing": "ROUTING",
    "summary": "SUMMARY",
    "planning": "PLANNING",
    "execution": "EXECUTION",
    "checkpoint": "CHECKPOINT",
}

# Default delay between steps for readability (0.3-0.5s per Constitution)
DEFAULT_DELAY = 0.4


def log_step(step_type: str, content: str, metadata: Optional[dict] = None) -> None:
    """
    Print structured output for Streamlit parsing.

    Emits both JSON-parseable output and human-readable formatted text.
    Per Constitution II: JSON output MUST precede human-readable output.

    Args:
        step_type: One of the valid STEP_TYPES keys
        content: Human-readable content for this step
        metadata: Optional additional data (tool_name, params, progress, etc.)
    """
    # Build JSON output
    output = {
        "type": step_type,
        "content": content,
        "timestamp": time.time(),
    }
    if metadata:
        output["metadata"] = metadata

    # JSON output first (for Streamlit parsing)
    print(json.dumps(output))

    # Human-readable output second
    type_label = STEP_TYPES.get(step_type, step_type.upper())
    print(f"\n[{type_label}]\n{content}\n")


def step_delay(seconds: float = DEFAULT_DELAY) -> None:
    """
    Add a delay between steps for readability in recordings.

    Per Constitution II: Include small delays (0.3-0.5s) between steps.

    Args:
        seconds: Delay duration (default 0.4s)
    """
    time.sleep(seconds)


def format_tool_call(tool_name: str, params: dict) -> str:
    """Format a tool call for display."""
    params_str = json.dumps(params, indent=2)
    return f"Function: {tool_name}\nParams: {params_str}"


def format_tool_response(response: dict) -> str:
    """Format a tool response for display."""
    return json.dumps(response, indent=2)
