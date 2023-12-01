# Question similar to "Path with Minimum Effort" 
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        r=len(grid)
        c=len(grid[0])

        cache=[[math.inf for _ in range(c)] for _ in range(r)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        minheap=[(grid[0][0],0,0)]

        cache[0][0] = grid[0][0]

        while minheap:
            elevation,i,j=heapq.heappop(minheap)

            if i==(r-1) and j==(c-1):
                return elevation

            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                
                if 0 <= nx < r and 0 <= ny < c:

                    new_elevation=max(grid[nx][ny],elevation)

                    if new_elevation < cache[nx][ny]:
                        cache[nx][ny] = new_elevation
                        heappush(minheap, (new_elevation, nx, ny))

            
        