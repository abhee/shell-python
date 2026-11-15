import sys
import os

BUILTINS = {'exit', 'echo', 'type', 'cd'}


def main():
    PROMPT = '$'
    
    while True:
         sys.stdout.write(f"{PROMPT} ")
         user_input = input()
         tokens = user_input.split()
         
         # BUILTIN exit - breaks the REPL
         if tokens[0] == "exit":
             break
         # BUILTIN echo - prints its arguments to stdout
         elif tokens[0] == "echo":
             do_echo(tokens[1:])
         elif tokens[0] == "type":
             do_type(tokens[1:])
         else:
             print(f"{user_input}: command not found")

def do_echo(args):
    """ prints args as is on console. """
    print(" ".join(args))
    
def do_type(args):
    """ Returns type of commands """
    for cmd in args:
        if cmd in BUILTINS:
            print(f"{cmd} is a shell builtin")
        else:
            print(f"{cmd}: not found")


if __name__ == "__main__":
    main()
