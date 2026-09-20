#declaración
clima_soleado: bool
presupuesto: int 
fin_de_mes: bool
carlos_tiene_tarea: bool
maria_tiene_tarea: bool
presentan_pelicula_coyote: bool
cupones_obsequiados_mamá: bool
entradas_adquiridas_papá: bool
viabilidad_fin_de_semana: bool
#entradas
clima_soleado = False
presupuesto = 150000
fin_de_mes = False
carlos_tiene_tarea = True
maria_tiene_tarea = False
presentan_pelicula_coyote = False
cupones_obsequiados_mamá = False
entradas_adquiridas_papá = True
#proceso
viabilidad_fin_de_semana = ((clima_soleado and (presupuesto >= 100000) and fin_de_mes) or ((presupuesto >= 10000) and (not carlos_tiene_tarea) and (not maria_tiene_tarea)) or (presentan_pelicula_coyote and (cupones_obsequiados_mamá or entradas_adquiridas_papá)))
#salida
if viabilidad_fin_de_semana:
    print ("pueden realizar una actividad el fin de semana")
else:
    print ("no pueden realizar ninguna actividad el fin de semana")