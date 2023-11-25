class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        A = B = 0
        for x in nums:
            B += x

        ans = [0] * n
        i = 0
        for x in nums:
            ans[i] = (2 * i - n) * x + B - A
            A += x
            B -= x
            i += 1
        return ans

        