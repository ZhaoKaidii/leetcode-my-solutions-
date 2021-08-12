class Solution(object):
    def setZeroes(self, matrix):
        m,n=len(matrix),len(matrix[0])
        row,col=[False]*m,[False]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i]=col[j]=True
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j]=0
        return matrix
