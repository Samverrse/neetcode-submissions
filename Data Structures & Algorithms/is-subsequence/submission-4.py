class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans=[]
        for letter in t:
            if letter in s:
                ans.append(letter)
                if ans==s:
                    return True
        return False
