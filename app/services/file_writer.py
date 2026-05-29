import os

def write_file(project_name, file_name, code):

    base_path = os.path.join(
        "app",
        "generated_projects",
        project_name
    )

    print("\nBASE PATH:")
    print(base_path)

    os.makedirs(base_path, exist_ok=True)

    file_path = os.path.join(base_path, file_name)

    print("\nWRITING TO:")
    print(file_path)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(code)

    print("\nSUCCESSFULLY WRITTEN")

    return file_path