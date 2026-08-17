class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict={}
        for n in nums:
            mydict[n]=mydict.get(n,0)+1
            sorted_dict=dict(sorted(mydict.items()))
        return list(sorted_dict.values())[:k]