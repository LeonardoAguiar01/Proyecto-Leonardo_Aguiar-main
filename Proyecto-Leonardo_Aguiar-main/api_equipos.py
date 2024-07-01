import requests
from equipos import Equipo

class ApiEquipos:
    equipos = []
    
    @staticmethod
    def obtener_datos_equipos():
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
        response = requests.get(url)
        data = response.json()
        ApiEquipos._crear_objetos_desde_json(data)
    
    @classmethod
    def _crear_objetos_desde_json(cls, data):
        cls.equipos = []
        for item in data:
            equipo = Equipo(item['id'], item["code"], item["name"], item["group"])
            cls.equipos.append(equipo)
    
    @classmethod
    def guardar_equipos(cls, filename):
        with open(filename, 'w') as file:
            for equipo in cls.equipos:
                file.write(f"Equipo: {equipo.id};{equipo.codigo};{equipo.nombre};{equipo.grupo}\n")
    
    @classmethod
    def cargar_equipos(cls, filename):
        cls.equipos = []
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            if line.startswith("Equipo:"):
                parts = line.strip().split(': ')[1].split(';')
                equipo = Equipo(parts[0], parts[1], parts[2], parts[3])
                cls.equipos.append(equipo)