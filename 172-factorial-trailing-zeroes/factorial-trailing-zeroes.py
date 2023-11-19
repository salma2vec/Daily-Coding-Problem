class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero = 0
        five = 5

        while n//five:
            zero+=n//five
            five*=5
        return zero        