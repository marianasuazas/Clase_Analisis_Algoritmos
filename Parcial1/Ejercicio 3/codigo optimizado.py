class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
      min_precio = prices[0]
      max_ganancia = 0

      for i in range (1, len(prices)):
        if prices[i] < min_precio:
          min_precio = prices[i]
        else:
          max_ganancia = max(max_ganancia, prices[i] - min_precio)
      return max_ganancia
      "complejidad temporal, mejor y peor caso O(n) se recorre solo una vez - complejidad espacial O(1)"
