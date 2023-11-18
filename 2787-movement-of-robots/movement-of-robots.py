class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        nums = sorted([i + (ord(c) - 79)// 3 * d for i, c in zip(nums, s)])
        return sum(map(lambda x, y: x * y, nums, range(1 - len(nums), len(nums), 2))) % 1000000007