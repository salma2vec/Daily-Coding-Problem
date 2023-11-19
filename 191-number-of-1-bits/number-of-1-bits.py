class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = format(n, 'b')
        return str(binary).count('1')        