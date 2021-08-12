class Solution(object):
    def numIslands(self, grid):
        m,n=len(grid),len(grid[0]) 
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        islands=0
        def search(r,c):
            grid[r][c]="0"
            for dx,dy in direction:
                nr=r+dx
                nc=c+dy
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]=="1":
                    search(nr,nc)
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    search(r,c)
                    islands+=1
        return islands
