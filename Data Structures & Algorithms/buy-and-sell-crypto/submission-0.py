class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mainP=0
        tempP=0
        for i in range(len(prices)-1):
            mm=max(prices[i+1:])
            if prices[i]<mm:
                tempP=mm-prices[i]
            else:
                tempP=0
            mainP=max(tempP,mainP)
        return mainP

        