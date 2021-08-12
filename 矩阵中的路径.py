class Solution(object):
    def exist(self, board, word):
        m,n,i,f=len(board),len(board[0]),1,False
        direction=[[1,0],[-1,0],[0,1],[0,-1]]      
        check=[[0]*n for _ in range(m)]
        def search(board,r,c,i,f):
            d=i
            if i==len(word):
                return True        
            for dx,dy in direction:
                nr,nc=r+dx,c+dy
                if i<len(word) and 0<=nr<m and 0<=nc<n and board[nr][nc]==word[i]:
                    if check[nr][nc]==1:
                        continue
                    i+=1
                    check[nr][nc]=1
                    f|=search(board,nr,nc,i,f)
                    if f:
                        return True
                    else:
                        i=d
                        check[nr][nc]=0
            return f
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
