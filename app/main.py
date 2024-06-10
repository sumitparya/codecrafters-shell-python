import sys
import os

commands_list = ["exit","echo","type"]
status=0

def main():

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        cmd = command.split(" ",1)[0]
        if cmd not in commands_list:
            sys.stdout.write(f"{command}: not found\n")
        else:
            if cmd == "exit":
                sys.exit(0)
            elif cmd == "echo":
                sys.stdout.write(command.split(" ",1)[1] + "\n")
            elif cmd == "type":
                paths = os.environ.get('PATH')
                directories = paths.split(':')
                for dir in directories:
                    program_path = os.path.join(dir, command.split(" ",1)[1])
                    if os.path.isfile(program_path):
                        status=1
                    else:
                        status=0              
                if status == 1:
                    sys.stdout.write(f"{command.split(' ',1)[1]} is {dir}/{command.split(' ',1)[1]}\n")
                else:
                    sys.stdout.write(f"{command.split(' ',1)[1]}: not found\n")
        sys.stdout.flush()
        

if __name__ == "__main__":
    main()
