class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    
    def __str__(self):
        return f"{self.nombre}"
    
    def agregar_producto(self, producto):
        self.productos.append(producto)