import functools
from math import log2

@functools.lru_cache(None)
def bto0(b):
    return (1 << b + 1) - 1

@functools.lru_cache(None)
def nto0(n):
    if n == 0:
        return 0

    b1 = int(log2(n))
    return bto0(b1) - nto0(n - (1 << b1))

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return nto0(n)

        