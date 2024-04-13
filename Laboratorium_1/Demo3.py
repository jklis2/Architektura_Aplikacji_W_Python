class Fibonacci:
    def __init__(self,end):
        self.previous = 0
        self.current = 1
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.end:
            next_ = self.current
            self.previous, self.current = self.current, self.previous + self.current
            return next_
        else:
            raise StopIteration
fibon=Fibonacci(1e6)
for f in fibon:
    print(f)