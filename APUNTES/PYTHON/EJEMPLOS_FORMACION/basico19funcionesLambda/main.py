def quince_por_ciento(a):
    return a * 0.15

resultado = quince_por_ciento(300)

print(resultado)

#Puedo guardar funciones en variables

variable = quince_por_ciento #sin parentesis

resultado2 = variable(300)

print(resultado2)

##EXPRESION LAMDA ( se usan para cosas pequeñas)

var = lambda a : a * 0.15

resultado3 = var(300)

#En este caso var tiene el mismo valor que variable en el caso anterior

print("var es : " + str(var))

var2 = lambda a , b : a * b

print(var2(5,4))