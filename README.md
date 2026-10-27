# 🤖 AI SQL Query Generator

## 📌 Project Overview

The AI SQL Query Generator is an interactive web application developed using Python and Streamlit. It uses a large language model through the Groq API to convert natural-language questions into SQL queries based on predefined database tables.

Users can enter questions in plain English and generate SQL queries for customer and order data, making SQL query creation easier and faster.

## ✨ Key Features

- **Natural Language to SQL:** Convert user questions into SQL queries.
- **Interactive Interface:** Enter questions through a Streamlit text area.
- **AI-Powered Generation:** Generate SQL using a language model accessed through the Groq API.
- **Predefined Database Schema:** Supports `customers` and `orders` tables.
- **SQL Code Display:** Display generated queries with SQL syntax highlighting.
- **Consistent Output:** Uses a low temperature setting for more consistent query generation.

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- Large Language Models (LLMs)
- SQL

## 🗄️ Database Schema

### Customers Table

- `customer_id`
- `customer_name`
- `city`
- `salary`

### Orders Table

- `order_id`
- `customer_id`
- `product_name`
- `amount`

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-sql-query-generator.git
cd ai-sql-query-generator
```

### 2. Install dependencies

```bash
pip install streamlit groq
```

### 3. Configure the API key

Store your Groq API key securely in an environment variable or Streamlit secrets. Do not hardcode private API keys in your source code.

### 4. Run the application

```bash
streamlit run "AI SQL Query Generator.py"
```

## 💡 Example

**Input question:**

Show all customers from Pune.

**Example generated SQL:**

```sql
SELECT *
FROM customers
WHERE city = 'Pune';
```

*The generated query may vary depending on the model response.*

## 🎯 Project Objective

The goal of this project is to demonstrate how natural-language processing and large language models can simplify SQL query generation and make database querying more accessible to users.

## 🔮 Future Enhancements

- Connect to a live database to execute generated queries.
- Support additional database schemas.
- Add SQL query validation and error handling.
- Provide query explanations and optimization suggestions.
- Add support for different SQL dialects.
- Introduce a query history feature.

## 👨‍💻 Skills Demonstrated

Python programming, Streamlit application development, API integration, prompt engineering, SQL fundamentals, and LLM-based application development.
