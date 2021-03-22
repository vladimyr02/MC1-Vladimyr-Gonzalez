#Importamos las bibliotecas 
import math
import numpy as np 
import sympy as sy

#Definir las variables
valor = 0
contador = 0
error = 0
punto = 0.755
base = 0.75

# Definir X como variable en nuestra función "f(x)=e^x"
x = sy.Symbol('x')

# Definir la función "f(x)=e^x"
funcion = math.e**-x
ult_f_primo = funcion

# Definir valor esperado
valorespe = funcion.subs(x, punto)

# Metodo para la serie de taylor
def serieTaylor(valor, contador, funcion, punto, base,ult_f_primo, ):

    if (contador==0):
        valor1 = ult_f_primo.subs(x, base)
        return valor1, ult_f_primo

    else:
        fprimo = ult_f_primo.diff()
        valor1 = valor + ( ( (fprimo.subs(x, base)) / (math.factorial(contador)) ) * math.pow(punto - base, contador) )
        return valor1, fprimo

# Metodo para calcular el error relativo
def relativeError(va, ve):
    
    error = abs((va-ve)/ve)*100
    return error

# Main
for i in range(0, 15):
    
    valor, ult_f_primo = serieTaylor(valor, contador, funcion, punto, base, ult_f_primo)
    contador = contador + 1
    error = relativeError(valor, valorespe)
    
    print(
        
        f"\nOrden {contador}" +
        f"\nValor obtenido: {valor}" +
        f"\nValor esperado: {valorespe}" +
        f"\nError relativo porcentual: {error}" 
    )
 