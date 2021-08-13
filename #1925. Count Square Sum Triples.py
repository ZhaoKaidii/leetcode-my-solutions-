class Solution:
    def countTriples(self, n: int) -> int:
        d=0
        for i in  range(1,n+1):
            f=[]
            a=int((i/2)*(2**0.5))+1
            b=int((i/2)*(2**0.5))
            while b>0 and a<i:
                if (a**2)+(b**2)==i**2:
                    f.append([a,b,i])
                    f.append([b,a,i])
                if a**2+b**2>i**2:
                    b-=1
                    continue
                if a**2+b**2<n**2:
                    a+=1
                    continue
                a+=1
                b-=1
            d+=len(f)
        return d
