class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n,s,r=len(matrix),len(matrix[0]),[],[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    s.append(i)
                    r.append(j)
        s=set(s)
        r=set(r)
        for i in range(m):
            for j in range(n):
                if (i in s) or (j in r):
                    matrix[i][j]=0
        return matrix
