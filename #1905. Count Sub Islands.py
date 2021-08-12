class Solution(object):
    def countSubIslands(self, grid1, grid2): 
        m,n=len(grid1),len(grid1[0])  
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        islands=0
        def search(grid,r,c):
            grid[r][c]=0
            for dx,dy in direction:
                nr=r+dx
                nc=c+dy
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    search(grid,nr,nc)
        for r in range(m):
            for c in range(n):
                if grid2[r][c]==1 and grid1[r][c]==0:
                    search(grid2,r,c)
        for r in range(m):
            for c in range(n):
                if grid2[r][c]==1:
                    search(grid2,r,c)
                    islands+=1
        return islands
