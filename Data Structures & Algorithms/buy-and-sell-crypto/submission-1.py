class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        maxP=0
        for i in range(len(prices)-1):
            mm=max(prices[i+1:])
            if prices[i]<mm:
                profit=mm-prices[i]
            else:
                profit=0
            maxP=max(profit,maxP)
        return maxP
            

            

