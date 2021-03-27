#un diccionario esta compuesto de llave, valor (key, value)
diccionario = {
    "IDE":"Integrated Development Environment",
    "OOP": "Object Oriented Programing",
    "DBMS": "Database Management System"
}

print(diccionario)

#largo
print(len(diccionario))

#accediendo a un elemento
print(diccionario["IDE"])

#otra forma, mismo resultado"
print (diccionario.get("IDE"))

#modificando valores
diccionario["IDE"]="Integrated development environment"
print(diccionario)

#iterar 
for termino in diccionario:
    print(termino)
    
for termino in diccionario:
    print(diccionario[termino])
    
for valor in diccionario.values():
    print(valor)
    
#comprobando existencia de un elemento
print ("IDE" in diccionario)

#agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print(diccionario)
