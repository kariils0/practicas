from eii_utils import leer_entero

x: int = 0
y: int = 0
plastico1:str = "4123-5555-6666-7777" #es tarjeta visa pq empieza con 4 digitos
plastico2:str = "4123-5555-6666-x"
plastico3:str = "4123-5555-6666-777a"
plastico4:str = "4123555566667777"
plastico5:str = "5123555566667777"

def validar_bloque_numerico(texto:str, inicio:int, fin:int) -> bool:
    es_valido:bool = False
    bloque = texto[inicio:fin]
    es_valido = contar_digitos(bloque) == 4
    return es_valido

def funcion_angel(numeros:list[int], digitos:int) -> list[int]: #esta funcion puede venir en el examen 
    salida:list[int] = []
    for i in numeros: 
        if len(str(i)) == digitos:
            salida.append(i) #se le agrega un valor a la lista y la va guardando

def es_un_digito(caracter:str) -> bool:
    return caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9" or caracter == "0"

def contar_digitos(texto:str) -> int:
    contador: int=0
    for caracter in texto: #for each, va sacando cada elemento de las listas. No es necesario que la variable se haya escrito antes, se declare
        if es_un_digito(caracter):
            contador += 1
    return contador

def es_numero_valido(plastico:str) -> bool:
    salida:bool = False
    contador = int = 0
    plastico = plastico.strip() #aqui se estan quitando errores a los lados, pa quitar errores de capa 8
    if plastico[0] == "4" and (len(plastico) == 16 or len(plastico)==19): #str es una lista, pa ver la cant q contiene se usa len
        contador = contar_digitos(plastico)
        if contador == 16 and len(plastico):
            salida = True
        else: 
            salida = validar_bloque_numerico(plastico, 0,4) and validar_bloque_numerico(plastico, 5,9) and validar_bloque_numerico(plastico, 10,14) and validar_bloque_numerico(plastico, 15,19)
    return salida


def obtener_mayor(a:int, b:int) -> int:
    if a > b:
        return a
    else:
        return b

if __name__ == '__main__': #a partir de ahora esto es obligatorio, para decirle a python que ejecute solo esta parte del codigo
    x, y = 23, 43 #se pueden asignar valores de un tiro
    #print(obtener_mayor(x, y))
    print(plastico1, es_numero_valido(plastico1))
    print(plastico2, es_numero_valido(plastico2))
    print(plastico3, es_numero_valido(plastico3))
    print(plastico4, es_numero_valido(plastico4))
    print(plastico5, es_numero_valido(plastico5))
    print(funcion_angel([10, 34, 45, 67, 78, 89, 890, 887],3))
