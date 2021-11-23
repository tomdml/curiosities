import time

class Timer:

    def __init__(self, out='Execution time: {:.6f}s'):
        self.out = out

    def __enter__(self):
        self.time = time.perf_counter()

    def __exit__(self, *err):
        self.newtime = time.perf_counter()
        print(self.out.format(self.newtime - self.time))
