import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs


        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        else:
            dir_list = os.listdir(target_dir)
            rows = []
            for item in dir_list:
                name = item
                file_size = os.path.getsize(os.path.join(target_dir, item))
                isdir = os.path.isdir(os.path.join(target_dir, item))
                rows.append(f"- {name}: file_size={file_size} bytes, is_dir={isdir}")
            return "\n".join(rows)

    except Exception:
        return "Error: ya fucked up"