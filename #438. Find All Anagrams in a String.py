class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic1=collections.Counter(p)
        i,j=0,len(p)-1
        dic2=collections.Counter(s[i:j])
        ans=[]
        while j<len(s):
            dic2[s[j]]+=1
            if dic1==dic2:
                ans.append(i)
            dic2[s[i]]-=1
            if dic2[s[i]]==0:
                del dic2[s[i]]
            i+=1
            j+=1
        return ans
