class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic={}
        ans,i,t=0,0,0
        while i < len(s):
            if s[i] not in dic:
                dic[s[i]]=1
                ans=max(ans,len(dic))
            else:
                while s[i] in dic:
                    del dic[s[t]]
                    t+=1
                dic[s[i]]=1
            i+=1
        return ans
