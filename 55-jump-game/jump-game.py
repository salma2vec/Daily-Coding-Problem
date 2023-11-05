class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # Initialize the farthest position reached
        
        for i in range(len(nums)):
            if i > max_reach:
                return False  # If you can't reach the current position, return False
            max_reach = max(max_reach, i + nums[i])  # Update the farthest position
            
            
        return True  # If you reach the end, return True        