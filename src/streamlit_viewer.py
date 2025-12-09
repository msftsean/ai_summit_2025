"""
Streamlit Viewer for Agentic Pattern Demos

Renders demo JSON output as formatted cards with visual styling
per step type and animations for screen recording.

Usage:
    streamlit run src/streamlit_viewer.py

    Then upload a JSON output file or paste JSON content.
"""

import streamlit as st
import json
import os
import time
from pathlib import Path

# =============================================================================
# Page Configuration (T041)
# =============================================================================

st.set_page_config(
    page_title="Agentic Pattern Demo Viewer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# Card Styling Mapping (T043)
# =============================================================================

STEP_STYLES = {
    "thinking": {
        "icon": "🧠",
        "color": "#3498db",  # Blue
        "bg_color": "#ebf5fb",
        "label": "Thinking"
    },
    "action": {
        "icon": "⚡",
        "color": "#e67e22",  # Orange
        "bg_color": "#fef5e7",
        "label": "Action"
    },
    "observation": {
        "icon": "👁️",
        "color": "#27ae60",  # Green
        "bg_color": "#e9f7ef",
        "label": "Observation"
    },
    "response": {
        "icon": "💬",
        "color": "#9b59b6",  # Purple
        "bg_color": "#f5eef8",
        "label": "Response"
    },
    "error": {
        "icon": "❌",
        "color": "#e74c3c",  # Red
        "bg_color": "#fdedec",
        "label": "Error"
    },
    "routing": {
        "icon": "🔀",
        "color": "#1abc9c",  # Teal
        "bg_color": "#e8f8f5",
        "label": "Routing"
    },
    "summary": {
        "icon": "📊",
        "color": "#34495e",  # Dark gray
        "bg_color": "#f4f6f6",
        "label": "Summary"
    },
    "planning": {
        "icon": "📋",
        "color": "#2980b9",  # Dark blue
        "bg_color": "#d4e6f1",
        "label": "Planning"
    },
    "execution": {
        "icon": "▶️",
        "color": "#16a085",  # Dark teal
        "bg_color": "#d5f5e3",
        "label": "Execution"
    },
    "checkpoint": {
        "icon": "✅",
        "color": "#f39c12",  # Yellow/gold
        "bg_color": "#fef9e7",
        "label": "Checkpoint"
    }
}

DEFAULT_STYLE = {
    "icon": "📝",
    "color": "#7f8c8d",
    "bg_color": "#f8f9f9",
    "label": "Step"
}

# =============================================================================
# CSS Animations (T047)
# =============================================================================

CUSTOM_CSS = """
<style>
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.step-card {
    animation: fadeIn 0.5s ease-out;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    border-left: 4px solid;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.step-header {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    font-weight: bold;
    font-size: 1.1em;
}

.step-icon {
    font-size: 1.3em;
    margin-right: 10px;
}

.step-content {
    white-space: pre-wrap;
    font-family: 'Monaco', 'Menlo', monospace;
    font-size: 0.95em;
    line-height: 1.5;
}

.step-timestamp {
    font-size: 0.8em;
    color: #888;
    margin-top: 8px;
}

.viewer-header {
    text-align: center;
    padding: 20px 0;
    border-bottom: 2px solid #eee;
    margin-bottom: 20px;
}

.stats-container {
    display: flex;
    gap: 20px;
    justify-content: center;
    margin: 15px 0;
}

.stat-box {
    background: #f8f9fa;
    padding: 10px 20px;
    border-radius: 8px;
    text-align: center;
}

.live-indicator {
    display: inline-block;
    width: 10px;
    height: 10px;
    background: #27ae60;
    border-radius: 50%;
    margin-right: 8px;
    animation: pulse 1s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}
</style>
"""

# =============================================================================
# JSON Parser (T042)
# =============================================================================

def parse_json_lines(content: str) -> list[dict]:
    """Parse JSON lines from content, handling both single JSON and line-delimited."""
    steps = []

    # Try parsing as single JSON array first
    try:
        data = json.loads(content)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict):
            return [data]
    except json.JSONDecodeError:
        pass

    # Parse as line-delimited JSON
    for line in content.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        try:
            step = json.loads(line)
            if isinstance(step, dict):
                steps.append(step)
        except json.JSONDecodeError:
            # Skip non-JSON lines (human-readable output)
            continue

    return steps


# =============================================================================
# Card Renderer (T044)
# =============================================================================

def render_step_card(step: dict, index: int):
    """Render a styled card for a step."""
    step_type = step.get("type", "unknown")
    content = step.get("content", "")
    timestamp = step.get("timestamp", None)

    style = STEP_STYLES.get(step_type, DEFAULT_STYLE)

    # Build card HTML
    card_html = f"""
    <div class="step-card" style="background-color: {style['bg_color']}; border-left-color: {style['color']};">
        <div class="step-header" style="color: {style['color']};">
            <span class="step-icon">{style['icon']}</span>
            <span>{style['label']} #{index + 1}</span>
        </div>
        <div class="step-content">{content}</div>
    """

    if timestamp:
        import datetime
        try:
            dt = datetime.datetime.fromtimestamp(timestamp)
            card_html += f'<div class="step-timestamp">⏱️ {dt.strftime("%H:%M:%S.%f")[:-3]}</div>'
        except (ValueError, OSError):
            pass

    card_html += "</div>"

    st.markdown(card_html, unsafe_allow_html=True)


# =============================================================================
# Live File Watcher
# =============================================================================

def get_watch_file_path():
    """Get the default watch file path."""
    return Path("output/live_demo.txt")


def read_live_file(file_path: Path) -> str:
    """Read content from live file if it exists."""
    if file_path.exists():
        try:
            return file_path.read_text(encoding='utf-8')
        except Exception:
            return ""
    return ""


# =============================================================================
# Main Application (T041, T045, T046, T048)
# =============================================================================

def main():
    """Main Streamlit application."""
    # Inject custom CSS
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    # Header
    st.markdown("""
    <div class="viewer-header">
        <h1>🤖 Agentic Pattern Demo Viewer</h1>
        <p>Visualize structured output from agentic AI demos</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar
    st.sidebar.header("📁 Load Demo Output")

    input_method = st.sidebar.radio(
        "Input Method",
        ["Upload File", "Paste JSON", "Sample Data", "Live Watch"]
    )

    steps = []
    live_refresh_rate = None  # Will be set in Live Watch mode

    if input_method == "Upload File":
        # File upload (T045)
        uploaded_file = st.sidebar.file_uploader(
            "Upload JSON output file",
            type=["json", "jsonl", "txt"]
        )
        if uploaded_file:
            content = uploaded_file.read().decode("utf-8")
            steps = parse_json_lines(content)

    elif input_method == "Paste JSON":
        # Text input
        json_input = st.sidebar.text_area(
            "Paste JSON output",
            height=200,
            placeholder='{"type": "thinking", "content": "...", "timestamp": 123}'
        )
        if json_input:
            steps = parse_json_lines(json_input)

    elif input_method == "Live Watch":
        # Live file watching mode
        st.sidebar.markdown("---")
        st.sidebar.markdown('<span class="live-indicator"></span> **Live Mode**', unsafe_allow_html=True)

        # Get project root (parent of src/) for absolute path
        project_root = Path(__file__).parent.parent.resolve()
        default_watch_file = str(project_root / "output" / "live_demo.txt")

        watch_file = st.sidebar.text_input(
            "Watch file path",
            value=default_watch_file,
            help="Run demo with: python src/agent_executor.py > output/live_demo.txt 2>&1"
        )

        live_refresh_rate = st.sidebar.slider("Refresh rate (seconds)", 0.5, 5.0, 1.0, 0.5)

        st.sidebar.markdown("---")
        st.sidebar.markdown("**Instructions:**")
        st.sidebar.code(f"python src/agent_executor.py > {watch_file} 2>&1", language="bash")

        # Create output directory if needed
        watch_path = Path(watch_file)
        if watch_path.parent.name and not watch_path.parent.exists():
            try:
                watch_path.parent.mkdir(parents=True, exist_ok=True)
                st.sidebar.success(f"Created {watch_path.parent}/")
            except Exception:
                pass

        # Read and parse the file
        if watch_path.exists():
            content = read_live_file(watch_path)
            steps = parse_json_lines(content)

            # Debug info
            st.sidebar.success(f"File: {len(content)} chars, {len(steps)} steps found")

            # Show file info
            mod_time = os.path.getmtime(watch_path)
            import datetime
            mod_dt = datetime.datetime.fromtimestamp(mod_time)
            st.sidebar.info(f"Last updated: {mod_dt.strftime('%H:%M:%S')}")

            # Clear file button
            if st.sidebar.button("Clear watch file"):
                watch_path.write_text("")
                st.rerun()
        else:
            st.sidebar.warning(f"Waiting for {watch_file}...")

    else:
        # Sample data
        if st.sidebar.button("Load Sample Data"):
            steps = [
                {"type": "thinking", "content": "[AGENT ANALYZING REQUEST]\nUser wants a refund for order #12345", "timestamp": 1733673600.0},
                {"type": "action", "content": "[TOOL CALL: refund_processor]\nParameters: {\"order_id\": \"12345\", \"reason\": \"not as described\"}", "timestamp": 1733673601.0},
                {"type": "observation", "content": "[TOOL RESPONSE]\nRefund approved: $99.99 will be credited in 3-5 days", "timestamp": 1733673602.0},
                {"type": "response", "content": "[AGENT OUTPUT]\nI've processed your refund for order #12345. You'll receive $99.99 back within 3-5 business days.", "timestamp": 1733673603.0},
                {"type": "routing", "content": "[COORDINATOR ROUTING]\n-> Routing to InventoryAgent", "timestamp": 1733673604.0},
                {"type": "planning", "content": "[PLANNING PHASE]\n1. Fetch metadata\n2. Download videos\n3. Transcode\n4. Upload\n5. Verify", "timestamp": 1733673605.0},
                {"type": "execution", "content": "[STEP 1/5] ✓ Fetch metadata\nProgress: [██████████] 100%", "timestamp": 1733673606.0},
                {"type": "checkpoint", "content": "[CHECKPOINT]\nPlan validated. Ready for execution.", "timestamp": 1733673607.0},
                {"type": "summary", "content": "[SUMMARY]\n✓ All steps completed successfully\n✓ 100 videos migrated", "timestamp": 1733673608.0},
            ]

    # Display steps
    if steps:
        # Statistics
        st.markdown(f"""
        <div class="stats-container">
            <div class="stat-box">
                <strong>{len(steps)}</strong><br/>
                <small>Total Steps</small>
            </div>
            <div class="stat-box">
                <strong>{len(set(s.get('type', 'unknown') for s in steps))}</strong><br/>
                <small>Step Types</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Filter by type (only show in non-live modes to avoid rerun conflicts)
        if input_method != "Live Watch":
            st.sidebar.markdown("---")
            st.sidebar.header("🔍 Filter")

            all_types = list(set(s.get("type", "unknown") for s in steps))
            selected_types = st.sidebar.multiselect(
                "Show step types",
                options=all_types,
                default=all_types
            )
        else:
            # In Live Watch mode, show all types
            selected_types = [s.get("type", "unknown") for s in steps]

        # Render filtered cards
        st.markdown("---")

        for i, step in enumerate(steps):
            if step.get("type", "unknown") in selected_types:
                render_step_card(step, i)

    else:
        st.info("👆 Use the sidebar to load demo output")

        # Show step type legend
        st.markdown("### Step Type Legend")
        cols = st.columns(5)
        for i, (step_type, style) in enumerate(STEP_STYLES.items()):
            with cols[i % 5]:
                st.markdown(f"{style['icon']} **{style['label']}**")

    # Auto-refresh for Live Watch mode (AFTER display)
    if input_method == "Live Watch" and live_refresh_rate is not None:
        time.sleep(live_refresh_rate)
        st.rerun()


if __name__ == "__main__":
    main()
