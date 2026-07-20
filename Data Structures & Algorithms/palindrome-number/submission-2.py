class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x==0:
            return True
        new=0
        original=x
        while x>0:
            l=x%10
            new=new*10+l
            x//=10
        if original==new:
            return True
        return False
        