class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(0, len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=i
            num = target - nums[i]
            if (num in hashmap) and (i!=hashmap[num]):
                return [hashmap[num],i]
    



        