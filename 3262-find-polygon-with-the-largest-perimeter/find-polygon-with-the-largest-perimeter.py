from collections import defaultdict as dd
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        N=len(nums)
        nums = list(sorted(nums))
        pref_sum = dd(lambda : None )
        p_i = None
        maxPossiblePolygonPermieter = -1
        for i in range(N):
            num = nums[i]
            if(pref_sum[p_i] is not None):
                if( pref_sum[p_i] > num):
                    if(i >= 2):
                        maxPossiblePolygonPermieter=pref_sum[p_i] + num
            pref_sum[i] = num  +  (0 if(pref_sum[p_i] is None) else pref_sum[p_i])

            del pref_sum[p_i]
            p_i = i
        return maxPossiblePolygonPermieter