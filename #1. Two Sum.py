class Solution(object):
    def twoSum(self, nums, target):
        hashtable=dict()
        for i, nums in enumerate(nums):
            if target-nums in hashtable:
                return [hashtable[target-nums],i]
            hashtable[nums]=i 
        return []
