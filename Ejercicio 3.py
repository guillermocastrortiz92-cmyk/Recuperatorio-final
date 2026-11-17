#Ejercicio nro 3


import unittest

# Punto A
def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")
    
    resultado = consumo_kwh * factor_emision
    return resultado


class TestCalculoEmisiones(unittest.TestCase):
    
    def test_valores_normales(self):
        # pruebo con un consumo normal y el factor por defecto
        calculo = calcular_emisiones_carbono(100)
        self.assertEqual(calculo, 40.0)
        
    def test_consumo_negativo(self):
        # verifico que salte el ValueError si el numero es menor a 0
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)


# Punto B
def obtener_metricas_consumo(registros):
    total_global = 0
    mayor_consumo = 0
    planta_top = ""
    
    for r in registros:
        consumo = r["consumo"]
        
        # uso la funcion del punto A para sacar las emisiones
        emisiones = calcular_emisiones_carbono(consumo)
        total_global = total_global + emisiones
        
        # me fijo si esta planta consumo mas que la anterior
        if consumo > mayor_consumo:
            mayor_consumo = consumo
            planta_top = r["planta"]
            
    return (total_global, planta_top)


def vista_panel_sustentabilidad(request):
    #  ejemplo para probar la vista
    datos_plantas = [
        {"planta": "Planta Norte", "consumo": 1200},
        {"planta": "Planta Sur", "consumo": 850},
        {"planta": "Planta Este", "consumo": 2100}
    ]
    
    total_emisiones, planta_mayor = obtener_metricas_consumo(datos_plantas)
    
    contexto = {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor
    }
    
    # return render(request, 'sustentabilidad/panel.html', contexto)
    return contexto


# pruebas  en consola
if __name__ == "__main__":
    print("Probando vista:", vista_panel_sustentabilidad(None))
    unittest.main()


