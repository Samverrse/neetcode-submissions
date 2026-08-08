class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        ans=[]
        for num in nums:
            dic[num]=dic.get(num,0)+1
        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(k):
            ans.append(sorted_dic[i][0])
            
        return ans