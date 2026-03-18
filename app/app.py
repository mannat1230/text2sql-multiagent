import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import gradio as gr
from src.pipelines.text2sql_pipeline import run_pipeline


def app_fn(question):
    steps, sql, result = run_pipeline(question)

    return (
        f"Steps:\n{steps}",
        f"SQL:\n{sql}",
        f"Result:\n{result}"
    )


gr.Interface(
    fn=app_fn,
    inputs="text",
    outputs=["text", "text", "text"],
    title="Multi-Agent Text2SQL System"
).launch()