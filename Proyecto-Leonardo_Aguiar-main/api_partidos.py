import requests
from api_estadios import ApiEstadios
from api_equipos import ApiEquipos
from estadio import Estadio
from equipos import Equipo
from partidos import Partido

class ApiPartidos:
    partidos = []
   
    @staticmethod
    def get_estadio(id):
        lista_estadios=ApiEstadios.estadios

        for estadio in lista_estadios:
            if estadio.id == id:
                return estadio

    @staticmethod
    def get_equipos(id):
        lista_equipos=ApiEquipos.equipos

        for equipo in lista_equipos:
            if equipo.id == id:
                return equipo

    @staticmethod
    def obtener_datos_partidos():
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
        response = requests.get(url)
        data = response.json()
        ApiPartidos._crear_objetos_desde_json(data)

    @classmethod
    def _crear_objetos_desde_json(cls, data):
        cls.partidos = []

        for item in data:
            home = cls.get_equipos(item['home']['id'])
            away = cls.get_equipos(item['away']['id'])
            estadio = cls.get_estadio(item['stadium_id'])
            obj = Partido(item['id'], item['number'], home, away, item['date'], item['group'], estadio)
            cls.partidos.append(obj)

        for partido in cls.partidos:
            print(partido)

    @classmethod
    def guardar_partidos(cls, filename):
        with open(filename, 'w') as file:
            for partido in cls.partidos:
                file.write(f"Partido: {partido.id};{partido.numero};{partido.fecha};{partido.grupo};{partido.estadio.id}\n")
                file.write(f"  Equipo local: {partido.home.id};\n")
                file.write(f"  Equipo visitante: {partido.away.id};\n")
                
    @classmethod
    def cargar_partidos(cls, filename):
        cls.partidos = []
        with open(filename, 'r') as file:
            lines = file.readlines()

        partido = None
        home = None
        away = None
        estadio = None

        for line in lines:
            if line.startswith("Partido:"):
                parts = line.strip().split(': ')[1].split(';')
                estadio= parts[4]
                estadio_obj=cls.get_estadio(estadio)
                partido = Partido(parts[0], parts[1], None, None, parts[2], parts[3], estadio_obj)
                cls.partidos.append(partido)
            elif line.startswith("  Equipo local:"):
                parts = line.strip().split(': ')[1].split(';')
                home=cls.get_equipos(parts[0])
                partido.home = home
            elif line.startswith("  Equipo visitante:"):
                parts = line.strip().split(': ')[1].split(';')
                away = cls.get_equipos(parts[0])
                partido.away = away
                
    @classmethod
    def ordenar_partidos(cls):
        cls.partidos.sort(key=lambda x: int(x.numero))


