import sys
import os
import sys
import os
# List of available commands
commands_list = ["exit", "echo", "type", "cd"]

def main():
    while True:
        # Display the prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        # Read the user input
        command = input()
        
        # Extract the command and arguments
        cmd = command.split(" ", 1)[0]
        
        # Get the system paths and home directory
        paths = os.environ.get('PATH')
        home = os.environ.get('HOME')
        directories = paths.split(':')
        
        # Initialize variables for found executable paths
        executable_path = None
        builtin_path = None
        
        for dir in directories:
            if os.path.isfile(f"{dir}/{command.split(' ', 1)[0]}"):
                builtin_path = f"{dir}/{command.split(' ', 1)[0]}"
        
        # Check if the command is "exit"
        if cmd == "exit":
            sys.exit(0)
        
        # Check if the command is "echo"
        elif cmd == "echo":
            # Print the argument
            sys.stdout.write(command.split(" ", 1)[1] + "\n")
        
        # Check if the command is "type"
        elif cmd == "type":
            # Search for the command in the directories
            for dir in directories:
                if os.path.isfile(f"{dir}/{command.split(' ', 1)[1]}"):
                    executable_path = f"{dir}/{command.split(' ', 1)[1]}"
            
            # Check if the command is a shell builtin
            if command.split(" ", 1)[1] in commands_list:
                sys.stdout.write(f"{command.split(' ', 1)[1]} is a shell builtin\n")
            
            # Check if the command is found in the directories
            elif executable_path:
                sys.stdout.write(f"{command.split(' ', 1)[1]} is {executable_path}\n")
            
            # Command not found
            else:
                sys.stdout.write(f"{command.split(' ', 1)[1]}: not found\n")
        
        # Check if the command is "cd"
        elif cmd == "cd":
            # Change directory to home
            if command.split(" ", 1)[1] == "~":
                os.chdir(home)
            
            # Change directory to the specified path
            else:
                try:
                    os.chdir(command.split(" ", 1)[1])
                except FileNotFoundError:
                    sys.stdout.write(f"cd: {command.split(' ', 1)[1]}: No such file or directory\n")
        
        # Check if the command is an executable file
        elif builtin_path:
            os.system(command)
        
        # Command not found
        else:
            sys.stdout.write(f"{command.split(' ', 1)[0]}: command not found\n")
        
        sys.stdout.flush()

if __name__ == "__main__":
    main()
