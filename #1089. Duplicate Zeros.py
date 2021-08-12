class Solution(object):
    def duplicateZeros(self, arr):
        i=0
        while i<len(arr):
            if arr[i]==0 and i < len(arr)-1:
                j=len(arr)-1
                while j>i:
                    arr[j]=arr[j-1]
                    j=j-1
                arr[i+1]=0
                i=i+2
            else:
                i=i+1
