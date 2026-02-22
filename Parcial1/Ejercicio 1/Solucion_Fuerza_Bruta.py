class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        Complejidad temporal O(n^2)
        Complejidad espacial O(n)
        por cada letra de la palabra s se busca y elimina en una lista que contiene las letras de la palabra t.
        """
        if len(s) != len(t):
            return False

        lista_t =list(t)

        for letra in s:
            
            if letra not in lista_t:
                return False

            lista_t.remove(letra)

        return True
