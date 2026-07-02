class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1="".join([ch for ch in s if ch.isalnum()])
        rev=s1[::-1]
        if s1.lower()==rev.lower():
            return True
        return False
