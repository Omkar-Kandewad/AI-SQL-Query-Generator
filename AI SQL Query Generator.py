import streamlit as st
from groq import Groq

# -------------------------------
# GROQ API KEY
# -------------------------------
client = Groq(
    api_key="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"
)

# -------------------------------
# STREAMLIT UI
# -------------------------------
st.set_page_config(page_title="AI SQL Generator")

st.title("AI SQL Query Generator")

user_input = st.text_area(
    "Enter your question"
)

# -------------------------------
# PROMPT
# -------------------------------
prompt = f"""
You are an expert SQL query generator.

Convert the given text into SQL query.

Database Tables:

customers(
    customer_id,
    customer_name,
    city,
    salary
)

orders(
    order_id,
    customer_id,
    product_name,
    amount
)

Rules:
1. Only generate SQL query
2. Do not explain anything
3. Use proper SQL syntax

Question:
{user_input}
"""

# -------------------------------
# GENERATE SQL
# -------------------------------
if st.button("Generate SQL"):

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    sql_query = response.choices[0].message.content

    st.subheader("Generated SQL Query")

    st.code(sql_query, language="sql")



