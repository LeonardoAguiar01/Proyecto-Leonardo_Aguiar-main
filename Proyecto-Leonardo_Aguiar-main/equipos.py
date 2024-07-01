class Equipo:
    def __init__(self, id, codigo, nombre, grupo):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.grupo = grupo
    
    def __str__(self):
        return f"{self.id} {self.codigo} {self.nombre} {self.grupo}"