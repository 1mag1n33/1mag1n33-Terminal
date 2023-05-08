from src.cli.terminal import Terminal
from src.cli.support_files.update.autoupdate import autoupdate

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
            