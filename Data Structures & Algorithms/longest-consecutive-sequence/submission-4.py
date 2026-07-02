class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp=0
        main=0
        sorit=sorted(set(nums))
        for i in range(len(sorit)-1):
            if sorit[i+1]-sorit[i]==1:
                temp+=1
            else:
                temp=0
            main=max(temp,main)
        return main+1
