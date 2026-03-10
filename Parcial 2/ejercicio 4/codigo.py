class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      "complejidad temporal 0(n) y complejidad espacial 0(n)"
      profit = 0

      for i in range(1, len (prices)):
        if prices[i] > prices[i-1]:
          profit += prices[i] - prices[i-1]
      return profit
