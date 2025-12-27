from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -----------------------------
# Request Schema
# -----------------------------
class QuestionRequest(BaseModel):
    store_id: str
    question: str

# -----------------------------
# Mock Shopify Data
# (used until real Shopify integration)
# -----------------------------
MOCK_SHOPIFY_DATA = {
    "avg_daily_sales": 10,
    "top_products": ["Product A", "Product B", "Product C"],
    "repeat_customers": 5
}

# -----------------------------
# ShopifyQL Generator
# -----------------------------
def generate_shopifyql(intent):
    if intent == "inventory":
        return """
        FROM orders
        SHOW sum(quantity) AS total_units_sold
        GROUP BY product_id
        SINCE -30d
        """
    elif intent == "sales":
        return """
        FROM orders
        SHOW sum(total_sales) AS total_sales
        SINCE -7d
        """
    elif intent == "customers":
        return """
        FROM orders
        SHOW count(distinct customer_id) AS repeat_customers
        SINCE -90d
        """
    return None

# -----------------------------
# Main AI Agent Endpoint
# -----------------------------
@app.post("/ask")
def ask_question(data: QuestionRequest):
    question = data.question.lower().strip()

    # Handle empty question
    if not question:
        return {
            "answer": "Please ask a valid business question.",
            "confidence": "low"
        }

    # -------------------------
    # Intent Detection
    # -------------------------
    if "reorder" in question or "inventory" in question:
        intent = "inventory"
    elif "sale" in question:
        intent = "sales"
    elif "customer" in question:
        intent = "customers"
    else:
        intent = "unknown"

    # Generate ShopifyQL internally (not exposed)
    _shopifyql = generate_shopifyql(intent)

    # -------------------------
    # Business Logic
    # -------------------------
    if intent == "inventory":
        avg_sales = MOCK_SHOPIFY_DATA["avg_daily_sales"]
        reorder_qty = avg_sales * 7

        answer = (
            f"Based on the last 30 days, you sell around {avg_sales} units per day. "
            f"You should reorder at least {reorder_qty} units to avoid stockouts next week."
        )
        confidence = "medium"

    elif intent == "sales":
        top_products = ", ".join(MOCK_SHOPIFY_DATA["top_products"])
        answer = (
            f"Your sales have been steady recently. "
            f"Top selling products include {top_products}."
        )
        confidence = "medium"

    elif intent == "customers":
        repeat_customers = MOCK_SHOPIFY_DATA["repeat_customers"]
        answer = (
            f"{repeat_customers} customers placed repeat orders in the recent period."
        )
        confidence = "low"

    else:
        answer = (
            "I need more details to answer this question accurately. "
            "Please specify inventory, sales, or customers."
        )
        confidence = "low"

    # -------------------------
    # Final Clean Response
    # -------------------------
    return {
        "answer": answer,
        "confidence": confidence
    }
