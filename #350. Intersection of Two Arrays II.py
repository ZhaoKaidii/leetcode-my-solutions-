class Solution(object):
    def intersect(self, nums1, nums2):
        dic={}
        for i in nums1:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        s=[]
        for i in nums2:
            if i in dic and dic[i]>0:
                s.append(i)
                dic[i]-=1
        return s
