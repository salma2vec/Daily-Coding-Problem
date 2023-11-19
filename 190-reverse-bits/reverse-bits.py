class Solution:
    def reverseBits(self, n: int) -> int:
        outp = 0
        for _ in range(31):
            outp += n%2
            outp <<= 1
            n >>= 1
        return outp + n        