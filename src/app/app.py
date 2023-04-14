import tkinter as tk
from src.other.terminal import Terminal

class ConsoleApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("1mag1n33 Terminal")
        self.pack()
        self.create_widgets()
        self.create_terminal()
        
    def create_widgets(self):
        # Console area
        self.console = tk.Text(self, wrap=tk.WORD, bg='black', fg='white', insertbackground='white')
        self.console.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.console.bind('<Return>', self.handle_input)

        # Input prompt
        self.prompt = tk.Label(self, text="1mag1n33 $ ", bg='black', fg='white')
        self.prompt.pack(side=tk.LEFT, anchor=tk.SW)

        # Input area
        self.input_entry = tk.Entry(self, bg='black', fg='white', insertbackground='white')
        self.input_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Exit button
        self.exit_button = tk.Button(self, text="Exit", command=self.handle_exit, bg='black', fg='white')
        self.exit_button.pack(side=tk.RIGHT, anchor=tk.SE)
        
    def create_terminal(self):
        self.term = Terminal(self.write_output)
        self.term.load_commands()
        
    def handle_input(self, event):
        input_text = self.input_entry.get()
        self.console.insert(tk.END, f'{self.prompt["text"]}{input_text}\n')
        self.input_entry.delete(0, tk.END)
        self.term.onecmd(input_text)
        
    def write_output(self, output):
        self.console.insert(tk.END, output)
        
    def handle_exit(self):
        self.term.onecmd('exit')
        self.master.destroy()
        
root = tk.Tk()

