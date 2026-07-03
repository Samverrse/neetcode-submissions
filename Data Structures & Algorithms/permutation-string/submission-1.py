class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        rev=[s1[0][::-1]]
        if s1 or rev in s2:
            return True
        return False

        