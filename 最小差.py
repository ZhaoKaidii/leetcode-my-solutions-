class Solution(object):
    def smallestDifference(self, a, b):
        a.sort()
        b.sort()
        i,j,r=0,0,2147483647
        while (i<len(a)) and (j<len(b)):
            r=min(r,abs(a[i]-b[j]))
            if a[i]>b[j]:j=j+1                 
            else: i=i+1   
        return r
