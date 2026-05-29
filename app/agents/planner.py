from core.llm import llm
from core.prompts import PLANNER_PROMPT

def planner_agent(user_prompt):
    response = llm.invoke(
        f"{PLANNER_PROMPT}\n\nUser Request:\n{user_prompt}"
    )

    return response.content