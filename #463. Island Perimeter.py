class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        def search(grid,r,c,B):
            #将已经使用过的陆地部分置为2，用于区分未使用的陆地和水域。便于后面判定衰减
            grid[r][c]=2
            aa=(r+1)<m and grid[r+1][c]!=0
            bb=(r-1)>=0 and grid[r-1][c]!=0
            cc=(c+1)<n and grid[r][c+1]!=0
            dd=(c-1)>=0 and grid[r][c-1]!=0
            #定义一下衰减，假如一块陆地周围有陆地，那么其对边长的贡献也应该对应的减少
            ded=int(aa)+int(bb)+int(cc)+int(dd)
            B.append(4-ded)
            for dx,dy in direction:
                nr=r+dx
                nc=c+dy
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:              
                    search(grid,nr,nc,B)
        ff=0
        for r in range(m):
            for c in range(n): 
                if grid[r][c]==1:
                    B=[]
                    search(grid,r,c,B)
                    ff=max(ff,sum(B))  
        return ff
