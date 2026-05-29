import os
import streamlit as st

from core.graph_builder import graph
from services.zip_service import create_zip
from services.execution_validator import run_validation

st.set_page_config(
    page_title="AI Coding Assistant",
    layout="wide"
)

st.title("🤖 Multi-Agent AI Coding Assistant")

st.write(
    "Generate complete software projects using AI agents."
)

prompt = st.text_area(
    "Enter your software request",
    height=200
)

if st.button("Generate Project"):

    if not prompt.strip():

        st.warning("Please enter a project request.")

    else:

        with st.spinner("AI Agents Generating Project..."):

            # ---------------------------------
            # RUN GRAPH
            # ---------------------------------

            result = graph.invoke({
                "user_prompt": prompt
            })

            st.success("Project Generated Successfully!")

            # ---------------------------------
            # SHOW FILES
            # ---------------------------------

            st.subheader("Generated Files")

            for file_name in result["architecture"]:

                st.write(f"✅ {file_name}")

            # ---------------------------------
            # PROJECT PATH
            # ---------------------------------

            project_path = os.path.join(
                "app",
                "generated_projects",
                result["project_name"]
            )

            # ---------------------------------
            # SHOW GENERATED CODE
            # ---------------------------------

            st.subheader("Generated Code")

            for file_name in result["architecture"]:

                file_path = os.path.join(
                    project_path,
                    file_name
                )

                if os.path.exists(file_path):

                    with open(
                        file_path,
                        "r",
                        encoding="utf-8"
                    ) as file:

                        code = file.read()

                    st.markdown(f"### {file_name}")

                    st.code(
                        code,
                        language="html"
                    )

            # ---------------------------------
            # EXECUTION VALIDATION
            # ---------------------------------

            st.subheader("Execution Validation")

            index_path = os.path.abspath(
                os.path.join(
                    project_path,
                    "index.html"
                )
            )

            validation_result = run_validation(
                index_path
            )

            if validation_result["success"]:

                st.success(
                    "App Executed Successfully!"
                )

            else:

                st.error(
                    "Execution Failed"
                )

                st.write(
                    validation_result["errors"]
                )

            # ---------------------------------
            # CREATE ZIP
            # ---------------------------------

            zip_path = os.path.join(
                "app",
                "generated_projects",
                f"{result['project_name']}.zip"
            )

            create_zip(
                project_folder=project_path,
                output_zip=zip_path
            )

            # ---------------------------------
            # DOWNLOAD BUTTON
            # ---------------------------------

            with open(zip_path, "rb") as file:

                st.download_button(
                    label="⬇ Download Project ZIP",
                    data=file,
                    file_name=f"{result['project_name']}.zip",
                    mime="application/zip"
                )