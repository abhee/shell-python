import sys
from . import cmdparser
from . import runner


_PROMPT = '$ '


# Implements the shell REPL
def repl():
    while True:
        sys.stdout.write(f"{_PROMPT}")
        try:
            user_input = input()
        except EOFError:
            break

        runner.run(cmdparser.tokenize(user_input))
         

if __name__ == "__main__":
    repl()
