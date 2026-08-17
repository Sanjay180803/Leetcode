class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range (0, len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                 continue
            l=[]
            j,k=i+1, len(nums)-1
            while j<k:
                if nums[j]+nums[k] == -nums[i]:
                    l=[nums[i],nums[j],nums[k]]
                    res.append(l)
                    j,k=j+1,k-1 
                    while j<k and nums[j]==nums[j-1]:
                        j=j+1
                    while j<k and nums[k]==nums[k+1]:
                        k=k-1
                elif nums[j]+nums[k] < -nums[i]:
                    j=j+1
                else:
                    k=k-1
        return res
            



