from src.llm import ask_llm

COLUMNS = """
ticket_id
created_at
category
priority
status
response_time_hrs
resolution_time_hrs
agent_id
customer_rating
issue_summary
"""

def generate_pandas_query(question):

    prompt = f"""
You are a data analyst.

DataFrame name is df.

Available columns:

{COLUMNS}

Return ONLY one pandas expression.

Do not import anything.
Do not define functions.
Do not use loops.
Do not use print.

Return ONLY valid pandas code.

Examples:

Question:
How many tickets are open?

Answer:
df[df["status"]=="Open"].shape[0]

Question:
{question}
"""

    return ask_llm(prompt)

def run_query(question, df):

    code = generate_pandas_query(question)

    try:
        result = eval(code)

        return {
            "query": code,
            "result": str(result)
        }

    except Exception as e:
        return {
            "query": code,
            "error": str(e)
        }