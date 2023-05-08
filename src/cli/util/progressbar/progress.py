import sys
import os
from colorama import init, Fore, Style

init()  # initialize colorama

class ProgressBar:
    """A progress bar"""
    def __init__(self, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.progress = 0

    def start(self):
        self.progress = 0
        self._update(0)

    def update(self, progress):
        self.progress = progress
        self._update(progress)

    def stop(self):
        self._update(self.total)
        print()

    def _update(self, progress):
        filled_length = int(self.length * progress // self.total)
        percent = f'{100 * (progress / float(self.total)):.1f}'
        bar = ''
        for i in range(self.length):
            if i < filled_length:
                if float(percent) <= 33:
                    bar += Fore.RED + Style.BRIGHT + '█' + Style.RESET_ALL
                elif float(percent) < 66:
                    bar += Fore.YELLOW + Style.BRIGHT + '█' + Style.RESET_ALL
                else:
                    bar += Fore.GREEN + Style.BRIGHT + '█' + Style.RESET_ALL
            else:
                bar += ' '
        output = f'\r{self.prefix} |{bar}| {percent}% {self.suffix},'
        sys.stdout.write(output)
        sys.stdout.flush()


