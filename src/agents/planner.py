from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0)

def plan(question):
    prompt = f"""
    Break this question into logical steps:

    {question}
    """
    response = llm.invoke(prompt)
    return response.content.strip()