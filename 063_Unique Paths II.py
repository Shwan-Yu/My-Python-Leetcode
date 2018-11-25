class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: continue
                if i == 0 and j == 0: dp[i][j] = 1
                elif i == 0: dp[i][j] = dp[i][j-1]
                elif j == 0: dp[i][j] = dp[i-1][j]
                else: dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
