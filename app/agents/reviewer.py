from core.llm import llm
from core.prompts import REVIEWER_PROMPT

def reviewer_agent(
    file_name,
    original_code,
    architecture,
    project_description
):

    prompt = f"""
{REVIEWER_PROMPT}

PROJECT DESCRIPTION:
{project_description}

PROJECT FILES:
{architecture}

CURRENT FILE:
{file_name}

ORIGINAL CODE:
{original_code}

Review and improve this code.
Fix all issues.
Return corrected code only.
"""

    response = llm.invoke(prompt)

    return response.content