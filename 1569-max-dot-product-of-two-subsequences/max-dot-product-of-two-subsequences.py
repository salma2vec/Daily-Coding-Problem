class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        curr = [float('-inf')] * (n + 1)
        prev = [float('-inf')] * (n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                curr_product = nums1[i-1] * nums2[j-1]
                
                curr[j] = max(curr_product, prev[j], curr[j-1], curr_product + max(0, prev[j-1]))
            
            curr, prev = prev, curr
        return prev[n]        