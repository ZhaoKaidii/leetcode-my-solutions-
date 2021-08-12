class Solution:
    def reverse(self, x: int) -> int:
        sig=1 if x>0 else -1
        s=str(abs(x))
        ans=int(s[::-1])*sig
        return ans if ans in range(-2**31,2**31) else 0
