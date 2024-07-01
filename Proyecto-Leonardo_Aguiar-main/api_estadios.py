import requests
from estadio import Estadio
from restaurante import Restaurante
from producto import Producto

class ApiEstadios:

    estadios = []

    @staticmethod
    def obtener_datos_estadios():
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
        response = requests.get(url)
        data = response.json()
        ApiEstadios._crear_objetos_desde_json(data)

    @classmethod
    def _crear_objetos_desde_json(cls, data):
        cls.estadios = []
        for item in data:
            estadio = Estadio(item['id'], item["name"], item["city"], item["capacity"])

            for rest_data in item["restaurants"]:
                restaurante = Restaurante(rest_data["name"])

                for prod_data in rest_data["products"]:
                    producto = Producto(
                        prod_data["name"],
                        prod_data["quantity"],
                        prod_data["price"],
                        prod_data["stock"],
                        prod_data.get("adicional", "")
                    )
                    restaurante.agregar_producto(producto)

                estadio.agregar_restaurante(restaurante)

            cls.estadios.append(estadio)

    @classmethod
    def guardar_estadios(cls, filename):
        with open(filename, 'w') as file:
            for estadio in cls.estadios:
                file.write(f"Estadio: {estadio.id};{estadio.nombre};{estadio.ciudad};{estadio.capacidad}\n")
                for restaurante in estadio.restaurantes:
                    file.write(f"  Restaurante: {restaurante.nombre}\n")
                    for producto in restaurante.productos:
                        file.write(f"    Producto: {producto.nombre};{producto.cantidad};{producto.precio};{producto.stock};{producto.adicional}\n")

    @classmethod
    def cargar_estadios(cls, filename):
        cls.estadios = []
        with open(filename, 'r') as file:
            lines = file.readlines()

        estadio = None
        restaurante = None

        for line in lines:
            if line.startswith("Estadio:"):
                parts = line.strip().split(': ')[1].split(';')
                estadio = Estadio(parts[0], parts[1], parts[2], parts[3])
                cls.estadios.append(estadio)
            elif line.startswith("  Restaurante:"):
                parts = line.strip().split(': ')[1]
                restaurante = Restaurante(parts)
                estadio.agregar_restaurante(restaurante)
            elif line.startswith("    Producto:"):
                parts = line.strip().split(': ')[1].split(';')
                producto = Producto(parts[0], parts[1], parts[2], parts[3], parts[4])
                restaurante.agregar_producto(producto)
