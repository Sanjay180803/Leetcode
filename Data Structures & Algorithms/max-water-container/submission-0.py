class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        area=0
        while i<j:
            ar=min(heights[j],heights[i])*(j-i)
            area=max(ar,area)
            if heights[j]<heights[i]:
                j=j-1
            else:
                i=i+1
            
        return area

        

        