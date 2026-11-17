import os

def find_exe_file(name: str) -> str | None:
    """ Returns abolute path of the executable file if it exists, None otherwise.
    """
    # name already contains file path 
    if os.path.exists(name) or name.startswith("/"):
        return name
    
    for dir_path in os.environ['PATH'].split(':'):
        file_path = f"{dir_path}/{name}"
        
        if os.access(file_path, os.X_OK):
            return file_path

    # File does not exist
    return None
