from shell_builtins import is_builtin, get_builtin
import fileutil
import subprocess

def run(tokens):
    """Run command with specified arguments."""
    cmd, args = tokens[0], tokens[1:]
    if is_builtin(cmd):
        get_builtin(cmd)(args)
    elif (path := fileutil.find_exe_file(cmd)):
        subprocess.run(tokens)
    else:
        print(f"{user_input}: command not found")
    
