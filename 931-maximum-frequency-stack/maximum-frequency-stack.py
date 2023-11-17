class FreqStack:

    def __init__(self):
        self.set = defaultdict(list)
        self.freq = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.max_freq = max(self.max_freq, self.freq[val])
        self.set[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.set[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.set[self.max_freq]:
            self.max_freq -= 1
        return val