class Solution(object):
    def countGoodSubstrings(self, s):
        i,j,ans=0,2,0
        dic=collections.Counter(s[i:j])
        while j<len(s):
            if s[j] in dic:
                dic[s[j]]+=1
            else:
                dic[s[j]]=1
            if len(dic)==3:
                ans+=1
            dic[s[i]]-=1
            if dic[s[i]]<=0:
                del dic[s[i]]
            i+=1
            j+=1
        return ans
