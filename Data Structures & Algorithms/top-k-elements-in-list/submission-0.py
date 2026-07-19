class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict={}
        for n in nums:
            mydict[n]=mydict.get(n,0)+1
            sortit=dict(sorted(mydict.items(),key=lambda x:x[1],reverse=True))
            first_k=list(sortit.keys())[:k]
        return first_k