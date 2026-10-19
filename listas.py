lista = ["angel", "dylan", "valeria", "ana", "jose"]
lista2 = lista[1:-1]
print(lista2)

# aqui me falta terminar lo de: plastico = "4444-5555-6666-7777" esta al inicio de la clase 


#una compresion de lista ayuda a poner todo mas corto
plastico = "4567667788991234" #aqui son letras, para q sean numeros ponerle int al inicio
for letra in plastico #falta
plastico2 = [int(letra)for letra in plastico]
print(plastico2)

plastico2 = [int(letra)for letra in plastico] [::-1]