def do_source(self, args):
    """
    Execute commands from a file in the current shell environment.
    """
    if not args:
        print("Usage: source <filename>")
        return

    try:
        with open(args) as f:
            contents = f.read()
            exec(contents, globals(), locals())
    except FileNotFoundError:
        print(f"File '{args}' not found.")
    except Exception as e:
        print(f"Error executing file '{args}': {str(e)}")
