# Data Model: Agentic AI Design Pattern Demos

| Status | 🟢 Ready |
|--------|----------|

| Version | Date       | Author | Changes           |
|---------|------------|--------|-------------------|
| 1.0.0   | 2025-12-08 | Claude | Initial data model |

## 📦 Overview

This document defines the data structures used across all demo scripts. Since demos are stateless (no persistence), these models represent runtime data shapes for output formatting and tool interactions.

---

## 🔧 Core Entities

### StepOutput

Represents a single unit of structured demo output.

| Field     | Type   | Required | Description                                      |
|-----------|--------|----------|--------------------------------------------------|
| type      | string | ✅       | Step type (thinking, action, observation, etc.)  |
| content   | string | ✅       | Human-readable content for this step             |
| timestamp | float  | ✅       | Unix timestamp when step was emitted             |

**Valid Types**: `thinking`, `action`, `observation`, `response`, `error`, `routing`, `summary`, `planning`, `execution`, `checkpoint`

**Example**:
```json
{
  "type": "thinking",
  "content": "Analyzing user request: 'I want a refund'",
  "timestamp": 1733673600.123
}
```

---

### Tool

Represents a mocked tool available to agents.

| Field       | Type   | Required | Description                              |
|-------------|--------|----------|------------------------------------------|
| name        | string | ✅       | Unique tool identifier (snake_case)      |
| description | string | ✅       | Human-readable purpose description       |
| parameters  | object | ✅       | JSON Schema defining input parameters    |

**Example**:
```json
{
  "name": "refund_processor",
  "description": "Process a customer refund for an order",
  "parameters": {
    "type": "object",
    "properties": {
      "order_id": {"type": "string", "description": "The order ID to refund"},
      "reason": {"type": "string", "description": "Reason for the refund"}
    },
    "required": ["order_id", "reason"]
  }
}
```

---

### ToolCall

Represents an invocation of a tool by an agent.

| Field  | Type   | Required | Description                    |
|--------|--------|----------|--------------------------------|
| tool   | string | ✅       | Name of the tool being called  |
| params | object | ✅       | Parameters passed to the tool  |

**Example**:
```json
{
  "tool": "refund_processor",
  "params": {"order_id": "ORD-12345", "reason": "not as described"}
}
```

---

### ToolResponse

Represents the result returned by a mocked tool.

| Field   | Type   | Required | Description                           |
|---------|--------|----------|---------------------------------------|
| status  | string | ✅       | Result status (success, error)        |
| data    | object | ✅       | Tool-specific response payload        |
| message | string | ❌       | Optional human-readable message       |

**Example**:
```json
{
  "status": "success",
  "data": {
    "refund_id": "REF-12345-1733673600",
    "amount": 99.99,
    "processing_time": "3-5 business days"
  }
}
```

---

## 🤖 Agent Entities

### Agent

Represents an AI agent in the demo.

| Field       | Type     | Required | Description                              |
|-------------|----------|----------|------------------------------------------|
| name        | string   | ✅       | Agent identifier                         |
| role        | string   | ✅       | Agent's purpose/specialty                |
| tools       | Tool[]   | ❌       | Available tools (if tool-using agent)    |
| system_prompt | string | ❌       | Instructions for the agent               |

**Example**:
```json
{
  "name": "CustomerSupportAgent",
  "role": "Handle customer service requests",
  "tools": ["refund_processor", "password_reset"],
  "system_prompt": "You are a helpful customer support agent..."
}
```

---

### AgentMessage

Represents communication between agents (for orchestration pattern).

| Field   | Type   | Required | Description                    |
|---------|--------|----------|--------------------------------|
| from    | string | ✅       | Sending agent name             |
| to      | string | ✅       | Receiving agent name           |
| content | string | ✅       | Message content                |
| type    | string | ✅       | Message type (request, response) |

**Example**:
```json
{
  "from": "Coordinator",
  "to": "InventoryAgent",
  "content": "Check availability for 2x Widget A, 1x Widget B",
  "type": "request"
}
```

---

## 📋 Planning Entities

### Plan

Represents a generated execution plan.

| Field       | Type       | Required | Description                    |
|-------------|------------|----------|--------------------------------|
| task        | string     | ✅       | High-level task description    |
| steps       | PlanStep[] | ✅       | Ordered list of plan steps     |
| total_steps | int        | ✅       | Total number of steps          |

**Example**:
```json
{
  "task": "Migrate 100 YouTube videos to course platform",
  "steps": [...],
  "total_steps": 5
}
```

---

### PlanStep

Represents a single step in an execution plan.

| Field    | Type   | Required | Description                              |
|----------|--------|----------|------------------------------------------|
| number   | int    | ✅       | Step sequence number (1-indexed)         |
| title    | string | ✅       | Brief step description                   |
| status   | string | ✅       | Execution status                         |
| progress | int    | ❌       | Completion percentage (0-100)            |
| duration | string | ❌       | Elapsed time for this step               |

**Valid Status Values**: `pending`, `in_progress`, `completed`, `failed`

**Status Display**:
- `pending` → ⏳
- `in_progress` → ⧗
- `completed` → ✓
- `failed` → ❌

**Example**:
```json
{
  "number": 1,
  "title": "Fetch video metadata from YouTube",
  "status": "completed",
  "progress": 100,
  "duration": "25s"
}
```

---

## 🔀 Orchestration Entities

### OrderRequest

Input for the multi-agent orchestration demo.

| Field    | Type       | Required | Description                    |
|----------|------------|----------|--------------------------------|
| items    | OrderItem[]| ✅       | Items to order                 |
| customer | string     | ✅       | Customer identifier            |

---

### OrderItem

Single item in an order.

| Field    | Type   | Required | Description         |
|----------|--------|----------|---------------------|
| product  | string | ✅       | Product name        |
| quantity | int    | ✅       | Number of units     |

---

### OrchestrationResult

Aggregated result from specialist agents.

| Field     | Type   | Required | Description                    |
|-----------|--------|----------|--------------------------------|
| order_id  | string | ✅       | Generated order identifier     |
| inventory | object | ✅       | Inventory check result         |
| payment   | object | ✅       | Payment processing result      |
| shipping  | object | ✅       | Shipping arrangement result    |
| success   | bool   | ✅       | Overall success status         |

---

## 🔗 Entity Relationships

```text
StepOutput ─── emitted by ──→ Demo Script

Agent ─── uses ──→ Tool[]
Agent ─── produces ──→ ToolCall
ToolCall ─── returns ──→ ToolResponse

Agent ─── sends ──→ AgentMessage ─── to ──→ Agent (orchestration)

Plan ─── contains ──→ PlanStep[]
```

---

## ✅ Data Model Complete

All entities defined for demo implementation. No persistence layer required.
