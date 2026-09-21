#declaración
lote_autorizado: bool
requerimientos_técnicos: bool
temperatura_horno: float
presión_línea_óptima: bool
requerimientos_insumos: bool
materia_prima_disponible: bool
orden_reabastecimiento_activa: bool
operarios_capacitados: int
es_turno_nocturno: bool
calidad_aprobada: bool
mantenimiento_pendiente: bool

#entradas
temperatura_horno = 190
presión_línea_óptima = True
materia_prima_disponible = True
orden_reabastecimiento_activa = True
operarios_capacitados = 3 
es_turno_nocturno = False
calidad_aprobada = True
mantenimiento_pendiente = False

# proceso
requerimientos_técnicos = (temperatura_horno >= 180) and presión_línea_óptima
requerimientos_insumos = materia_prima_disponible or orden_reabastecimiento_activa
lote_autorizado = requerimientos_técnicos and requerimientos_insumos

if lote_autorizado:
    operarios_capacitados and es_turno_nocturno
    print("Línea 1")
