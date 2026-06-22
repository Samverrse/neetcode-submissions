class Solution:
    def reverseString(self, s: List[str]) -> None:
        rev=s[::-1]
        s[:len(rev)]=rev
        return rev


