class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        return (lambda xs: sum(nlargest(k - 1, xs)) - sum(nsmallest(k - 1, xs)))(tuple(map(sum, pairwise(weights))))        