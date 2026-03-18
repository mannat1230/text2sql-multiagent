from src.utils.db import run_query

def execute(sql):
    try:
        return run_query(sql)
    except Exception as e:
        return str(e)