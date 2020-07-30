#Ejemplo de uso de set

mi_set = {"platano", "naranja", "manzana"}

#print(mi_set[0]) . Esto no se puede hacer, los set no tienen indice, los elementos se guardan de forma desordenada

#Podemos agregar y eleminar elementos en un set

mi_set.add("pera") 

mi_set.remove("platano")

#A pesar de no tener indice,  si podemos recorrer el contenido de lo set
for elemento in mi_set:
    print(elemento)
    
    
    