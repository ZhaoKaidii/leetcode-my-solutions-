class Solution(object):
    def searchMatrix(self, matrix, target):
        c=False
        if len(matrix)==0 or len(matrix[0])==0:
            c=False
        else:
            import numpy as np 
            m,n=np.shape(matrix)
            for i in range(m):
                if target<=matrix[i][n-1]:
                    for j in range(n):
                        c= c or(target==matrix[i][j])
        return c
