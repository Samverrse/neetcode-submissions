class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp_profit=0
        main_profit=0
        for i in range(len(prices)-1):
            maxPr=max(prices[i+1:])
            if prices[i]<maxPr:
                temp_profit=maxPr-prices[i]
            else:
                temp_profit=0
            main_profit=max(temp_profit,main_profit)
        return main_profit


        
            

