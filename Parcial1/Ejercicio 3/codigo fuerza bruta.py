class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      max_ganancia = 0
      n = len (prices)

      for i in range (n):
          for j in range (i+1, n):
            ganancia = prices[j] - prices [i]
            if ganancia > max_ganancia:
              max_ganancia = ganancia
      return max_ganancia
      "este ejercicio tiene complejidad O(n²), se utilizan dos for anidados - mejor caso y peor caso O(n²) porque se recorre todo - complejidad espacial O(1) "
