class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = set()
        prev = 0
        for x in accumulate(nums):
            if x % k in s: return True
            s.add(prev)
            prev = x % k
        return False 