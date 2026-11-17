#Ejercicio nro "2"

import json

# excepción personalizada para el stock inválido
class StockInvalidoError(Exception):
    pass


# base orientada a objetos
class DispositivoEcologico:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        #valores no negativos
        self.stock = stock

    # encapsulamiento de valores
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise StockInvalidoError("Error: El stock no puede ser un valor negativo.")
        self.__stock = nuevo_stock

    # base para adaptar con polimorfismo
    def ficha_tecnica(self):
        return "Dispositivo: " + self.nombre + " - Stock: " + str(self.__stock)


# clase
class PanelSolar(DispositivoEcologico):
    def __init__(self, nombre, stock, potencia_w):
        #atributos de la clase padre
        super().__init__(nombre, stock)
        self.potencia_w = potencia_w

    # Polimorfismo: personalizamos la ficha técnica para los paneles solares
    def ficha_tecnica(self):
        ficha = "Panel Solar: " + self.nombre + " | Potencia: " + str(self.potencia_w) + "W | Stock: " + str(self.stock)
        return ficha


# gestor para manejo de la persistencia del catálogo
class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        # convertimos los objetos  para guardarlos en el archivo JSON
        catalogo_lista = []
        
        for dispositivo in lista_dispositivos:
            # verificamos panel solar para guardar su atributo extra
            if isinstance(dispositivo, PanelSolar):
                datos = {
                    "tipo": "PanelSolar",
                    "nombre": dispositivo.nombre,
                    "stock": dispositivo.stock,
                    "potencia_w": dispositivo.potencia_w
                }
            else:
                datos = {
                    "tipo": "Generico",
                    "nombre": dispositivo.nombre,
                    "stock": dispositivo.stock
                }
            catalogo_lista.append(datos)

        # guardado de lista en el archivo con formato JSON
        archivo = open(ruta_archivo, "w", encoding="utf-8")
        json.dump(catalogo_lista, archivo, indent=4, ensure_ascii=False)
        archivo.close()

# PRUEBA Y EJECUCIÓN

print("=== PRUEBA 1: Verificando la captura de StockInvalidoError ===")
try:
    # prueba de error (valores negativos)
    panel_roto = PanelSolar("Panel Test", -5, 300)
except StockInvalidoError as error:
    print("¡Excepción atrapada con éxito!", error)

print("\n=== PRUEBA 2: Creando productos válidos y exportando a JSON ===")

# instancias válidas
panel_1 = PanelSolar("EcoSun 400W", 15, 400)
panel_2 = PanelSolar("SunPower Pro", 8, 500)
dispositivo_gen = DispositivoEcologico("Filtro de Agua Bio", 25)

# Proba de el polimorfismo imprimiendo las fichas técnicas
print(panel_1.ficha_tecnica())
print(panel_2.ficha_tecnica())
print(dispositivo_gen.ficha_tecnica())

lista_productos = [panel_1, panel_2, dispositivo_gen]

# gestor y guardamos el archivo requerido
gestor = GestorInventario()
nombre_archivo = "catalogo_ecotech.json"

gestor.guardar_catalogo_json(lista_productos, nombre_archivo)

print("\n¡Catálogo exportado exitosamente al archivo '" + nombre_archivo + "'!")
