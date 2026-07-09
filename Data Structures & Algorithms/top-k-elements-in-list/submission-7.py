class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for n in nums:
            a=nums.count(n)
            if n not in count.keys():
                count[n]=a
        print(count)
        sorted_data = dict(sorted(count.items(), key=lambda item: item[1]))
        return list(reversed(sorted_data.keys()))[:k]
