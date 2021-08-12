class Solution(object):
    def findDuplicate(self, nums):
        return (sum(nums)-sum(set(nums)))/(len(nums)-len(set(nums)))
