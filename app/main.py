import sys
import shell_builtins
import runner


_PROMPT = '$ '


# Implements the shell REPL
def repl():
    while True:
        sys.stdout.write(f"{_PROMPT}")
        try:
            user_input = input()
        except EOFError:
            break

        tokens = user_input.split()
        runner.run(tokens)
         

if __name__ == "__main__":
    repl()
