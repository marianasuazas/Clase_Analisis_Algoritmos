class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        Complejidad temporal O(n^2), porque en cada iteración se realiza una busqueda y eliminación.
        Complejidad espacial O(n), por la lista que se crea para agregar las letras de t.
        """
        if len(s) != len(t):
            return False

        lista_t =list(t)

        for letra in s:
            
            if letra not in lista_t:
                return False

            lista_t.remove(letra)

        return True
