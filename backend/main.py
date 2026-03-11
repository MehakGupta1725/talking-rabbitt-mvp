from fastapi import FastAPI
import pandas as pd
from groq import Groq
import os

app = FastAPI()

# Load API key from environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@app.post("/analyze")
async def analyze(data: dict):

    question = data["question"]
    table = data["data"]

    df = pd.DataFrame(table)

    prompt = f"""
You are a professional business intelligence analyst.

A user uploaded a dataset.

Dataset columns:
{list(df.columns)}

User question:
{question}

Provide a short professional business insight.

Rules:
- Do NOT include code.
- Do NOT include formulas.
- Do NOT mention programming or pandas.
- Write in clear business language.
- Maximum 2 sentences.

Example style:
"The North region generated the highest revenue, indicating stronger sales performance compared to other regions."
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    # Safety: remove code blocks if model accidentally outputs them
    answer = answer.replace("```", "")
    answer = answer.replace("python", "")

    return {"answer": answer}