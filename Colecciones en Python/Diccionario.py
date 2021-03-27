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