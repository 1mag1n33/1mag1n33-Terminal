import os
import json
from src.cli.terminal import Terminal
from src.cli.support_files.update.autoupdate import autoupdate
from src.imports import settings

def exit():
    print('Exiting the terminal...')
    raise SystemExit

with open(settings, 'r') as f:
            settings_config = json.load(f)

if __name__ == '__main__':
    
    if settings_config.get('debug', True):
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                term = Terminal()
                term.cmdloop()
            except Exception as e:
                print(e)
                input("Press Enter to continue...")
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt")
                exit()
            
    else:
        term = Terminal()
        autoupdate()
        while True:
            try:
                term.cmdloop()
                break
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt")
                exit()
            