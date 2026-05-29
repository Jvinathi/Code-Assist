from datetime import datetime

def generate_project_name(user_prompt):

    cleaned_name = user_prompt.lower()

    cleaned_name = cleaned_name.replace("build", "")
    cleaned_name = cleaned_name.replace("create", "")
    cleaned_name = cleaned_name.replace("app", "")

    cleaned_name = cleaned_name.strip()

    cleaned_name = cleaned_name.replace(" ", "_")

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    project_name = f"{cleaned_name}_{timestamp}"

    return project_name