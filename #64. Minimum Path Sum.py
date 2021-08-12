class Solution(object):
    def minPathSum(self, grid):
        import numpy as np 
        m,n=np.shape(grid)
        dp=np.zeros((m+1,n+1))
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1:
                    dp[i][j]=dp[i][j-1]+grid[i-1][j-1]
                elif j==1 and i!=1:
                    dp[i][j]=dp[i-1][j]+grid[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+grid[i-1][j-1],dp[i][j-1]+grid[i-1][j-1])
        return int(dp[m][n])
