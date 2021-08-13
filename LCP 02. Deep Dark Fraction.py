class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        n,m=0,1
        for i in cont[::-1]:
            n,m=m,(m*i+n)
        return [m,n]
