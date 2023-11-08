class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_values = []
        window = deque()
        
        for i in range(len(nums)):
            while window and window[0] < i - k + 1:
                window.popleft()
            
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            window.append(i)
            
            if i >= k - 1:
                max_values.append(nums[window[0]])
        
        return max_values        