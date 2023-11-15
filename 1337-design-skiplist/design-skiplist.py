class Skiplist:

    def __init__(self):
        self.skiplist = defaultdict(int)

    def search(self, target: int) -> bool:
        return self.skiplist[target] > 0

    def add(self, num: int) -> None:
        self.skiplist[num] += 1

    def erase(self, num: int) -> bool:
        if self.skiplist[num] > 0:
            self.skiplist[num] -= 1
            return True
        return False
