import sys
import os
import subprocess

PROMPT = '$'


def main():
    while True:
         sys.stdout.write(f"{PROMPT} ")
         user_input = input()
         tokens = user_input.split()

         if _is_builtin(tokens[0]):
             do_builtins(tokens)
         elif _is_exec(_find_file_path(tokens[0])):
             do_exec(tokens)
         else:
             print(f"{user_input}: command not found")

def do_builtins(cmd):
    """ Execute builtin commands. """
    if cmd[0] == "exit":
        _exit()
    elif cmd[0] == "echo":
        _echo(cmd[1:])
    elif cmd[0] == "type":
        _type(cmd[1])
    else:
        pass
    
def do_exec(cmd):
    """Execute a binary with the specified arguments"""
    subprocess.run(cmd)

def _find_file_path(file_name):
    """ Returns abolute path of the file if it exists, None otherwise.
    """
   
    if file_name.startswith("./") and os.path.exists:
        return file_name  # file exists in current directory.

    directories_in_path = os.environ['PATH'].split(':')
    
    for dir_name in directories_in_path:
        file_path = f"{dir_name}/{file_name}"
        
        if os.access(file_path, os.X_OK):
            return file_path

    # File does not exist
    return None
    

def _is_exec(file_path):
    """ Returns True if the file exists and is an executable file.
        Returns False if the file does not exist, or is not an executable file.
    """
    return file_path is not None and os.access(file_path, os.X_OK)

def _is_builtin(arg):
    BUILTINS = {'exit', 'echo', 'type'}
    return arg in BUILTINS

def _exit():
    """BUILTIN exit - breaks the REPL """
    sys.exit()

def _echo(args):
    """ BUILTIN echo - prints its arguments to stdout """
    print(" ".join(args))

def _type(cmd):
    """ prints type of command """

    # Handle bultins
    if _is_builtin(cmd):
        print(f"{cmd} is a shell builtin")
        return
       
    
    # Check whether cmd is in path and is an executable
    file_path = _find_file_path(cmd)
    
    if _is_exec(file_path):
        print(f"{cmd} is {file_path}")
    else:
        print(f"{cmd}: not found")  # cmd is neither a bultin, nor an executable file
    

if __name__ == "__main__":
    main()
