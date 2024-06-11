import sys
import os

commands_list = ["exit","echo","type"]

def main():

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        cmd = command.split(" ",1)[0]
        paths = os.environ.get('PATH')
        directories = paths.split(':')
        pa=None
        ap=None
        for dir in directories:
            if os.path.isfile(f"{dir}/{command.split(" ",1)[0]}"):
                ap = f"{dir}/{command.split(" ",1)[0]}"
        if cmd == "exit":
            sys.exit(0)
        elif cmd == "echo":
            sys.stdout.write(command.split(" ",1)[1] + "\n")
        elif cmd == "type":
            for dir in directories:
                if os.path.isfile(f"{dir}/{command.split(" ",1)[1]}"):
                    pa = f"{dir}/{command.split(" ",1)[1]}"
            if command.split(" ",1)[1] in commands_list:
                sys.stdout.write(f"{command.split(" ",1)[1]} is a shell builtin\n")
            elif pa:
                sys.stdout.write(f"{command.split(" ",1)[1]} is {pa}\n")
            else:
                sys.stdout.write(f"{command.split(' ',1)[1]}: not found\n")
        elif ap:
            os.system(command)
        else:
            sys.stdout.write(f"{command.split(' ',1)[1]}: command not found\n")
        sys.stdout.flush()
        

if __name__ == "__main__":
    main()
