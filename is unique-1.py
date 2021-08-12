class Solution:
    def isUnique(self, astr: str) -> bool:
        n=len(set(astr))
        m=len(astr)
        return n==m
