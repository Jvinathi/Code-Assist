import ast

from core.llm import llm
from core.prompts import ARCHITECT_PROMPT

def architect_agent(plan):

    response = llm.invoke(
        f"{ARCHITECT_PROMPT}\n\n{plan}"
    )

    raw_output = response.content.strip()

    print("\nRAW OUTPUT:")
    print(raw_output)

    try:

        file_list = ast.literal_eval(raw_output)

        if isinstance(file_list, list):

            print("\nPARSED SUCCESSFULLY")
            print(file_list)

            return file_list

        return []

    except Exception as e:

        print("\nPARSING FAILED")
        print(e)

        return []