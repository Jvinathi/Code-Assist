from typing import TypedDict
from agents.reviewer import reviewer_agent
from langgraph.graph import StateGraph, END
from services.project_namer import generate_project_name
from agents.planner import planner_agent
from agents.architect import architect_agent
from agents.coder import coder_agent
from services.js_validator import validate_javascript
from services.file_writer import write_file
from services.code_validator import clean_code

class GraphState(TypedDict):
    user_prompt: str
    plan: str
    architecture: list
    project_name: str

# -----------------------------
# PLANNER NODE
# -----------------------------

def planner_node(state):

    print("\nRUNNING PLANNER NODE")

    plan = planner_agent(
        state["user_prompt"]
    )

    project_name = generate_project_name(
        state["user_prompt"]
    )

    print("\nPROJECT NAME:")
    print(project_name)

    return {
        "plan": plan,
        "project_name": project_name
    }
# -----------------------------
# ARCHITECT NODE
# -----------------------------

def architect_node(state):

    print("\nRUNNING ARCHITECT NODE")

    architecture = architect_agent(state["plan"])

    return {
        "architecture": architecture
    }

# -----------------------------
# CODER NODE
# -----------------------------

def coder_node(state):

    print("\nRUNNING CODER NODE")

    project_name = state["project_name"]

    for file_name in state["architecture"]:

        print(f"\nGenerating file: {file_name}")

        max_retries = 3

        final_code = None

        for attempt in range(max_retries):

            print(f"\nATTEMPT {attempt + 1}")

            # ---------------------------------
            # GENERATE CODE
            # ---------------------------------

            generated_code = coder_agent(
                file_name=file_name,
                project_description=state["user_prompt"],
                architecture=state["architecture"]
            )

            print("\nINITIAL CODE GENERATED")

            # ---------------------------------
            # REVIEW CODE
            # ---------------------------------

            reviewed_code = reviewer_agent(
                file_name=file_name,
                original_code=generated_code,
                architecture=state["architecture"],
                project_description=state["user_prompt"]
            )

            print("\nCODE REVIEW COMPLETED")

            # ---------------------------------
            # VALIDATE JAVASCRIPT
            # ---------------------------------

            if file_name.endswith(".js"):

                valid, error = validate_javascript(
                    reviewed_code
                )

                if valid:

                    print("\nVALID JAVASCRIPT")

                    final_code = reviewed_code

                    break

                else:

                    print("\nINVALID JAVASCRIPT")

                    print(error)

            else:

                final_code = reviewed_code

                break

        # ---------------------------------
        # SAVE FINAL CODE
        # ---------------------------------

        if final_code:

            write_file(
                project_name=project_name,
                file_name=file_name,
                code=final_code
            )

            print(f"\nFINAL FILE WRITTEN: {file_name}")

        else:

            print(
                f"\nFAILED TO GENERATE VALID CODE FOR {file_name}"
            )

    return state
# -----------------------------
# BUILD GRAPH
# -----------------------------

builder = StateGraph(GraphState)

builder.add_node("planner", planner_node)

builder.add_node("architect", architect_node)

builder.add_node("coder", coder_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "architect")

builder.add_edge("architect", "coder")

builder.add_edge("coder", END)

graph = builder.compile()