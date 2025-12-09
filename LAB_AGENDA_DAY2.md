<!--
NOTICE: This document is internal training material.
Do not index or crawl.
-->
<!-- noindex -->
<!-- robots: noindex, nofollow -->

<div align="center">

# 🏛️ CivicNav Lab Agenda - Day 2

> **ISV Vibe Coding Lab** | Azure AI Engineering | Total Duration: 2.5 hours

</div>

---

## 📊 Status

| Metric | Status |
|--------|--------|
| ![Exercises](https://img.shields.io/badge/exercises-8%20total-blue) | Exercise Count |
| ![Duration](https://img.shields.io/badge/duration-2.5%20hours-green) | Total Time |
| ![Difficulty](https://img.shields.io/badge/difficulty-beginner%20to%20advanced-yellow) | Skill Range |
| ![Status](https://img.shields.io/badge/status-ready-brightgreen) | Lab Ready |

---

## 📋 Version History

| Version | Date | Changes | Status |
|---------|------|---------|--------|
| 1.0.0 | 2024-12-09 | ✨ Initial agenda aligned with CivicNav exercises | ✅ Current |

---

## 🎯 Overview

Build and explore **CivicNav** - an AI-powered city services Q&A assistant demonstrating:

| Feature | Description |
|---------|-------------|
| 🤖 **Agentic RAG** | QueryAgent → RetrieveAgent → AnswerAgent pipeline |
| 📝 **Spec-Driven Dev** | SPEC.md guiding AI code generation |
| 🔄 **Multi-LLM** | OpenAI API, Ollama, Azure OpenAI |
| ☁️ **Azure Integration** | AI Search, Container Apps, MCP Server |
| 🚀 **One-Command Deploy** | `azd up` |

---

## 📅 Agenda

| Time | Segment | Activities & Focus | Exercises |
|------|---------|-------------------|-----------|
| ⏱️ **0 – 15** | 🎤 **Introduction & Objectives** | Welcome everyone. Introduce **CivicNav** - an AI-powered city services Q&A assistant we'll explore together. Frame the lab: "From AI chaos to controlled engineering." Demo vibe coding pitfalls (unstructured prompting) vs. our spec-driven approach with the 3-agent architecture (QueryAgent → RetrieveAgent → AnswerAgent). Present the toolchain: **GitHub Copilot + Agent Mode**, **Azure MCP Server**, **Azure AI Search**, **OpenAI/Ollama**, and **azd deployment**. Verify environments: VS Code open, project cloned, Python venv active. | — |
| ⏱️ **15 – 35** | 🛠️ **Foundation: Setup & Concepts** | Guide participants through **Exercise 0** (Environment Setup): clone repo, install dependencies, run `uvicorn`, verify health endpoint and UI at localhost:8000. Then cover **Exercise 1** (Understanding Agents & RAG): explain the 3-agent pipeline, RAG concepts (retrieval before generation), hybrid search (keyword + vector), and why this architecture beats monolithic prompts. Live demo: ask CivicNav "When is trash pickup?" and trace the answer through QueryAgent → RetrieveAgent → AnswerAgent. | Ex 0, Ex 1 |
| ⏱️ **35 – 55** | 🔌 **Azure MCP Server Setup** | **Exercise 2**: Configure VS Code's Agent Mode with Azure MCP Server. Participants install the MCP extension, configure `mcp.json`, authenticate with Azure CLI. Demo Copilot querying Azure resources directly ("What AI Search indexes exist?"). This unlocks AI-assisted Azure resource management for the rest of the lab. | Ex 2 |
| ⏱️ **55 – 75** | 📝 **Spec-Driven Development** | **Exercise 3**: Introduce SPEC.md and the constitution.md - how specifications guide AI code generation. Participants explore the existing spec, then use Copilot (with spec context) to generate a new feature stub (e.g., add a "feedback" endpoint). Compare spec-guided output vs. blind prompting. Emphasize: "What & why before how." | Ex 3 |
| ☕ **75 – 90** | 🧘 **Break & Q&A** | 15-minute break. Informal Q&A. Address any setup issues. Participants can explore the codebase or chat UI. | — |
| ⏱️ **90 – 120** | 🔍 **Build RAG Pipeline** | **Exercise 4**: Deep dive into the search layer. Explore `DemoSearchTool` (local) vs. `SearchTool` (Azure AI Search). Participants test the `/api/search` endpoint with different queries, analyze relevance scores, and examine how RetrieveAgent orchestrates hybrid search. Hands-on: modify search parameters (top_k, category filters) and observe result changes. | Ex 4 |
| ⏱️ **120 – 145** | 🔗 **Agent Orchestration** | **Exercise 5**: Master the pipeline orchestration. Trace a query end-to-end through all 3 agents. Examine `BaseAgent` abstract class, understand data flow (QueryResult → SearchResults → Answer with citations). Analyze latency tracking. Hands-on: add logging to an agent and observe the chain-of-thought reasoning. This is the "agentic" core of the lab. | Ex 5 |
| ⏱️ **145 – 165** | 🚀 **Deployment & MCP Server** | **Exercise 6** (Deploy): Demo `azd up` one-command deployment to Azure Container Apps. Show azure.yaml and infra/ Bicep templates. Explain environment management (dev/staging/prod). **Exercise 7** (optional/advanced): Show how CivicNav exposes itself as an MCP server - turning your app into a tool that AI assistants can call. Participants who finish early can configure their VS Code to use CivicNav as an MCP tool. | Ex 6, Ex 7 |
| ⏱️ **165 – 180** | 🎬 **Wrap-Up & Q&A** | Summarize outcomes: We explored a production-ready agentic RAG app with spec-driven patterns, multi-LLM support (OpenAI/Ollama/Azure), and one-command deployment. Compare to unstructured approaches: our codebase is modular, documented, and maintainable. Invite participants to share their running apps or insights. Provide resources: exercise docs, SPEC.md, Azure AI docs. Key takeaway: AI-assisted development with engineering discipline = rapid innovation without chaos. | — |

---

## 🏗️ Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    🖥️ User Interface                            │
│                    (Chat UI / MCP Tools)                        │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   ⚡ FastAPI Application                        │
│                   POST /api/query endpoint                      │
└─────────────────────────────┬───────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  🔍 QueryAgent  │  │ 📚 RetrieveAgent│  │ 💬 AnswerAgent  │
│                 │  │                 │  │                 │
│ • Intent class. │  │ • Hybrid search │  │ • Synthesize    │
│ • Entity extract│  │ • Vector + KW   │  │ • Citations     │
│                 │  │ • Semantic rank │  │                 │
└────────┬────────┘  └────────┬────────┘  └────────┬────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                      ☁️ Azure Services                          │
│  ┌─────────────────┐              ┌─────────────────┐           │
│  │ 🧠 Azure OpenAI │              │ 🔎 Azure AI     │           │
│  │  • gpt-4o       │              │    Search       │           │
│  │  • embeddings   │              │  • Vector index │           │
│  └─────────────────┘              └─────────────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📚 Exercise Summary

| # | Exercise | Duration | Difficulty | Status |
|---|----------|----------|------------|--------|
| 0 | 🛠️ Environment Setup | 20 min | ⭐ Beginner | ✅ Ready |
| 1 | 🧠 Understanding AI Agents & RAG | 25 min | ⭐ Beginner | ✅ Ready |
| 2 | 🔌 Azure MCP Server Setup | 20 min | ⭐ Beginner | ✅ Ready |
| 3 | 📝 Spec-Driven Development | 20 min | ⭐ Beginner | ✅ Ready |
| 4 | 🔍 Build RAG Pipeline | 45 min | ⭐⭐ Intermediate | ✅ Ready |
| 5 | 🔗 Agent Orchestration | 40 min | ⭐⭐⭐ Advanced | ✅ Ready |
| 6 | 🚀 Deploy with azd | 35 min | ⭐⭐ Intermediate | ✅ Ready |
| 7 | 🔧 Expose as MCP Server | 45 min | ⭐⭐⭐ Advanced | ✅ Ready |

---

## 🔄 Key Changes from Original Plan

| Original | Updated | Rationale |
|----------|---------|-----------|
| 🏗️ "Build from scratch" approach | 🔍 Explore pre-built CivicNav | App is already complete; focus on understanding & extending |
| 💬 Generic "city info chatbot" | 🏛️ Specific CivicNav with 3-agent pipeline | Concrete architecture to learn from |
| 🛠️ "Spec Kit CLI" (`specify init`) | 📝 SPEC.md + constitution.md | Using actual spec files in the project |
| 🔧 Flask/FastAPI from scratch | ⚡ FastAPI already running (Exercise 0) | Lab explores existing code, not building from zero |
| 📦 "Agent Framework SDK" generic | 🤖 BaseAgent + QueryAgent/RetrieveAgent/AnswerAgent | Actual implementation in the codebase |
| ❓ Vague "AI integration" | 🔍 RAG pipeline with DemoSearchTool/Azure AI Search | Specific hybrid search implementation |
| 🐳 Docker/Azure Functions | 🚀 `azd up` to Container Apps | Modern Azure Developer CLI approach |
| ❌ No MCP coverage | 🔌 Exercises 2 & 7 cover MCP as consumer and producer | MCP is a major differentiator |
| ⏱️ ~2 hour coding | ⏱️ ~2.5 hours exploring + hands-on exercises | More realistic for exploration lab |

---

## ✅ Materials Checklist

- [ ] 📁 CivicNav repo cloned and verified on presenter machine
- [ ] 💬 Demo queries prepared: "When is trash pickup?", "What permits do I need?", "Park hours"
- [ ] ☁️ Azure resources provisioned (AI Search, OpenAI) or demo mode enabled
- [ ] 🔌 VS Code with Copilot + MCP extension configured
- [ ] 📄 Exercise documents printed or accessible (docs/exercises/)
- [ ] 🎥 Backup: screenshots/videos if live demo fails

---

## 💬 Demo Queries

Use these queries during the live demo:

| Query | Expected Behavior | Category |
|-------|-------------------|----------|
| 🗑️ "When is trash pickup?" | Returns schedule info with citations | Utilities |
| 🏗️ "What permits do I need for a fence?" | Shows permit requirements | Permits |
| 🌳 "Park hours" | Returns park operating hours | Recreation |
| 🕳️ "How do I report a pothole?" | Service request information | Infrastructure |

---

## 🔧 Troubleshooting Quick Reference

| ❌ Issue | ✅ Solution |
|----------|------------|
| `DefaultAzureCredential` fails | Run `az login` |
| Search index not found | Use demo mode or run indexer |
| OpenAI quota exceeded | Switch to Ollama or mock mode |
| MCP not connecting | Check `mcp.json` configuration |
| Port 8000 in use | Kill existing process or use different port |

---

## 📚 Resources

| Resource | Link |
|----------|------|
| 📖 CivicNav Exercise Docs | [./docs/exercises/](./docs/exercises/) |
| 📖 Azure OpenAI Documentation | [learn.microsoft.com](https://learn.microsoft.com/azure/cognitive-services/openai/) |
| 📖 Azure AI Search Documentation | [learn.microsoft.com](https://learn.microsoft.com/azure/search/) |
| 📖 MCP Specification | [modelcontextprotocol.io](https://modelcontextprotocol.io/) |
| 📖 Azure Developer CLI | [learn.microsoft.com](https://learn.microsoft.com/azure/developer/azure-developer-cli/) |

---

<div align="center">

**Made with ❤️ for Azure AI Engineers**

**Version**: 1.0.0 | **Last Updated**: 2024-12-09

</div>
