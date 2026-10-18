
print("Bienvenidos a la cafetería Cafecito")

opcion_1 = input("¿Qué bebida comprarás: café, té o chocolate? ").lower()
tamaño = input("¿Cuál será el tamaño de la bebida: S, M o L? ").upper()
precio = 0

#elegir bebida 
if opcion_1 == "café":
    precio = 1000
    opcion_cafe = input("¿Quieres el café descafeinado? ").upper()
    if opcion_cafe == "SI":
        precio += 500
    opcion_leche = input("¿Lo quieres con leche deslactosada? ").upper()
    if opcion_leche == "SI":
            precio += 300
elif opcion_1 == "té":
    precio = 700
elif opcion_1 == "chocolate":
    precio = 1500
else:
    print("Perdón, no tenemos esa opción")

#tamaño de bebida
if tamaño == "S":
    precio += 0
elif tamaño == "M":
    precio += 200
elif tamaño == "L":
    precio += 400
else:
    print("Perdón, de ese tamaño no tenemos")

#cantidad de bebidas 
cantidad = int(input("¿Cuántas bebidas comprará? "))
precio *= cantidad

#total a pagar
print(f"Su total a pagar es: {precio} colones")