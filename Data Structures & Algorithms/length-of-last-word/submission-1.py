class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        striped=s.strip()
        s1=striped.split()
        return len(s1[-1])

        