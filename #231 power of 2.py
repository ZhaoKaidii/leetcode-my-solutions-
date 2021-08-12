class Solution(object):
    def isPowerOfTwo(self, n):
        return n&(-n)==n if n else False
