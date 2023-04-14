from src.other.terminal import Terminal
import os


if __name__ == '__main__':
    term = Terminal()
    term.load_commands()
    while True:
        try:
            term.cmdloop()
            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            term.do_exit()
            
            
