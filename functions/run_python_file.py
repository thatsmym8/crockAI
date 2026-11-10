import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run the code contained in the specified .py file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to a .py file to run code from, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "additional arguments that may be required for the desired function"
                }
            },
            "required": ["file_path"]
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args is not None:
            command.extend(args)

        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30)
        nonzero = f"Process exited with code {completed_process.returncode}"
        no_output = "No output produced"
        output = f"STDOUT: {completed_process.stdout} STDERR: {completed_process.stderr}"

        if completed_process.returncode != 0:
            return nonzero
        elif completed_process.stdout is None and completed_process.stderr is None:
            return no_output
        else:
            return output

    except Exception as e:
        return f"Error: executing Python file: {e}"