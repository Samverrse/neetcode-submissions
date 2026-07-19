class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp=0
        main=0
        for i in range(len(prices)-1):
            mm=max(prices[i+1:])
            if prices[i]<mm:
                temp=mm-prices[i]
            else:
                temp=0
            main=max(temp,main)
        return main 


        
            

