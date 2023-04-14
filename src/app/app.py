import tkinter as tk
import subprocess
from tkinter import ttk
from src.other.terminal import Terminal

class ConsoleApp:
    def __init__(self, master):
        self.master = master
        self.create_terminal()

    def create_terminal(self):
        self.term = tk.Text(self.master, bg='black', fg='white', font=('Consolas', 11))
        self.term.pack(fill='both', expand=True)
        self.term.focus_set()
        self.term.bind('<Return>', self.execute_command)

    def execute_command(self, event):
        command = self.term.get('input_start', 'end-1c')
        self.term.insert('end', f'\n> {command}\n', 'input_start')
        self.term.tag_config('input_start', foreground='#4CBB17')
        self.term.insert('end', self.run_command(command))
        self.term.see('end')

    def run_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            return output
        except subprocess.CalledProcessError as error:
            return error.output
        
root = tk.Tk()

