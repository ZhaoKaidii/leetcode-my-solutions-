class Solution:
    def subarraySum(self, nums, k):
        dic = {0: 1}
        ret = pre_sum = 0
        for i in nums:
            pre_sum += i
            ret += dic.get(pre_sum - k,0)
            if pre_sum not in dic:
                dic[pre_sum]=1
            else:
                dic[pre_sum] += 1
        return ret
