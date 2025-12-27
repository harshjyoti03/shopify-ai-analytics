# Shopify AI Analytics Agent

An agent-driven analytics system that converts natural language business questions into actionable Shopify insights using **ShopifyQL-style reasoning**.

This project emphasizes **reasoning depth, explainability, and analytics design** over production-level integrations.

---

## 🧩 System Overview

The system is split into two main services:

1. **Ruby on Rails API**  
   - Accepts user questions
   - Acts as the orchestration layer
   - Designed to handle Shopify OAuth in production

2. **Python AI Service (Agent)**  
   - Built using **FastAPI**
   - Interprets questions
   - Generates analytics logic
   - Produces business-friendly insights

---

## 2️⃣ Python AI Service (Agent)

### Built With
- **Python**
- **FastAPI**

### Responsibilities
- Understand user intent
- Decide which analytics data is required
- Generate ShopifyQL-style queries
- Compute insights using mock data
- Convert technical metrics into business language

---

## 🤖 Agent Workflow

The AI service follows an **agentic reasoning flow**:

### 1. Understand Intent
Identify whether the question relates to:
- Inventory
- Sales
- Customers

### 2. Plan
- Select the appropriate dataset
- Choose time window and metrics

### 3. Generate ShopifyQL
- Build syntactically correct analytics queries
- Use correct datasets and aggregations

### 4. Execute (Mocked)
- Use mock Shopify analytics data
- Simulate real query execution

### 5. Explain Results
- Translate numerical outputs into clear business advice

---

## 📊 Example Output

```json
{
  "answer": "Based on the last 30 days, you sell around 10 units per day. You should reorder at least 70 units to avoid stockouts next week.",
  "confidence": "medium"
}
```

## 🔐 Shopify OAuth Status

### Status: 
Designed and Mocked (Intentionally not fully implemented)

### Reasoning
- The assignment emphasizes reasoning depth and analytics design
- Shopify OAuth is largely boilerplate and well-documented
- Focus was placed on:
    - Agent workflows
    - ShopifyQL reasoning
    - Insight generation

### Planned Production Flow
- Shopify OAuth handled entirely in Rails
- Access tokens stored securely
- Tokens passed to the Python service for analytics execution

This architecture is clearly documented and easily extendable.


## ShopifyQL Understanding

The system dynamically generates ShopifyQL-style queries such as:

```sql
FROM orders
SHOW sum(quantity) AS total_units_sold
GROUP BY product_id
SINCE -30d
```

### This demonstrates:
- Knowledge of Shopify analytics datasets
- Correct dataset selection
- Time-based aggregation logic
- Practical analytics reasoning


## Error Handling

- Empty or invalid questions are handled gracefully
- Ambiguous questions prompt clarification
- Safe defaults prevent misleading insights


##Tech Stack

- Backend API: Ruby on Rails (API-only)
- AI Service: Python + FastAPI
- Analytics Language: ShopifyQL
- Authentication: Shopify OAuth (designed)
- Data Source: Mock Shopify analytics data

## Project Structure

```plaintext
shopify-ai-analytics/
├── rails_api/
│   └── app/controllers/api/v1/questions_controller.rb
├── python_ai/
│   └── main.py
└── README.md
```

## Design Philosophy

The project focuses on clarity, correctness, and reasoning depth rather than production polish.

###Key priorities:
- Explainable AI behavior
- Clean system boundaries
- Real-world analytics thinking
- Business-friendly insights

## Future Enhancements

- Full Shopify OAuth integration
- Real Shopify Analytics API execution
- LLM-based ShopifyQL generation
- Conversation memory for follow-up questions
- Caching and performance optimizations
