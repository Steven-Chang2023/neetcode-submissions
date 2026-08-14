class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.cur_min = float('inf')
    def push(self, val: int) -> None:
        self.s1.append(val)
        self.s2.append(self.getMin())
        self.cur_min = min(val, self.cur_min)
    def pop(self) -> None:
        cur_val = self.s1.pop()
        old_min = self.s2.pop()
        self.cur_min = old_min

    def top(self) -> int:
        return self.s1[len(self.s1) - 1]

    def getMin(self) -> int:
        return self.cur_min
