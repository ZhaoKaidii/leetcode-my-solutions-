class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        s=[n for n in bin(n)]
        ss=collections.Counter(s)
        return ss['1']==1
