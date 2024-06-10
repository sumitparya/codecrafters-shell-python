import sys

commands_list = ["exit","echo"]

def main():

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        cmd = command.split(" ",1)[0]
        if cmd not in commands_list:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()
        else:
            if cmd == "exit":
                sys.exit(0)
            elif cmd == "echo":
                sys.stdout.write(command.split(" ",1)[1] + "\n")
                sys.stdout.flush()
            

if __name__ == "__main__":
    main()
