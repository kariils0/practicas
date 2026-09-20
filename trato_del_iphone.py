#declaración
compra_iphone: bool
rendimiento_académico: bool
promedio_general: float 
nota_materia_1: float
nota_materia_2: float
nota_materia_3: float
nota_materia_4: float
colaboración_en_hogar: bool
lavado_auto_abuela: int
lavado_auto_mamá: int
#entradas
promedio_general = 80
nota_materia_1 = 75
nota_materia_2 = 80
nota_materia_3 = 69
nota_materia_4 = 78
lavado_auto_abuela = 3
lavado_auto_mamá = 7
#proceso
rendimiento_académico = (promedio_general >= 80) and (nota_materia_1 >= 75 and nota_materia_2 >= 75 and nota_materia_3 >= 75 and nota_materia_4 >= 75)
colaboración_en_hogar = (lavado_auto_abuela >= 8) or (lavado_auto_mamá >= 8) or ((lavado_auto_abuela + lavado_auto_mamá) >= 12)
compra_iphone = rendimiento_académico and colaboración_en_hogar
#salida
if compra_iphone:
    print("La abuela de Carmen le puede comprar el último modelo de iPhone")
else:
    print("No se le puede comprar el iPhone a Carmen")