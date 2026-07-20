class Solution:
    def isPalindrome(self, x: int) -> bool:
        new=0
        while x>0:
            l=x%10
            new=new*10+l
            l//=10
            if x==new:
                return True
        return False
        