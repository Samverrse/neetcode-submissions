class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1="".join([char for char in s if char.isalnum()])
        rev=s1[::-1]
        print(rev)
        if s1.lower()==rev.lower():
            return True
        return False        