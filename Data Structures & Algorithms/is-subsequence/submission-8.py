class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it=iter(t)
        for letter in s:
            if letter not in it:
                return False
        return True
