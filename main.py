from src.other.terminal import Terminal
from src.other.support_files.update.github import autoupdate

def exit():
    print('Exiting the terminal...')
    raise SystemExit

if __name__ == '__main__':
    term = Terminal()
    autoupdate()
    while True:
        try:
            term.cmdloop()
            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            exit()
            