class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        prev = float('-inf')
        
        for num in nums:
            if num <= prev:
                moves += prev - num + 1
                prev += 1
            else:
                prev = num
        
        return moves