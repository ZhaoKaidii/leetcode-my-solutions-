class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=[0]+heights+[0]
        n,area=len(heights),0
        s=[0]      
        for i in range(1,n):
            while heights[i]<heights[s[-1]]:
                h,w=heights[s.pop()],i-s[-1]-1
                area=max(area,h*w)
            s.append(i)
        return area
