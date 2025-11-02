import os

def write_file(working_directory, file_path, content=""):
    return_string = []
    
    try:
        full_abspath = os.path.abspath(os.path.join(working_directory, file_path))
        work_abspath = os.path.abspath(working_directory)
        
        if not full_abspath.startswith(work_abspath):
            return_string.append(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        elif not os.path.exists(full_abspath):
            os.makedirs(os.path.dirname(full_abspath), exist_ok=True)
            
            if content != "":
                with open(full_abspath, "w") as f:
                    f.write(content)
                return_string.append(f'Successfully wrote to "{file_path}" ({len(content)} characters written). Created missing directories')
            else:
                return_string.append(f'Error: Cannot write to "{file_path}" as no information to write was given. Missing directories still created')
        else:
            if content != "":
                with open(full_abspath, "w") as f:
                    f.write(content)
                return_string.append(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
            else:
                return_string.append(f'Error: Cannot write to "{file_path}" as no information to write was given')
    
    except Exception as e:
        return_string.append(f"Error: {e}")
    
    return "\n".join(return_string)