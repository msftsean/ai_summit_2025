"""
ReAct Loop Pattern Demo

Demonstrates a research agent that shows the think→action→observation cycle
for investigating AI frameworks. Shows iterative reasoning and refinement.

Pattern: ReAct (Reasoning + Acting)
"""

import json
import sys
sys.path.insert(0, '.')

from common.output import log_step, step_delay

# =============================================================================
# Tool Definition (T018)
# =============================================================================

SEARCH_TOOL = {
    "name": "search",
    "description": "Search the web for information on a topic",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query"
            }
        },
        "required": ["query"]
    }
}


# =============================================================================
# Mock Search Implementation (T019)
# =============================================================================

# Staged search results for AI frameworks research
MOCK_SEARCH_RESULTS = {
    "latest AI frameworks 2025": {
        "results": [
            "Claude (Anthropic) - Advanced reasoning and coding capabilities",
            "GPT-4 Turbo (OpenAI) - Multimodal with vision and code",
            "Gemini (Google) - Multimodal with long context windows",
            "Llama 3 (Meta) - Open-source large language model",
            "Mistral (Mistral AI) - Efficient open-weight models"
        ],
        "summary": "Top AI frameworks in 2025 include Claude, GPT-4, Gemini, Llama 3, and Mistral."
    },
    "Claude vs GPT-4 capabilities": {
        "results": [
            "Claude excels at nuanced reasoning and following complex instructions",
            "GPT-4 has strong multimodal capabilities including vision",
            "Claude has larger context windows (200K tokens)",
            "GPT-4 Turbo offers faster inference and lower costs",
            "Both support function calling and tool use"
        ],
        "summary": "Claude focuses on reasoning depth; GPT-4 emphasizes multimodal capabilities."
    },
    "open source AI frameworks": {
        "results": [
            "Llama 3 - Meta's latest open-source model, competitive with GPT-4",
            "Mistral 8x7B - Mixture of experts architecture, very efficient",
            "Falcon - Technology Innovation Institute's open model",
            "Qwen - Alibaba's multilingual open model",
            "Phi-3 - Microsoft's small but capable open model"
        ],
        "summary": "Open-source options include Llama 3, Mistral, Falcon, Qwen, and Phi-3."
    },
    "AI framework use cases": {
        "results": [
            "Code generation and assistance - All major frameworks support this",
            "Document analysis - Claude and GPT-4 excel here",
            "Creative writing - Claude known for nuanced output",
            "Data analysis - GPT-4 with Code Interpreter",
            "Agents and automation - All frameworks support tool use"
        ],
        "summary": "Common use cases: coding, document analysis, creative writing, data analysis, agents."
    }
}


def mock_search(query: str) -> dict:
    """Return staged search results based on query."""
    query_lower = query.lower()

    # Find best matching result
    for key, result in MOCK_SEARCH_RESULTS.items():
        if any(word in query_lower for word in key.split()):
            return {
                "status": "success",
                "query": query,
                "result_count": len(result["results"]),
                "results": result["results"],
                "summary": result["summary"]
            }

    # Default response
    return {
        "status": "success",
        "query": query,
        "result_count": 3,
        "results": [
            f"General information about {query}",
            "Related documentation and guides",
            "Community discussions and tutorials"
        ],
        "summary": f"Found general information about {query}."
    }


# =============================================================================
# ReAct Agent Implementation (T020)
# =============================================================================

class ReActAgent:
    """Research agent using think→action→observation cycle."""

    def __init__(self):
        self.observations = []
        self.turn_count = 0

    def think(self, context: str) -> str:
        """Generate a thought based on current context."""
        if self.turn_count == 0:
            return f"I need to research {context}. Let me start with a broad search to understand the landscape."
        elif self.turn_count == 1:
            return "I got some high-level information. Let me dig deeper into specific comparisons."
        elif self.turn_count == 2:
            return "I should also look at open-source alternatives for a complete picture."
        else:
            return "I have enough information to synthesize a comprehensive answer."

    def decide_action(self) -> tuple:
        """Decide what action to take based on turn count."""
        actions = [
            ("search", {"query": "latest AI frameworks 2025"}),
            ("search", {"query": "Claude vs GPT-4 capabilities"}),
            ("search", {"query": "open source AI frameworks"}),
            (None, None)  # No more actions needed
        ]
        return actions[min(self.turn_count, len(actions) - 1)]

    def execute_action(self, action: str, params: dict) -> dict:
        """Execute the chosen action."""
        if action == "search":
            return mock_search(params["query"])
        return {"status": "error", "message": f"Unknown action: {action}"}

    def run_turn(self, context: str) -> bool:
        """
        Run one ReAct turn. Returns False when done.
        """
        self.turn_count += 1

        # Output turn header
        print(f"\n{'─'*50}")

        # THOUGHT
        thought = self.think(context)
        log_step("thinking", f"Turn {self.turn_count} Thought:\n{thought}",
                metadata={"turn_number": self.turn_count})
        step_delay()

        # ACTION
        action, params = self.decide_action()
        if action is None:
            return False  # No more actions needed

        action_str = f"{action}(\"{params.get('query', '')}\")"
        log_step("action", f"Action: {action_str}",
                metadata={"tool_name": action, "tool_params": params})
        step_delay()

        # OBSERVATION
        result = self.execute_action(action, params)
        self.observations.append(result)

        obs_text = f"Found {result['result_count']} results:\n"
        for i, r in enumerate(result['results'][:3], 1):
            obs_text += f"  {i}. {r}\n"
        obs_text += f"\nSummary: {result['summary']}"

        log_step("observation", obs_text)
        step_delay()

        return True  # Continue to next turn


# =============================================================================
# Demo Functions (T021, T022, T023)
# =============================================================================

def run_react_turn(agent: ReActAgent, context: str) -> bool:
    """Run a single ReAct turn with formatted output."""
    return agent.run_turn(context)


def research_ai_frameworks():
    """Run the AI frameworks research with 3-4 ReAct turns."""
    topic = "latest AI frameworks in 2025"

    print("\n" + "="*60)
    print(f"🔍 RESEARCH TOPIC: {topic}")
    print("="*60)

    agent = ReActAgent()

    # Run 3-4 ReAct turns
    max_turns = 4
    for _ in range(max_turns):
        continue_loop = run_react_turn(agent, topic)
        if not continue_loop:
            break

    # Synthesize final answer
    print(f"\n{'─'*50}")
    final_answer = synthesize_final_answer(agent.observations)
    log_step("response", f"[FINAL ANSWER]\n{final_answer}")

    return final_answer


def synthesize_final_answer(observations: list) -> str:
    """Synthesize observations into a final answer (T023)."""
    answer = """Based on my research, here are the latest AI frameworks in 2025:

**Proprietary Models:**
• Claude (Anthropic) - Known for nuanced reasoning, 200K context window
• GPT-4 Turbo (OpenAI) - Multimodal with vision, fast inference
• Gemini (Google) - Long context, multimodal capabilities

**Open Source Options:**
• Llama 3 (Meta) - Competitive with GPT-4, fully open
• Mistral 8x7B - Efficient mixture-of-experts architecture
• Phi-3 (Microsoft) - Small but highly capable

**Key Trends:**
1. Larger context windows (up to 200K+ tokens)
2. Multimodal capabilities (text, vision, code)
3. Tool use and function calling support
4. Open-source alternatives closing the gap

**Recommendation:** Choose based on your needs:
• Reasoning tasks → Claude
• Multimodal → GPT-4 or Gemini
• Open-source → Llama 3 or Mistral"""

    return answer


# =============================================================================
# Main Entry Point (T024)
# =============================================================================

def main():
    """Run the ReAct Loop demo."""
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "="*60)
    print("REACT LOOP PATTERN DEMO")
    print("   Research Agent with Think->Action->Observation Cycle")
    print("="*60)

    research_ai_frameworks()

    print("\n" + "="*60)
    print("Demo complete!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
