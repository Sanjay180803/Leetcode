class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1=set(nums)
        longest=0

        for num in nums1:
            if num-1 not in nums1:
                curr=num
                count=1
                while curr+1 in nums1:
                    curr=curr+1
                    count=count+1
                longest=max(count,longest)
        return longest
            

      
    
