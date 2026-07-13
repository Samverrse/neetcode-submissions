class Solution:
    def reverse(self, x: int) -> int:
        new=0
        while x>0:
            l=x%10
            new=new*10+l
            x//=10
            
        return new
        