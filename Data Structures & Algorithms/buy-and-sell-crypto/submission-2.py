class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        purchase, sale = 0, 1
        maxProfit = 0

        while(sale < len(prices)):
            if(prices[sale] > prices[purchase]):
                maxProfit = max(maxProfit, prices[sale] - prices[purchase])

            else:
                purchase = sale
                
            sale += 1

        return maxProfit