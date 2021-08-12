class Solution(object):
    def findSwapValues(self, array1, array2):
        m=sum(array1)-sum(array2)
        m=sum(array1)-sum(array2)
        if m%2==1 or m==0:
           return []
        else:
           s=set(array2)
           m=m/2
           for n in array1:
                if n-m in s:
                   return [n,n-m]
                   break
           return []
