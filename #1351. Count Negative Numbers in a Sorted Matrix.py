class Solution(object):
    def countNegatives(self, grid):
        c=0
        i,j,m,n=0,0,len(grid),len(grid[0])
        while i<m:
            while j<n:
                if grid[i][j]<0:
                    c=c+(m-i)*(n-j)
                    n=j
                    j=0
                    continue
                j+=1
            i+=1
            if j==n:
                j=0
                continue          
        return c
