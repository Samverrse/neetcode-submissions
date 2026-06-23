class Solution:
    def reverseWords(self, s: List[str]) -> None:
        ans=[]
        s.split()
        for word in s:
            ans.append(s[-1])
        return ans

        