class Solution:
    def multiply(self, A: int, B: int) -> int:
        r=0
        while A:
            if A%2:
                r+=B
            A>>=1
            B<<=1
        return r
