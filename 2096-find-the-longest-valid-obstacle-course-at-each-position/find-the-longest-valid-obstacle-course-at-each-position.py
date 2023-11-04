class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        dp = [0] * n
        dp[0] = 1
        lis = [obstacles[0]]

        for i in range(1, n):
            if obstacles[i] >= lis[-1]:
                lis.append(obstacles[i])
                dp[i] = len(lis)
            else:
                left, right = 0, len(lis) - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if lis[mid] <= obstacles[i]:
                        left = mid + 1
                    else:
                        right = mid
                lis[left] = obstacles[i]
                dp[i] = left + 1

        return dp