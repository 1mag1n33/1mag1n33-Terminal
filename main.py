from src.other.terminal import Terminal


if __name__ == '__main__':
    term = Terminal()
    while True:
        try:
            term.cmdloop()
            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            term.do_exit()