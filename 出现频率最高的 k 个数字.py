class Solution(object):
    def topKFrequent(self, nums, k):
        def takefirst(ele):
            return ele[0]
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        s=[[dic[i],i] for i in dic]
        s.sort(key=takefirst,reverse=True)
        p=[i[1] for i in s[0:k]]
        return p
