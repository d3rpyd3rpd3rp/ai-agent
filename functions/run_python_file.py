import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):
    return_string = []
    
    try:
        full_abspath = os.path.abspath(os.path.join(working_directory, file_path))
        work_abspath = os.path.abspath(working_directory)
        
        if not full_abspath.startswith(work_abspath):
            return_string.append(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        elif not os.path.exists(full_abspath):
            return_string.append(f'Error: File "{file_path}" not found.')
        elif not file_path.endswith('.py'):
            return_string.append(f'Error: "{file_path}" is not a Python file.')
        else:
            try:
                completed = subprocess.run(
                    [sys.executable, file_path, *args],
                    cwd=working_directory,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                stdout_text = completed.stdout or ""
                stderr_text = completed.stderr or ""
                if not stdout_text.strip() and not stderr_text.strip():
                    return_string.append("No output produced.")
                else:
                    if stdout_text:
                        return_string.append(f"STDOUT:\n{stdout_text}")
                    if stderr_text:
                        return_string.append(f"STDERR:\n{stderr_text}")
                    
                if completed.returncode != 0:
                    return_string.append(f"Process exited with code {completed.returncode}")

            except Exception as e:
                return_string.append(f"Error: executing Python file: {e}")
    
    except Exception as e:
        return_string.append(f"Error: {e}")
    
    return "\n".join(return_string)
