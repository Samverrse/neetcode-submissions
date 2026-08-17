class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        ansf=[]
        for lists in points:
            a,b=lists
            dist=(a**2)+(b**2)
            ans.append((dist,lists))
        ans.sort()
        for i in range(k):
            ansf.append(ans[i][1])
        return ansf



            