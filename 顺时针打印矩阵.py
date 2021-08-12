class Solution(object):
    def spiralOrder(self, matrix):
        if matrix==[]:
            return []
        m,n,i,f=len(matrix),len(matrix[0]),0,[]
        check=[[0]*n for _ in range(m)]
        def layer(i,f):
            for j in range(i,n-i):
                if check[i][j]==1:
                    continue
                f.append(matrix[i][j])
                check[i][j]=1
            for j in range(i+1,m-i): 
                if check[j][n-i-1]==1:
                    continue
                f.append(matrix[j][n-i-1])
                check[j][n-i-1]=1
            for j in range(n-i-2,i-1,-1):
                if check[m-i-1][j]==1:
                    continue
                f.append(matrix[m-i-1][j])
                check[m-i-1][j]==1
            for j in range(m-i-2,i,-1):
                if check[j][i]==1:
                    continue
                f.append(matrix[j][i])
                check[j][i]=1
        num_of_layer=(min(m,n)+1)//2
        while i<num_of_layer:
            layer(i,f)
            i+=1
        return f
