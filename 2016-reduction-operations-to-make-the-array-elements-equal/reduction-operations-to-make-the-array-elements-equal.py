class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        el_counts = Counter(nums)
        sorted_el = sorted(el_counts.items())
        res = sum(i * cnt for i, (num, cnt) in enumerate(sorted_el))
        
        return res