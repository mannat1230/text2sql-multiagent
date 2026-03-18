from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0)

def validate(sql, schema, llm):
    prompt = f"""
    Validate this SQL:
    {sql}

    Schema:
    {schema}

    Fix if incorrect.
    """

    return llm.invoke(prompt).content