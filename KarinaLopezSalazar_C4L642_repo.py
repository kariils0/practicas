
costo_bolsa: int = 600
bolsas_adicionales: float = 0
bolsas_compradas: int = 0
piso: int = 2
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

bolsas_compradas = int(input(f"¿Cuántas bolsas compra María?"))
bolsas_adicionales = (bolsas_compradas // 12) * 3
inventario = bolsas_compradas + bolsas_adicionales
costo_total = bolsas_compradas * costo_bolsa



utilidad_final = ingreso - costo_total
print("REPORTE FINAL")
print("Ingreso total: ", ingreso)
print("Bolsas vendidas: ", bolsas_vendidas)
print("Bolsas restantes: ", bolsas_restantes)
print("Utilidad final: ", utilidad_final)