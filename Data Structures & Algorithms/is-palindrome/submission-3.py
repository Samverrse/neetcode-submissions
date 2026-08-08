class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str="".join([ch for ch in s if ch.isalnum()])
        reversed_str=new_str[::-1]
        if new_str.lower()==reversed_str.lower():
            return True
        return False

