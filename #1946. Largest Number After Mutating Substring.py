class Solution(object):
    def maximumNumber(self, num, change):
        s,f=[d for d in num],False      #1 2             
        for i in range(len(s)): #3
            a=int(s[i])         
            if change[a]>a:     #4
                    s[i]=str(change[a])
                    f=True
            else:
                if f and  change[a]<a:           #5
                        break
        return "".join(s)
