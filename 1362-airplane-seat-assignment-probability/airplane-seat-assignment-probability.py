class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 1.0 / n + (n - 2) / n * self.nthPersonGetsNthSeat(n - 1)


        