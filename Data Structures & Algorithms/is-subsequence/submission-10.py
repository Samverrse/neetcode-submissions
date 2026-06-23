class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for str1 in s:
            if str1 not in t:
                return False
        return True

        