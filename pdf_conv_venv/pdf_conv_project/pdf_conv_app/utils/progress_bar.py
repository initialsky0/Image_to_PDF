import sys

class ProgressBar():
    def __init__(self, progress_total):
        self.progress_total = progress_total
        self.progress_current = 0

    def start_progress(self):
        sys.stdout.write("[{}]".format(" " * 10))