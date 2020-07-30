#Ejercicio 1
#Escribir una clase en python que convierta un número entero a número romano

class ConvertirRomano():
    
    def conversion(self, numero):

        convertir = True
        
        list = []
        
        lista_romanos = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XL","L", "XC", "C", "M"]
        
        while convertir:
            
            self.numero = numero
            
            numero_int = int(numero)
            
            if numero_int == 0 or numero_int > 100:
                print("El número no puede ser cero ni mayor que 100")
                
            else:
                while True:
                    if len(numero) == 1:
                        if numero_int == 1:
                            list.append(lista_romanos[0])
                            break
                        elif numero_int == 2:
                            list.append(lista_romanos[1])
                            break
                        elif numero_int == 3:
                            list.append(lista_romanos[2])
                            break
                        elif numero_int == 4:
                            list.append(lista_romanos[3])
                            break
                        elif numero_int == 5:
                            list.append(lista_romanos[4])
                            break
                        elif numero_int == 6:
                            list.append(lista_romanos[5])
                            break
                        elif numero_int == 7:
                            list.append(lista_romanos[6])
                            break
                        elif numero_int == 8:
                            list.append(lista_romanos[7])
                            break
                        elif numero_int == 9:
                            list.append(lista_romanos[8])
                            break      
                    
                    if len(numero) > 1 and len(numero) < 3:
                            if numero[0] == "1":
                                if numero[1] == "0":
                                    list.append(lista_romanos[9])
                                    break
                                elif numero[1] == "1":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[0])
                                    break
                                elif numero[1] == "2":   
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[1])
                                    break
                                elif numero[1] == "3":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[2])
                                    break
                                elif numero[1] == "4":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[3])
                                    break
                                elif numero[1] == "5":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[4])
                                    break
                                elif numero[1] == "6":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[5])
                                    break
                                elif numero[1] == "7":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[6])
                                    break
                                elif numero[1] == "8":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[7])
                                    break
                                elif numero[1] == "9":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[8])
                                    break
                            
                            elif numero[0] == "2":
                                if numero[1] == "0":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    break
                                elif numero[1] == "1":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[0])
                                    break
                                elif numero[1] == "2":   
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[1])
                                    break
                                elif numero[1] == "3":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[2])
                                    break
                                elif numero[1] == "4":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[3])
                                    break
                                elif numero[1] == "5":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[4])
                                    break
                                elif numero[1] == "6":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[5])
                                    break
                                elif numero[1] == "7":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[6])
                                    break
                                elif numero[1] == "8":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[7])
                                    break
                                elif numero[1] == "9":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[8])
                                    break
                                
                            elif numero[0] == "3":
                                if numero[1] == "0":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    break
                                elif numero[1] == "1":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[0])
                                    break
                                elif numero[1] == "2":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[1])
                                    break
                                elif numero[1] == "3":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[2])
                                    break
                                elif numero[1] == "4":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[3])
                                    break
                                elif numero[1] == "5":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[4])
                                    break
                                elif numero[1] == "6":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[5])
                                    break
                                elif numero[1] == "7":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[6])
                                    break
                                elif numero[1] == "8":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[7])
                                    break
                                elif numero[1] == "9":
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[8])                    
                                    break
                                
                            
                            elif numero[0] == "4":
                                if numero[1] == "0":
                                    list.append(lista_romanos[10])
                
                                    break
                                elif numero[1] == "1":
                                    list.append(lista_romanos[10])
                                    list.append(lista_romanos[0])
                                    break
                                elif numero[1] == "2":
                                    list.append(lista_romanos[10])
                                    list.append(lista_romanos[1])
                                    break
                                elif numero[1] == "3":
                                    list.append(lista_romanos[10])
                                    list.append(lista_romanos[2])
                                    break
                                elif numero[1] == "4":
                                    list.append(lista_romanos[10])
                                    list.append(lista_romanos[3])
                                    break
                                elif numero[1] == "5":
                                    list.append(lista_romanos[10])
                                    list.append(lista_romanos[4])
                                    break
                                elif numero[1] == "6":
                                    list.append(lista_romanos[10])
                                    list.append(lista_romanos[5])
                                    break
                                elif numero[1] == "7":
                                    list.append(lista_romanos[10])
                                    list.append(lista_romanos[6])
                                    break
                                elif numero[1] == "8":
                                    list.append(lista_romanos[10])
                                    list.append(lista_romanos[7])
                                    break
                                elif numero[1] == "9":
                                    list.append(lista_romanos[10])
                                    list.append(lista_romanos[8])                    
                                    break
                                            
                            elif numero[0] == "5":
                                if numero[1] == "0":
                                    list.append(lista_romanos[11])
                
                                    break
                                elif numero[1] == "1":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[0])
                                    break
                                elif numero[1] == "2":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[1])
                                    break
                                elif numero[1] == "3":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[2])
                                    break
                                elif numero[1] == "4":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[3])
                                    break
                                elif numero[1] == "5":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[4])
                                    break
                                elif numero[1] == "6":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[5])
                                    break
                                elif numero[1] == "7":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[6])
                                    break
                                elif numero[1] == "8":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[7])
                                    break
                                elif numero[1] == "9":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[8])                    
                                    break
                            
                            elif numero[0] == "6":
                                if numero[1] == "0":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    break
                                elif numero[1] == "1":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[0])
                                    break
                                elif numero[1] == "2":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[1])
                                    break
                                elif numero[1] == "3":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[2])
                                    break
                                elif numero[1] == "4":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[3])
                                    break
                                elif numero[1] == "5":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[4])
                                    break
                                elif numero[1] == "6":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[5])
                                    break
                                elif numero[1] == "7":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[6])
                                    break
                                elif numero[1] == "8":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[7])
                                    break
                                elif numero[1] == "9":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[8])                    
                                    break
                            
                            elif numero[0] == "7":
                                if numero[1] == "0":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    break
                                elif numero[1] == "1":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[0])
                                    break
                                elif numero[1] == "2":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[1])
                                    break
                                elif numero[1] == "3":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[2])
                                    break
                                elif numero[1] == "4":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[3])
                                    break
                                elif numero[1] == "5":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[4])
                                    break
                                elif numero[1] == "6":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[5])
                                    break
                                elif numero[1] == "7":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[6])
                                    break
                                elif numero[1] == "8":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[7])
                                    break
                                elif numero[1] == "9":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[8])                    
                                    break
                            
                            elif numero[0] == "8":
                                if numero[1] == "0":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    break
                                elif numero[1] == "1":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[0])
                                    break
                                elif numero[1] == "2":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[1])
                                    break
                                elif numero[1] == "3":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[2])
                                    break
                                elif numero[1] == "4":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[3])
                                    break
                                elif numero[1] == "5":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[4])
                                    break
                                elif numero[1] == "6":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[5])
                                    break
                                elif numero[1] == "7":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[6])
                                    break
                                elif numero[1] == "8":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[7])
                                    break
                                elif numero[1] == "9":
                                    list.append(lista_romanos[11])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[9])
                                    list.append(lista_romanos[8])                    
                                    break
                            
                            elif numero[0] == "9":
                                if numero[1] == "0":
                                    list.append(lista_romanos[12])
                                    break
                                elif numero[1] == "1":
                                    list.append(lista_romanos[12])
                                    list.append(lista_romanos[0])
                                    break
                                elif numero[1] == "2":
                                    list.append(lista_romanos[12])
                                    list.append(lista_romanos[1])
                                    break
                                elif numero[1] == "3":
                                    list.append(lista_romanos[12])
                                    list.append(lista_romanos[2])
                                    break
                                elif numero[1] == "4":
                                    list.append(lista_romanos[12])
                                    list.append(lista_romanos[3])
                                    break
                                elif numero[1] == "5":
                                    list.append(lista_romanos[12])
                                    list.append(lista_romanos[4])
                                    break
                                elif numero[1] == "6":
                                    list.append(lista_romanos[12])
                                    list.append(lista_romanos[5])
                                    break
                                elif numero[1] == "7":
                                    list.append(lista_romanos[12])
                                    list.append(lista_romanos[6])
                                    break
                                elif numero[1] == "8":
                                    list.append(lista_romanos[12])
                                    list.append(lista_romanos[7])
                                    break
                                elif numero[1] == "9":
                                    list.append(lista_romanos[12])
                                    list.append(lista_romanos[8])                    
                                    break
                            
                    if len(numero) == 3:
                        list.append(lista_romanos[13])
                
                print("El numero romano equivalente es " + "".join(list) ) 
                convertir = False
    
    #end metodo convertir          
                
#end class ConvertirRomano            



x = input("Indica un numero entero entre 1 y 100 : ")    

conversor = ConvertirRomano()

conversor.conversion(x)
                
                
                