import subprocess
from . import shell_builtins
from . import fileutil


def run(tokens):
    """Run command with specified arguments."""
    cmd, args = tokens[0], tokens[1:]
    if shell_builtins.is_builtin(cmd):
        shell_builtins.get_builtin(cmd)(args)
    elif (path := fileutil.find_exe_file(cmd)):
        subprocess.run(tokens)
    else:
        print(f"{cmd}: command not found")
    
