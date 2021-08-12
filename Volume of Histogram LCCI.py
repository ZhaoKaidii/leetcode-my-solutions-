class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        c,i,j=0,0,len(height)-1
        r,l=height[-1],height[0]
        while i<=j:
            r=max(height[j],r)
            l=max(height[i],l)
            if r>l:
               c+=l-height[i]
               i+=1
            else:
                c+=r-height[j]
                j-=1
        return c
