from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(temperature=0)

def generate(question, schema):
    prompt = f"""
    You are a SQL expert.

    Use ONLY the given schema.
    Do NOT invent columns.

    Schema:
    {schema}

    Generate valid SQLite SQL.

    Question: {question}
    """
    return llm.invoke(prompt).content