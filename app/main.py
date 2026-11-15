import sys


def main():
    PROMPT = '$'
    while True:
         sys.stdout.write(f"{PROMPT} ")
         user_input = input()
         print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
