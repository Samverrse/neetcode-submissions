class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it=iter(t)
        for ch in s:
            if ch not in t:
                return False
        return True

        