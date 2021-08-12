class Solution(object):
    def reverseLeftWords(self, s, n):
        return s[n:]+s[0:n]
