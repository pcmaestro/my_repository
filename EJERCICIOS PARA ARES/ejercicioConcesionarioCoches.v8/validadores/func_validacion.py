import re

from validadores import regexp


#metodos de validación

def validar_marca(marca):
    patron = regexp.validacion_marca
    validador = re.compile(patron)    
    return validador.match(marca)

def validar_modelo(modelo):
    patron = regexp.validacion_modelo
    validador = re.compile(patron)
    return validador.match(modelo)    
   
def validar_color(color):
    patron = regexp.validacion_color
    validador = re.compile(patron)
    return validador.match(color)    

def validar_motor(motor):
    patron = regexp.validacion_motor
    validador = re.compile(patron)
    return validador.match(motor)    

def validar_precio(precio):
    patron = regexp.validacion_precio
    validador = re.compile(patron)    
    return validador.match(precio)    

def validar_forma_pago(forma_pago):
    patron = regexp.validacion_forma_pago
    validador = re.compile(patron)
    return validador.match(forma_pago)
