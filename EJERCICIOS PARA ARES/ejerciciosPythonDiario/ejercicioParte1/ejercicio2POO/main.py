class ConvertirEntero():
    
    def __init__(self):
        
        self.numero = ""
        self.diccionario = {}
     
    def convertir(self,numero):       
        
        self.numero = numero
         
        self.diccionario = {"I":1, "II":2, "III":3, "IV":4, "V":5, "VI":6, "VII":7, "VIII":8, "IX":9, "X":10}
        

        if self.numero in self.diccionario:
            for i in self.diccionario:
                if seelf.numero == i:
                    print("El equivalente entero de " + self.numero + " es " + str(self.diccionario[i]))
                    break
        else:
            print("El número debe ser un valor romano entre 1 y 10")           
     
 #end clase ConvertirEntero
 
 
conversor = ConvertirEntero()
                 
x = (input("Indica un número romano para conocer su equivalente en número entero : ")).upper()

conversor.convertir(x)

    


