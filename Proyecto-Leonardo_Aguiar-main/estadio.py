class Estadio:
    def __init__(self, id,nombre, ciudad ,capacidad):
        self.id=id
        self.nombre = nombre
        self.capacidad = capacidad
        self.ciudad = ciudad
        self.restaurantes = []
    
    def __str__(self):
        return f"{self.id }{self.nombre} {self.ciudad} {self.capacidad}"
    
    
    
    
    def agregar_restaurante(self, restaurante):
        self.restaurantes.append(restaurante)