class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s=0
        for i in stones:
            if i in jewels:
                s+=1
        return s
