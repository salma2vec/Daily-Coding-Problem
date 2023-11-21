class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def reverse_num(n):
            return int(str(n)[::-1])

        nice_pairs = 0
        seen = {} 

        for num in nums:
            diff = num - reverse_num(num)
            nice_pairs += seen.get(diff, 0)
            seen[diff] = seen.get(diff, 0) + 1

        return nice_pairs % (10**9 + 7)
        