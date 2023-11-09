class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def update(bit, i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(bit, i):
            count = 0
            while i > 0:
                count += bit[i]
                i -= i & -i
            return count

        if not nums:
            return []

        min_val, max_val = min(nums), max(nums)
        bit = [0] * (max_val - min_val + 2)
        result = []

        for num in reversed(nums):
            index = num - min_val + 1
            smaller_count = query(bit, index - 1)
            result.append(smaller_count)
            update(bit, index)

        return result[::-1]        