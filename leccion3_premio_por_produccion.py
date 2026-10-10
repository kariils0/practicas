meta_zapatos: int = 50
pago_normal: float = 5.00
pago_extra: float = 6.00
pago_total: float
pares_extra: int
pares_faltantes: int 
pares_armados: int =  10

if pares_armados == meta_zapatos:
    pago_total = pares_armados * pago_normal
    print("Alcanzó la meta exacta de 50 pares.")
elif pares_armados > meta_zapatos:
    pares_extra = pares_armados -meta_zapatos
    pago_total = (meta_zapatos * pago_normal) + (pares_extra * pago_extra)
    print(f"Superó la meta con {pares_extra} par(es) extra(s).")
else:
    pares_faltantes = meta_zapatos - pares_armados
    if pares_faltantes > 0:
        print(f"No alcanzó la meta. Le faltaron {pares_faltantes}.")
    pago_total = pares_armados * pago_normal

print(f"Su pago total es: {pago_total}.")