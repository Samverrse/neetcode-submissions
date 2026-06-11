class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
       sort1=sorted(arr)
       rep=sort1[-1].replace(-1)
       return rep