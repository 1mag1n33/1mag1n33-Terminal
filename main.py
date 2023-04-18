from src.other.terminal import Terminal
from src.commands.do_exit import do_exit

if __name__ == '__main__':
    term = Terminal()
    term.load_commands()
    while True:
        try:
            term.cmdloop()
            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            do_exit()