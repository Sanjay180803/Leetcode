class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(0, len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=i
            diff=target-nums[i]
            if diff in hashmap and hashmap[diff]!=i:
                return [hashmap[diff], i]
    



        