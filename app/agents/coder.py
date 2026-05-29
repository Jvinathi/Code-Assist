from core.llm import llm
from core.prompts import CODER_PROMPT


def coder_agent(
    file_name,
    project_description,
    architecture
):

    prompt = f"""
{CODER_PROMPT}

PROJECT REQUIREMENT:
{project_description}

PROJECT FILES:
{architecture}

CURRENT FILE:
{file_name}

STRICT RULES:
1. Return ONLY raw code
2. DO NOT use markdown
3. DO NOT use ```html or ```javascript
4. DO NOT explain anything
5. Start immediately with code
6. Generate COMPLETE WORKING code
7. HTML must correctly link CSS and JS
8. JavaScript must use addEventListener properly
9. Do NOT use placeholder code
10. All buttons must work

For calculator apps:
- Buttons must work
- JavaScript must handle clicks properly
- CSS must style buttons properly
- HTML must connect script.js correctly

For todo apps:
- Add button must work
- Tasks must appear dynamically
- Delete functionality must work
- JavaScript must manipulate DOM properly

Generate COMPLETE code for:
{file_name}
"""

    response = llm.invoke(prompt)

    return response.content.strip()