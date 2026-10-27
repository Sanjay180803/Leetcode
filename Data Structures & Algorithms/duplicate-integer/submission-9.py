class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps={}
        for i in nums:
            count=0
            if i not in maps.keys():
                maps[i]= count+1
            else:
                return True
        return False

                