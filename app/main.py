import sys
import os

PROMPT = '$'


def main():
    while True:
         sys.stdout.write(f"{PROMPT} ")
         user_input = input()
         tokens = user_input.split()

         if _is_builtin(tokens[0]):
             do_builtins(tokens)
         elif _is_exec(tokens[0]):
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
    """Execute a binary with the arguments specified """
    pass

def _is_exec(arg):
    """ Returns (True, file_path) if the file is a executable.
        Returns (False, None) if the file is not executable, or does not exist.
    """
    dirs = os.environ['PATH'].split(':')
    
    for dir_name in dirs:
        file_path = f"{dir_name}/{arg}"
        
        if os.access(file_path, os.X_OK):
            return True, file_path

    return False, None

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
    is_a_binary, file_path = _is_exec(cmd)
    
    if is_a_binary:
        print(f"{cmd} is {file_path}")
        return
   
    # cmd is neither a bultin, nor an executable file
    print(f"{cmd}: not found")
    

if __name__ == "__main__":
    main()
