class Partido:
    def __init__(self, id, numero, home, away, fecha, grupo, estadio):
        self.id = id
        self.numero = numero
        self.home = home
        self.away = away
        self.fecha = fecha
        self.grupo = grupo
        self.estadio = estadio
    
    def __str__(self):
        return f"Partido {self.numero}: {self.home.nombre} vs {self.away.nombre} en {self.fecha}, Grupo {self.grupo}, Estadio {self.estadio.nombre}"
    
    