import os

def get_files_info(working_directory, directory="."):
    return_string = []
    
    if directory == ".":
        return_string.append("Result for current directory:")
    else:
        return_string.append(f"Result for '{directory}' directory:")
    
    try:
        full_abspath = os.path.abspath(os.path.join(working_directory, directory))
        work_abspath = os.path.abspath(working_directory)
    
        if not full_abspath.startswith(work_abspath):
            return_string.append(f'\tError: Cannot list "{directory}" as it is outside the permitted working directory')
        elif not os.path.isdir(full_abspath):
            return_string.append(f'\tError: "{directory}" is not a directory')
        else:
            return_string.append("\n".join(list(map(lambda data: f'\t- {data}: file_size={os.path.getsize(f'{full_abspath}/{data}')} bytes, is_dir={os.path.isdir(f'{full_abspath}/{data}')}', os.listdir(full_abspath)))))
    
    except Exception as e:
        return_string.append(f"\tError: {e}")
    
    return "\n".join(return_string)
