class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mini= 1e9
        pro=0
        for price in prices:
            mini=min(mini, price)
            pro=max(pro, price-mini)
        return pro