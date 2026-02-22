class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        Complejidad temporal O(n)
        Complejidad espacial O(n)
        Se soluciona contando las letras de la primera palabra y restando las de la segunda, si coinciden retorna true.
        """
        if len(s) != len(t):
            return False

        dic_s = {}

        for letra in s:
            if letra in dic_s:
                dic_s[letra] += 1
            else:
                dic_s[letra] = 1

        for letra in t:

            if letra not in dic_s:
                return False

            dic_s[letra] -= 1

            if dic_s[letra] < 0:
                return False

        return True 
