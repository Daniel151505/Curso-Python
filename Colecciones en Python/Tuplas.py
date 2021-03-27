#Tupla mantiene el orden, pero ya no se puede modificar
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)

#largo de la tupla
print(len(frutas))

#accediendo a un elemento 
print(frutas[2])

#navegación inversa
print(frutas[-1])

#rango
print(frutas[0:2]) #excluyendo el indice 2

#modificar un valor
frutaLista = list(frutas)
frutaLista[1] = "Platanito"
frutas = tuple(frutaLista)
print(frutas)