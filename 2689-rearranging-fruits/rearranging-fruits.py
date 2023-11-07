class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        C1, C2 = Counter(basket1), Counter(basket2)
        abs_min = min(min(basket1), min(basket2))
        h = []
        
        for i in C1.keys():
            if C1[i] > C2[i]:
                diff = C1[i] - C2[i]
                if diff % 2:
                    return -1
                h.extend([i] * (diff // 2))
        
        for i in C2.keys():
            if C2[i] > C1[i]:
                diff = C2[i] - C1[i]
                if diff % 2:
                    return -1
                h.extend([i] * (diff // 2))
        
        heapq.heapify(h)
        n, ans = len(h), 0
        for _ in range(n // 2):
            ans += min(2 * abs_min, heapq.heappop(h))
        
        return ans        