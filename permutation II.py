class Solution(object):
    def permuteUnique(self, nums):
        s=[f for f in itertools.permutations(nums)]
        ss=[f for f in set(s)]
        return ss
