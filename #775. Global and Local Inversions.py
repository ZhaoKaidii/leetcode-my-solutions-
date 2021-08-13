class Solution(object):
    def isIdealPermutation(self, A):
        N = len(A)
        floor = N
        for i in xrange(N-1, -1, -1):
            floor = min(floor, A[i])
            if i >= 2 and A[i-2] > floor:
                return False
        return True
