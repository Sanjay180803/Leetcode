class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_list={}
        op=[]
        for i in strs:
            if tuple(sorted(i)) not in s_list.keys():
                l=[]
                l.append(i)
                s_list[tuple(sorted(i))]=l
            else:
                s_list[tuple(sorted(i))].append(i)
        for l in s_list.values():
            op.append(l)
        return op