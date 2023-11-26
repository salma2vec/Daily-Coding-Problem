class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        k = 1
        ans = 0
        idx = 1
        if nums[0] != 1:
            ans += 1
            idx = 0
        
        for i in range(idx, len(nums)):
            x = nums[i]
            if k >= n:
                break
            if x <= k + 1:
                k = k + x
            else:
                while k + 1 < x and k < n:
                    k = k + k + 1
                    ans += 1
                k = k + x
        
        while k < n:
            k = k + k + 1
            ans += 1
        
        return ans        