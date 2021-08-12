class Solution(object):
    def permutation(self, s):
        p=list("".join(ss) for ss in itertools.permutations(s))
        pp=[f for f in set(p)]
        return pp
