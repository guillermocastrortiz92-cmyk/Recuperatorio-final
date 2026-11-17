# Ejercicio nro 1
# EcoTech Solutions

# Punto A: limpiar un registro
def limpiar_registro_sensor(registro_raw):
    # saco los espacios del id
    s_id = registro_raw["sensor_id"].strip()

    # limpio la temperatura sacandole las letras
    t_str = str(registro_raw["temperatura"]).strip()
    t_str = t_str.replace("°C", "").replace("C", "").replace("c", "")
    temp_num = float(t_str)

    # si no tiene ubicacion o esta vacia le pongo un texto por defecto
    if "ubicacion" in registro_raw and registro_raw["ubicacion"] != "":
        ubica = registro_raw["ubicacion"].strip()
    else:
        ubica = "Sin ubicacion"

    # armo el diccionario limpio
    dic_limpio = {
        "sensor_id": s_id,
        "temperatura": temp_num,
        "ubicacion": ubica
    }
    
    return dic_limpio


# Punto B: generar resumen y alertas
def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    alertas = []
    acumulador = 0

    for s in lista_sensores_limpios:
        acumulador = acumulador + s["temperatura"]
        
        # si pasa el umbral lo meto en la lista de alerta
        if s["temperatura"] > umbral_temperatura:
            alertas.append(s["sensor_id"])

    # calculo el promedio
    promedio = acumulador / len(lista_sensores_limpios)

    return (alertas, promedio)


# --- PRUEBAS DEL PROGRAMA ---
lecturas_crudas = [
    {"sensor_id": " SENSOR-1 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
    {"sensor_id": "SENSOR-2 ", "temperatura": "31.8°C"},
    {"sensor_id": " SENSOR-3", "temperatura": "19.2c", "ubicacion": "Deposito"},
    {"sensor_id": "SENSOR-4", "temperatura": "29.4 C", "ubicacion": ""}
]

# print("Datos originales:", lecturas_crudas) # por las dudas para ver que entren bien

# limpio las lecturas usando un bucle for comun
sensores_limpios = []
for reg in lecturas_crudas:
    resultado_limpio = limpiar_registro_sensor(reg)
    sensores_limpios.append(resultado_limpio)

# busco alertas y promedio
limite = 28.0
lista_alertas, promedio_global = generar_resumen_sensores(sensores_limpios, limite)

# muestro el reporte por pantalla
print("=== REPORTE DE SENSORES ===")
for item in sensores_limpios:
    print("Sensor:", item["sensor_id"], "|| Temp:", item["temperatura"], "|| Ubicacion:", item["ubicacion"])

print("-----------------------------------")
print("Promedio general de temperatura:", round(promedio_global, 2))
print("Sensores que superan el umbral:", lista_alertas)