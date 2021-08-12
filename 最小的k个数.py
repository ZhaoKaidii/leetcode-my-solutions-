class Solution(object):
    def getLeastNumbers(self, arr, k):
        arr.sort(reverse=False)
        return arr[0:k]
