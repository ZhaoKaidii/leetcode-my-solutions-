class Solution(object):
    def smallestK(self, arr, k):
        arr.sort()
        return arr[:k]
