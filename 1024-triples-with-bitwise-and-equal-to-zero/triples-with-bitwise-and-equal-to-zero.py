from collections import defaultdict

class Solution:
    def countTriplets(self, A: List[int]) -> int:
        pairs, N = defaultdict(int), len(A)
        for i in range(N):
            for j in range(N):
                pairs[A[i]&A[j]] += 1
        return sum(pairs[k] if A[i] & k == 0 else 0 for k in pairs for i in range(N))