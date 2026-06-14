class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        for x in strs[0]:
            #prefix+=x
            for word in strs[1:]:
                if word.startswith(prefix+x)==False:
                    return prefix
            prefix+=x