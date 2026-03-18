from src.agents.planner import plan
from src.agents.sql_generator import generate
from src.agents.validator import validate
from src.agents.executor import execute
from src.utils.db import get_schema

def run_pipeline(question, schema, llm):
    steps = plan(question, llm)

    sql = generate_sql(question, schema)

    validated_sql = validate(sql, schema, llm)

    result = execute(validates_sql)

    return {
        "steps": steps,
        "sql": validated_sql,
        "result": result
    }