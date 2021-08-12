class Solution(object):
    def findKthPositive(self, arr, k):
        return list(set(range(2001)) - set(arr))[k]
