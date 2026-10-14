
costo_bolsa: int = 600
bolsas_adicionales: float = 0
bolsas_compradas: int = 0
piso: int = 1
aula: int = 10
aparece_seguridad: bool
compra_por_cliente: int = 0
precio_venta: int 
inventario: int = 0
hay_clientes_interesados: bool
costo_total: float = 0
ingreso: float = 0
bolsas_vendidas: int = 0
bolsas_restantes: int = 0
utilidad_final: float = 0
continuar_recorrido: bool = True


bolsas_compradas = int(input("¿Cuántas bolsas compra María?"))
bolsas_adicionales = (bolsas_compradas // 12) * 3
inventario = bolsas_compradas + bolsas_adicionales
costo_total = bolsas_compradas * costo_bolsa

while piso <= 2 and continuar_recorrido:
    aula = 1
    while aula <= 10 and continuar_recorrido:
        print(f"Se encuentra en el piso {piso} y en el aula {aula}")

        aparece_seguridad = input("¿Hay personal de seguridad cerca?: ")
        if aparece_seguridad == "True":
            print("Detener jornada")
            continuar_recorrido = False
        else:
            hay_clientes_interesados = input("¿Hay clientes interesados en esta aula?: ")
            while hay_clientes_interesados == "True" and inventario > 0 and continuar_recorrido:
                compra_por_cliente = int(input("¿Cuántas bolsas de plátanos comprará el cliente?: "))
                if compra_por_cliente < 1 or compra_por_cliente > 3:
                    print("No se le puede vender. La cantidad debe de ser 1, 2 o 3")
                elif compra_por_cliente > inventario:
                    print("Las ventas no pueden exceder el inventario")
                else:
                    if compra_por_cliente == 1:
                        precio_venta = 1100
                    elif compra_por_cliente == 2:
                        precio_venta = 1700
                    else:
                        precio_venta = 2400

                    inventario = inventario - compra_por_cliente
                    bolsas_vendidas = bolsas_vendidas + compra_por_cliente
                    ingreso = ingreso + precio_venta

                    if inventario == 0:
                        print("Hay que finalizar la jornada, el inventario se acabó")
                        continuar_recorrido = False
                if continuar_recorrido and inventario > 0:
                    hay_clientes_interesados = input("¿Todavía hay clientes interesados en esta aula? ")
        if continuar_recorrido:
            aula = aula + 1
    if continuar_recorrido:
        piso = piso + 1

bolsas_restantes = inventario
utilidad_final = ingreso - costo_total

print("REPORTE FINAL")
print(f"Ingreso total: {ingreso}")
print(f"Bolsas vendidas: {bolsas_vendidas}")
print(f"Bolsas restantes: {bolsas_restantes}")
print(f"Utilidad final: {utilidad_final}")