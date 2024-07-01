class Producto:
    def __init__(self, nombre, cantidad,precio ,stock, adicional):
        self.nombre = nombre
        self.cantidad = cantidad
        self.stock = stock
        self.precio = precio
        self.adicional = adicional
    
    def __str__(self):
        return f"{self.nombre} {self.cantidad}  - {self.precio} , {self.stock} ,  {self.adicional}"