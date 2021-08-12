class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:       
        ss=[200]
        lis=[]
        final=[0]*len(T)
        for i in range(len(T)):
            if T[i]<=ss[-1]:
                ss.append(T[i])
                lis.append(i)
            else: 
                while T[i]>ss[-1] and len(ss)>1:
                    ss.pop()
                    final[lis[-1]]=(i-lis[-1])
                    lis.pop()
                ss.append(T[i])
                lis.append(i)
        return final
