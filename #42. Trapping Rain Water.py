class Solution(object):
    def trap(self, height):
        if len(height)<3:
            return 0
        c,i,j=0,0,len(height)-1
        R,L=height[-1],height[0]
            R=max(R,height[j])
            L=max(L,height[i])
            if R>L:
                c+=L-height[i]
                i+=1
            else:
                c+=R-height[j]
                j-=1
        return c
