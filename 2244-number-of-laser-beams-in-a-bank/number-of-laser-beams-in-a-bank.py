class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        return sum(map(prod, pairwise(filter(int, (r.count('1') for r in bank)))))
        