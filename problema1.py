#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t = input().split()
m = input().split()

#hacemos el orden que nos piden en el problema
s = m+t+m

# le aplicamos un "formato" a los digitos
for i in range(len(s)):
    if s[i].isdigit():
        s[i] = int(s[i])

#imprimimos la tupla
print(tuple(s))
