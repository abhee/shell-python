import sys


def main():
    PROMPT = '$'
    while True:
         sys.stdout.write(f"{PROMPT} ")
         user_input = input()
         # exit builtin - breaks the REPL
         if user_input == "exit":
             break
         
         print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
