import sys
import os
from colorama import init, Fore, Style

init()  # initialize colorama

class ProgressBar:
    """A progress bar"""
    def __init__(self, total, prefix='', suffix=''):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = 1
        self.length = 100
        self.progress = 0

    def update(self, progress):
        self.progress = progress + 1
        percent = round(100.0 * self.progress / float(self.total), 1)
        filled_length = int(round(self.length * self.progress / float(self.total)))
        bar = ''
        for i in range(self.length):
            if i < filled_length:
                if percent <= 33:
                    bar += Fore.RED + Style.BRIGHT + '█' + Style.RESET_ALL
                elif percent < 66:
                    bar += Fore.YELLOW + Style.BRIGHT + '█' + Style.RESET_ALL
                else:
                    bar += Fore.GREEN + Style.BRIGHT + '█' + Style.RESET_ALL
            else:
                bar += ' '
        output = f'\r{self.prefix} |{bar}| {percent}% {self.suffix}'
        sys.stdout.write(output)
        sys.stdout.flush()
        if progress == self.total:
            print()
