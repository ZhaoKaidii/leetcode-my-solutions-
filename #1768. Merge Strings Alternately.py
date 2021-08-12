class Solution(object):
    def mergeAlternately(self, word1, word2):
        s=""
        m=min(len(word1),len(word2))
        for i in range(m):
            s=s+word1[i]
            s=s+word2[i]
        s=s+word1[m:]+word2[m:]
        return s
