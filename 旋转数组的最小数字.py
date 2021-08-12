class Solution(object):
    def minArray(self, numbers):
        left,right=0,len(numbers)-1
        while left<right:
            mid=left+(right-left)//2
            if numbers[right]>numbers[mid]:
                right=mid
            elif numbers[mid]>numbers[right]:
                left=mid+1
            else:
                right-=1
        return numbers[left]
