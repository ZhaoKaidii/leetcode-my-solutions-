class Solution(object):
    def convertInteger(self, A, B):
        return collections.Counter(bin((A & 0xffffffff)^(B & 0xffffffff)))['1']
