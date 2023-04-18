def do_help(self, args):
        if args:
            try:
                func = getattr(self, 'help_' + args)
            except AttributeError:
                print(f'No help found for "{args}"')
            else:
                print(func.__doc__)
        else:
            commands = sorted([cmd[3:] for cmd in dir(self) if cmd.startswith('do_')])
            print('\n'.join(commands))

def help_help(self):
    """
    Usage: ?, help
    Gives you a list of the commands.
    """