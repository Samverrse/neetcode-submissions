class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp=0
        main=0
        numss=sorted(set(nums))
        for i in range(len(numss)-1):
            if numss[i+1]-numss[i]==1:
                temp+=1
            else:
                temp=0
            main=max(temp,main)
        return main+1



        
