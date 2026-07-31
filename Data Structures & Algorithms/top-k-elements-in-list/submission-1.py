class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        bucket=[[] for j in range(len(nums)+1)]
        for i in nums:
            a=nums.count(i)
            if i not in dic.keys():
                dic[i]=a
        for key,value in dic.items():
            bucket[value].append(key)
        result=[]
        for freq in range(len(bucket)-1,0,-1):
            for num in bucket[freq]:
                result.append(num)
                if len(result)==k:
                    return result
        return result