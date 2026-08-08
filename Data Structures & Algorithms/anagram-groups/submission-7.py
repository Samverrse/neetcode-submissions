class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sf="".join(sorted(s))
            res[sf].append(s)
        return list(res.values())