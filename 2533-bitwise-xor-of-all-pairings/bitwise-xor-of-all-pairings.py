class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        return reduce(xor, nums1 * (len(nums2) & 1) + nums2 * (len(nums1) & 1), 0)
