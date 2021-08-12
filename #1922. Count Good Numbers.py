class Solution(object):
    def countGoodNumbers(self, n):
        return (pow(4,n//2,10**9+7)*pow(5,n-n//2,10**9+7))%(10**9+7)
