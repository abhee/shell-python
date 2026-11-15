import sys


def main():
    PROMPT = '$'
    while True:
         sys.stdout.write(f"{PROMPT} ")
         user_input = input()
         tokens = user_input.split()
         
         # exit builtin - breaks the REPL
         if tokens[0] == "exit":
             break

         # BUILTIN echo - prints its arguments to stdout
         elif tokens[0] == "echo":
             print(" ".join(tokens[1:]))
         else:
             print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
