class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = 0
        glasses = [poured]  # Store the amount of champagne in each glass of the current row

        while row < query_row:
            next_glasses = [0.0] * (row + 2)

            for i in range(len(glasses)):
                excess = max(0, (glasses[i] - 1) / 2)
                next_glasses[i] += excess
                next_glasses[i + 1] += excess

            glasses = next_glasses
            row += 1

        return min(1.0, glasses[query_glass])         