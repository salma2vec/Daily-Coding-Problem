class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        two = float('-inf')

        for num in reversed(nums):
            if num < two:
                return True
            while stack and num > stack[-1]:
                two = stack.pop()
            stack.append(num)

        return False        