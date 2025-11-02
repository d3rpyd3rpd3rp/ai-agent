import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    return_string = []
    
    try:
        full_abspath = os.path.abspath(os.path.join(working_directory, file_path))
        work_abspath = os.path.abspath(working_directory)
        
        if not full_abspath.startswith(work_abspath):
            return_string.append(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        elif not os.path.isfile(full_abspath):
            return_string.append(f'Error: File not found or is not a regular file: "{file_path}"')
        else:
            with open(full_abspath, "r") as f:
                content = f.read(MAX_CHARS + 1)
                if len(content) > MAX_CHARS:
                    content += f'\n[File "{file_path}" truncated at {MAX_CHARS} characters]'
                return_string.append(content)
    
    except Exception as e:
        return_string.append(f"Error: {e}")
    
    return "\n".join(return_string)
