class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        @cache
        def dp(a,b,c):
            ans = math.inf
            if c: prev = arr2[b-1]
            else: prev = arr1[a-1]
            if a == len(arr1): return 0
            if prev < arr1[a]: ans = min(ans, dp(a+1,b,0))
            if b < len(arr2) and prev < arr2[b]: ans = min(ans, 1+dp(a+1,b+1,1))
            if b < len(arr2) and prev >= arr2[b]:ans = min(ans, dp(a,b+1,c))
            return ans

        arr2.sort()
        ans = dp(1,0,0)
        if arr2[0] < arr1[0]: ans = min(ans, 1+dp(1,1,1))
        if ans == math.inf: return -1
        return ans