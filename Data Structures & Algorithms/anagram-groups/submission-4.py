class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sjoined="".join(sorted(s))
            res[sjoined].append(s)
        return list(res.values())
