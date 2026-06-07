class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        for word in strs:
            group=[]
            for wor in strs:
                if sorted(word)==sorted(wor):
                    group.append(wor)
            if group not in ans:
                ans.append(group)
        return ans
