class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memmap = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in memmap:
                memmap[key] = []

            memmap[key].append(word)

        return list(memmap.values())

        


        
            


        