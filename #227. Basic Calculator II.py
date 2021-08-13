class Solution:
    def calculate(self, s: str) -> int:
        def num(s,i):
            d=c=0
            while i<len(s):
                if s[i]==" " and c<1:
                    i+=1
                    c+=1
                    continue               
                if s[i].isalnum():
                    d=d*10+int(s[i])
                    i+=1
                else:
                    break
            return d,i
        g=[]
        i=0
        sig=1
        while i<len(s):
            if s[i].isalnum():
                dd,i=num(s,i)
                g.append(sig*dd)
                continue
            else:
                if s[i]=="+":
                    sig=1
                    i+=1
                elif s[i]=="-":
                    sig=-1
                    i+=1
                elif s[i]=="*":
                    ddd,i=num(s,i+1)
                    g[-1]*=ddd
                elif s[i]=="/":
                    ddd,i=num(s,i+1)
                    g[-1]=int(g[-1]/ddd)
                else:
                    i+=1
        return sum(g)
