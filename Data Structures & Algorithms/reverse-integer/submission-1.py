class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        new=0
        while x>0:
            l=x%10
            new=new*10+l
            x//=10
        
        new *= sign
        if new < -2**31 or new > 2**31 - 1:
            return 0
        return new