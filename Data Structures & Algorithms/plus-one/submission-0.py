class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=int("".join(map(str,digits)))+1
        result = list(map(int, str(n)))
        return result


        