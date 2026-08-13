class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        while sum!=0:
            l=n%10
            sum+=l**2
            n//=10
        return True
        