class Solution(object):
    def getLucky(self, s, k):
        dic={}
        for i in range(97,124):
            a=chr(i)
            if a not in dic:
                dic[a]=str(i-96)
        c=""
        for i in s:
            c=c+dic[i]
        while k>0 and len(c)>1:
            d=0
            for i in c:
                d+=int(i)
                
            c=str(d)
            k-=1
        return int(c)
