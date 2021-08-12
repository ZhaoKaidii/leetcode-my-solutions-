class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        t = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                t[i][j]=matrix[m-j-1][i]
        matrix[:]=t
