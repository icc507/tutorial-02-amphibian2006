#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)
t = input().split()
s = []
# invertimos el orden
for i in range(len(t)):
    s.append(t[len(t)-i-1])
# hacemos los numeros enteros
for i in range(len(s)):
    if s[i].isdigit():
        s[i] = int(s[i])
# volvemos a s tupla
r=tuple(s)

print(r)
