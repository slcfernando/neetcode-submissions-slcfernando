class MinStack:
    def __init__(self):
        self.arr = []
        self.minima = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.minima:
            self.minima.append(val)
        else:
            self.minima.append(min(val, self.getMin()))

    def pop(self) -> None:
        self.arr.pop()
        self.minima.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minima[-1]