from shell.terminal import Terminal

if __name__ == '__main__':
    term = Terminal()
    term.load_commands()
    term.cmdloop()
