class CommandHistory:
    def __init__(self):
        self.history = []

    def add_command(self, command):
        self.history.append(command)

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history.clear()

    def print_history(self):
        print("Command History:")
        for i, command in enumerate(self.history, 1):
            print(f"{i}. {command}")

    def cmdloop(self, prompt):
        while True:
            try:
                line = input(prompt)
            except EOFError:
                line = 'EOF'
            if not line:
                continue

            # Add the command to the history
            self.add_command(line.strip())

            # Exit the loop if the user enters "exit"
            if line.lower() == 'exit':
                break

            # Pass the command to the command processor
            self.onecmd(line)

            # Reset the prompt for the next command
            self.prompt = prompt
