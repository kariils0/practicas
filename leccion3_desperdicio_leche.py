litros_desperdiciados: int
dinero_perdido: int

litros_desperdiciados = 90
if litros_desperdiciados > 50:
    litros_desperdiciados = litros_desperdiciados
    dinero_perdido = litros_desperdiciados * 2.50
    print(f"Revisar boquillas de llenado. Además, su dinero perdido es de {dinero_perdido}")
else:
    print("Eficiencia aceptable")