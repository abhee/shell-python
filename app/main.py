import sys
import os

BUILTINS = {'exit', 'echo', 'type', 'cd'}
PROMPT = '$'


def main():
    
    while True:
         sys.stdout.write(f"{PROMPT} ")
         user_input = input()
         tokens = user_input.split()
         
         if tokens[0] == "exit":
             do_exit()
         elif tokens[0] == "echo":
             do_echo(tokens[1:])
         elif tokens[0] == "type":
             do_type(tokens[1])
         else:
             print(f"{user_input}: command not found")

def do_exit():
    """BUILTIN exit - breaks the REPL """
    sys.exit()

def do_echo(args):
    """ BUILTIN echo - prints its arguments to stdout """
    print(" ".join(args))
    
def do_type(cmd):
    """ Returns type of commands """

    # Handle bultins
    if cmd in BUILTINS:
        print(f"{cmd} is a shell builtin")
        return

    # Check whether cmd is in path and is an executable
    dirs = os.environ['PATH'].split(':')
    
    for dir_name in dirs:
        file_path = f"{dir_name}/{cmd}"
        
        if os.access(file_path, os.X_OK):
            print(f"{cmd} is {file_path}")
            return
    else:
        print(f"{cmd}: not found")
    

if __name__ == "__main__":
    main()
