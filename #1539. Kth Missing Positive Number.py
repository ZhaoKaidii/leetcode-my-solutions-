class Solution(object):
    def findKthPositive(self, arr, k):
        n=len(arr)
        n=arr[-1]-n
        if n<k:
            return arr[-1]+k-n
        if arr[0]>k:
            return k
        a,b=0,len(arr)
        while b-a>1:
            c=(a+b)//2
            if k<=(arr[c]-c-1):
                b=c
            else:
                a=c
        return k-(arr[a]-a-1)+arr[a]
