#set es una colección sin orden y sin indice, no permite elementos repetidos
#  los elementos no se pueden modificar, pero si agregar nuevos o eliminar
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

#largo
print(len(planetas))

#revisar si un elemento está presente
print("Marte" in planetas)

#agregar
#no se puede agregar elementos duplicados
planetas.add("Tierra")
print(planetas)
