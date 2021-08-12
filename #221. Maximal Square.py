class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix)==0:
            return 0
        import numpy as np
        ans,m,n=0,len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in  range(n):
                if matrix[i][j]=='0':
                    continue
                else:
                    if m==0 or n==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
        ans=max(ans,np.max(dp))
        return ans*ans
