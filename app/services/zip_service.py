import os
import zipfile

def create_zip(project_folder, output_zip):

    with zipfile.ZipFile(
        output_zip,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        for root, dirs, files in os.walk(project_folder):

            for file in files:

                file_path = os.path.join(root, file)

                arcname = os.path.relpath(
                    file_path,
                    project_folder
                )

                zipf.write(file_path, arcname)

    return output_zip