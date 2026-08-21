class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall=0
        r_wall=0
        n =len(height)
        max_left=[0]*n
        max_rt=[0]*n
        for i in range(n):
            j=-i-1
            max_left[i]=l_wall
            max_rt[j]=r_wall
            l_wall=max(l_wall, height[i])
            r_wall=max(r_wall,height[j])
        tot=0
        for i in range(n):
            tot=tot+max(0,min(max_left[i],max_rt[i])-height[i])
        return tot
        