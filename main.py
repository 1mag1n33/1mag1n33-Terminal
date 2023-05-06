from src.other.terminal import Terminal

def exit():
    print('Exiting the terminal...')
    raise SystemExit

if __name__ == '__main__':
    term = Terminal()
    while True:
        try:
            term.cmdloop()
            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            exit()
            