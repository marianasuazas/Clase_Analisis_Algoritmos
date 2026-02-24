"““Complejidad: O(2^n · n) porque se generan 2^n combinaciones y para cada una se recorren hasta n elementos; mejor y peor caso O(2^n · n); espacio O(n)."
def fuerza_bruta(n, s):
    min_eliminadas = n
 
    for mask in range(1 << n):
        nueva = []
 
        for i in range(n):
            if mask & (1 << i):
                nueva.append(s[i])
 
        valido = True
        for i in range(1, len(nueva)):
            if nueva[i] == nueva[i - 1]:
                valido = False
                break
 
        if valido:
            eliminadas = n - len(nueva)
            min_eliminadas = min(min_eliminadas, eliminadas)
 
    return min_eliminadas
 
 
n = int(input().strip())
s = input().strip()
 
print(fuerza_bruta(n, s))
