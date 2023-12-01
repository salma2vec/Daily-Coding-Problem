class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        index = defaultdict(list)
        # Index Hashing
        for i in range(len(ring)):
            index[ring[i]].append(i)
        @lru_cache
        def dfs(r, k):
            if k == len(key):
                return 0
            ans = float("inf")
            for idx in index[key[k]]:
                clockwise_movement_cost = abs(idx - r) + 1
                anticlockwise_movement_cost = len(ring) - abs(idx - r) + 1
                ans = min(ans, min(clockwise_movement_cost, anticlockwise_movement_cost) + dfs(idx, k + 1))
            return ans

        return dfs(0, 0)
        