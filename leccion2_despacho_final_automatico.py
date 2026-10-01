despachar_producto: bool
peso_correcto: bool = False
es_azul: bool = True
vaciado_de_linea_activado: bool = True
sensor_obstruido: bool = False

despachar_producto = (peso_correcto and es_azul) or (vaciado_de_linea_activado and not sensor_obstruido)

if despachar_producto:
    print("Despachar producto")
else: 
    print("No despachar producto")