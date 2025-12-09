"""LLM provider auto-detection and mock fallback for demos."""

import requests
from typing import Optional, Dict, Any, List
from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """Base class for LLM providers."""

    @abstractmethod
    def generate(self, prompt: str, system: str = "") -> str:
        """Generate a response from the LLM."""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if this provider is available."""
        pass


class OllamaProvider(BaseLLMProvider):
    """Ollama local LLM provider (localhost:11434)."""

    def __init__(self, model: str = "llama3.2"):
        self.base_url = "http://localhost:11434"
        self.model = model

    def is_available(self) -> bool:
        """Check if Ollama is running."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=1)
            return response.ok
        except Exception:
            return False

    def generate(self, prompt: str, system: str = "") -> str:
        """Generate response using Ollama API."""
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "system": system,
                    "stream": False,
                },
                timeout=30,
            )
            if response.ok:
                return response.json().get("response", "")
        except Exception:
            pass
        return ""


class LMStudioProvider(BaseLLMProvider):
    """LM Studio local LLM provider (localhost:1234)."""

    def __init__(self):
        self.base_url = "http://localhost:1234/v1"

    def is_available(self) -> bool:
        """Check if LM Studio is running."""
        try:
            response = requests.get(f"{self.base_url}/models", timeout=1)
            return response.ok
        except Exception:
            return False

    def generate(self, prompt: str, system: str = "") -> str:
        """Generate response using OpenAI-compatible API."""
        try:
            messages = []
            if system:
                messages.append({"role": "system", "content": system})
            messages.append({"role": "user", "content": prompt})

            response = requests.post(
                f"{self.base_url}/chat/completions",
                json={"messages": messages, "temperature": 0.7},
                timeout=30,
            )
            if response.ok:
                return response.json()["choices"][0]["message"]["content"]
        except Exception:
            pass
        return ""


class MockLLMProvider(BaseLLMProvider):
    """Mock LLM provider with scripted responses for demos."""

    def __init__(self):
        self.response_index = 0
        self.scripted_responses: List[str] = []

    def is_available(self) -> bool:
        """Mock provider is always available."""
        return True

    def set_responses(self, responses: List[str]) -> None:
        """Set scripted responses for the demo."""
        self.scripted_responses = responses
        self.response_index = 0

    def generate(self, prompt: str, system: str = "") -> str:
        """Return next scripted response."""
        if not self.scripted_responses:
            return "Mock response: No scripted responses configured."

        response = self.scripted_responses[self.response_index % len(self.scripted_responses)]
        self.response_index += 1
        return response


def get_llm_provider() -> BaseLLMProvider:
    """
    Auto-detect available LLM provider.

    Checks in order:
    1. Ollama (localhost:11434)
    2. LM Studio (localhost:1234)
    3. Falls back to MockLLMProvider

    Returns:
        Available LLM provider instance
    """
    # Try Ollama first
    ollama = OllamaProvider()
    if ollama.is_available():
        print("🤖 Using Ollama for LLM responses")
        return ollama

    # Try LM Studio
    lm_studio = LMStudioProvider()
    if lm_studio.is_available():
        print("🤖 Using LM Studio for LLM responses")
        return lm_studio

    # Fall back to mock
    print("🤖 Using mock responses (no local LLM detected)")
    return MockLLMProvider()
