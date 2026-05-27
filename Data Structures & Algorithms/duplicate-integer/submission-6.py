class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps={}
        for i in nums:
            count=1
            if i not in maps:
                maps[i]= count
            else:
                return True
        return False