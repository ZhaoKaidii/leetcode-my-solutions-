class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        left=right=c=0
        while i<j:
            left=max(left,height[i])
            right=max(right,height[j])
            c=max(c,min(left,right)*(j-i))
            if left>=right:
                j-=1
            else:
                i+=1
        return c
