def findContentChildren(g, s):
    
    #O(n log n + m log m)temporal por los 2 sort para las listas.
    #O(1) espacial, usamos i, j, contentos.
    
    # Ordenamos ambas listas
    g.sort()
    s.sort()
    
    i = 0  # puntero para niños
    j = 0  # puntero para galletas
    contentos = 0
    
    # Recorremos mientras haya niños y galletas disponibles
    while i < len(g) and j < len(s):
        # Si la galleta actual satisface al niño actual
        if s[j] >= g[i]:
            contentos += 1   # niño contento
            i += 1           # pasamos al siguiente niño
            j += 1           # usamos esta galleta
        else:
            # Si la galleta no alcanza, seguimos con una más grande
            j += 1
    
    return contentos