import sys

commands_list = ["exit 0"]

def main():

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command not in commands_list:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()
        elif command == "exit 0":
            sys.exit(0)
            

if __name__ == "__main__":
    main()
