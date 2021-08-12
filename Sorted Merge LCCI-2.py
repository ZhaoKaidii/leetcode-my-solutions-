class Solution(object):
    def merge(self, A, m, B, n):
        for i in range(len(B)):
            A[m+i]=B[i]
        A.sort()
        return A
