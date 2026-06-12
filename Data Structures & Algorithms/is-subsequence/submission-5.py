class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans=[]
        for letter in s:
            if letter not in t:
                return False
        return True
