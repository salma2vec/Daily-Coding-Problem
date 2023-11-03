class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        
        count = [0] * (max_num + 1)
        for num in nums:
            count[num] += num
        
        prev_max = 0
        curr_max = 0
        
        for i in range(max_num + 1):
            temp = curr_max
            curr_max = max(prev_max + count[i], curr_max)
            prev_max = temp
        
        return curr_max        