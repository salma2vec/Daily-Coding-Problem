class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [row.count(1) == 1 for row in mat]
        cols = [col.count(1) == 1 for col in zip(*mat)]
        return sum(r and c and mat[i][j] for i, r in enumerate(rows) for j, c in enumerate(cols))        