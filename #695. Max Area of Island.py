class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        def search(grid,r,c,B):
            grid[r][c]=0
            for dx,dy in direction:
                nr=r+dx
                nc=c+dy
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    B.append(1)
                    search(grid,nr,nc,B)
        ff=0
        for r in range(m):
            for c in range(n): 
                if grid[r][c]==1:
                    B=[1]
                    search(grid,r,c,B)
                    ff=max(ff,len(B))
            
        return ff
