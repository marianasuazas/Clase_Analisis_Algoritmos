"""
Complejidad temporal O(n)
Complejidad espacial O(1)
Se recorre la cadena una sola vez y cada vez que una piedra es igual a la anterior se suma 1 al contador para contar cuántas deben eliminarse.
"""
n = int(input())
s = input()

count = 0

for i in range(1, n):
    if s[i] == s[i - 1]:
        count += 1

print(count)
