class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        result = ['1'] * length
        for i, binary_str in enumerate(nums):
            result[i] = chr(ord('1') - ord(binary_str[i]) + ord('0'))
        return "".join(result)   