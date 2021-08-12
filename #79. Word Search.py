class Solution(object):
    def exist(self, board, word):
        m,n=len(board),len(board[0])
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        check=[[0]*n for _ in range(m)]
        def search(board,r,c,i,f):
            d=i
            if i==len(word):
                check[r][c]=0
                return True        
            for dx,dy in direction:
                nr=r+dx
                nc=c+dy
                if i<len(word) and 0<=nr<m and 0<=nc<n and board[nr][nc]==word[i]:
                    if check[nr][nc]==1:
                        continue
                    i+=1
                    check[nr][nc]=1
                    f|=search(board,nr,nc,i,f)
                    if f==True:
                        return True
                    else:
                        i=d
                        check[nr][nc]=0
            return f
        i=1
        f=False
        for r in range(m):
            for c in range(n): 
                if board[r][c]==word[0]:
                    check[r][c]=1
                    f|=search(board,r,c,i,f)
                    i=1      
                    if f:
                        return True
                    else:
                        check[r][c]=0
        return f
