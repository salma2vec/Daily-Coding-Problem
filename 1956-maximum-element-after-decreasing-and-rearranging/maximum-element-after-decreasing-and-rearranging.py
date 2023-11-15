class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        m = 0
        for v in arr:
            if v > m:
                m += 1
        return m        