class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            index1= nums.index(i)
            if target-i in nums[index1+1:]:
                return [index1,nums.index(target-i,index1+1)]