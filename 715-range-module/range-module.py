class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        new_ranges = []
        inserted = False

        for start, end in self.ranges:
            if end < left:
                new_ranges.append([start, end])
            elif right < start:
                if not inserted:
                    new_ranges.append([left, right])
                    inserted = True
                new_ranges.append([start, end])
            else:
                left = min(left, start)
                right = max(right, end)

        if not inserted:
            new_ranges.append([left, right])

        self.ranges = new_ranges

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.ranges:
            if start <= left and right <= end:
                return True
            elif end >= right:
                break
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_ranges = []

        for start, end in self.ranges:
            if end <= left or start >= right:
                new_ranges.append([start, end])
            else:
                if start < left:
                    new_ranges.append([start, left])
                if end > right:
                    new_ranges.append([right, end])

        self.ranges = new_ranges