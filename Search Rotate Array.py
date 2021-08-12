class Solution(object):
    def search(self, arr, target):
        arr=arr+[float('inf')]
        if arr[0]>target:
            i=len(arr)-2
            while arr[i]<arr[i+1]:
                if arr[i]==target:
                    while arr[i-1]==arr[i]:
                        i-=1
                    return i
                i-=1
        else:
            arr=[-1]+arr
            i=1
            while i<len(arr) and arr[i-1]<arr[i]:
                if arr[i]==target:
                    return i-1
                i+=1
        return -1
