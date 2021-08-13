class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1=collections.Counter(s1)
        i,j=0,len(s1)-1
        dict2=collections.Counter(s2[i:j])
        while j<len(s2): 
            dict2[s2[j]]+=1         
            if dict1==dict2:
                return True       
            dict2[s2[i]]-=1
            if dict2[s2[i]]==0:
                del dict2[s2[i]]
            i+=1
            j+=1
        return False
