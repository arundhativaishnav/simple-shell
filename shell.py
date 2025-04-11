import subprocess

def execute_command(command):
    """Execute a shell command and return the output."""
    try:
        # Use subprocess.run to execute the command
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print("Output:\n", result.stdout)
        else:
            print("Error:\n", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to run the shell command executor."""
    print("Simple Shell Command Executor")
    print("Type 'exit' to quit the program.")
    
    while True:
        # Prompt the user for a command
        command = input("Enter a shell command: ")
        
        if command.lower() == 'exit':
            print("Exiting the shell command executor.")
            break
        
        # Execute the command
        execute_command(command)

if __name__ == "__main__":
    main()