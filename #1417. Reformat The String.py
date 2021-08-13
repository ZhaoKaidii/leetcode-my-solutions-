class Solution(object):
    def reformat(self, s):
        d,f=[],[]
        for i in s:
            if i.isalpha():
                d.append(i)
            else:
                f.append(i)
        if abs(len(d)-len(f))>1:
            return ""
        k=[]
        if len(d)>len(f):
            for i in range(len(f)):
                k.append(d[i])
                k.append(f[i])
            k.append(d[-1])
        elif len(d)<len(f):
            for i in range(len(d)):
                k.append(f[i])
                k.append(d[i])
            k.append(f[-1])
        else:
            for i in range(len(f)):
                k.append(f[i])
                k.append(d[i])
        return "".join(k)
