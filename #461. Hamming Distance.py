class Solution(object):
    def hammingDistance(self, x, y):
        count=0
        a=[c for c in bin(x)]
        b=[c for c in bin(y)]
        for  i in range(min(len(a)-2,len(b)-2)):
            count=count+int(a[-1]!=b[-1])
            del a[-1]
            del b[-1]
        if len(a)>len(b):
            return count+collections.Counter(a)['1']
        else: 
            return count+collections.Counter(b)['1']
