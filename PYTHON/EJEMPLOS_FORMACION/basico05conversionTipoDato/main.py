
variable = "123"

tipo = type(variable)

print("Variable : " + variable + " tipo " + str(tipo) )

#A esta transformación que hacemos ahora se le llama casting, en este caso casting a entero
resultado = int(variable) + 10

print("El resultado es " + str(resultado))