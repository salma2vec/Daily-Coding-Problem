class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        s = sum(cost)
        dp = [s for _ in range(n+1)]
        for i in range(n):
            time[i] += 1 
        dp[0] = 0
        for i in range(n):
            for x in range(n-1,-1,-1):
                y = min(x+time[i],n) 
                dp[y] = min(dp[y],dp[x]+cost[i])
        return dp[-1]         