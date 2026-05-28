class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        bucket=[[] for i in range(len(nums) + 1) ]
        for i in range (0, len(nums)):
            if nums[i] not in dic:
                count =0
                count +=1
                dic[nums[i]] = count
            else:
                dic[nums[i]]+=1
        for key, value in dic.items():
            bucket[value].append(key)
        result = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result