import sys

class ProgressBar():
    def __init__(self, progress_total, progress_title='Progress', max_length=20):
        '''
            progress_total should be the length of the array or dictionary.
            max_length must be a number that 100 is divisible by.
        '''
        self.progress_total = progress_total
        self.progress_title = progress_title
        self.max_length = max_length
        self.progress_step = 100 / max_length
        self.progress_current = 0

    def get_prog_str(self, step, percent='0.0'):
        step = int(step)
        bar = "{}{}".format(step * chr(9608), (self.max_length - step) * '-')
        return "{}: |{}| {:.1f}% Done".format(
            self.progress_title, 
            bar, 
            float(percent)
        )

    def next_step(self, cur_index):
        prog_percent = ((cur_index + 1) / self.progress_total) * 100
        prog_per_step = prog_percent // self.progress_step
        if(prog_per_step > self.progress_current):
            self.progress_current = prog_per_step
            sys.stdout.write('\r' + self.get_prog_str(prog_per_step, prog_percent))
            sys.stdout.flush()
            if(prog_per_step == self.max_length):
                sys.stdout.write('\n{} complete!\n'.format(self.progress_title))

# Testing code
# def prog_test():
#     import time

#     content = list(range(100))
#     prog = ProgressBar(len(content), "Converting")

#     for index, _ in enumerate(content):
#         time.sleep(0.1)
#         prog.next_step(index)

# prog_test()