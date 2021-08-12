class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m,n=len(land),len(land[0])
        direction=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        def search(land,r,c,B):
            land[r][c]=1
            for dx,dy in direction:
                nr=r+dx
                nc=c+dy
                if 0<=nr<m and 0<=nc<n and land[nr][nc]==0:
                    B.append(1)
                    search(land,nr,nc,B)
        ff=[]
        for r in range(m):
            for c in range(n): 
                if land[r][c]==0:
                    B=[1]
                    search(land,r,c,B)
                    ff.append(len(B))   
        ff.sort()   
        return ff
