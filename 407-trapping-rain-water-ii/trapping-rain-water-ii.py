class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False]*n for _ in range(m)]
        heap = []
        water_trapped = 0
        
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][0] = visited[i][n-1] = True
            
        for j in range(1, n-1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited[0][j] = visited[m-1][j] = True
            
        while heap:
            height, i, j = heapq.heappop(heap)
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i+di, j+dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    water = max(0, height - heightMap[ni][nj])
                    water_trapped += water
                    heapq.heappush(heap, (max(heightMap[ni][nj], height), ni, nj))
        
        return water_trapped