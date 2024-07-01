from api_partidos import ApiPartidos
import re


class Gestion_partidos():
    
    def __init__(self):
        self.partidos = ApiPartidos.partidos
    
    def main(self):
        print('-- Gestión de partidos y estadios')
        while True:
            print('''
    1. Buscar partidos por país
    2. Buscar partidos por estadio
    3. Buscar partidos por fecha
    =========================
    4. Salir
    ''')
            seleccion = input("Ingrese el número correspondiente a su selección: ")
            while not seleccion.isnumeric() or int(seleccion) not in range(1, 5):
                print('Error')
                seleccion = input("Ingrese el número correspondiente a su selección: ")

            if seleccion == '1':
                self.buscar_pais_menu()
            elif seleccion == '2':
                self.buscar_estadio_menu()
            elif seleccion == '3':
                self.buscar_fecha_menu()
            else:
                print('Gracias por su visita. Vuelva pronto...')
                break

            ans = input('¿Desea continuar? [y/n]: ')
            while ans not in ['y', 'n']:
                print('Inválido')
                ans = input('¿Desea continuar? [y/n]: ')
            
            if ans == 'n':
                print('Gracias por su visita. Vuelva pronto...')
                break
    
    def buscar_pais_menu(self):
        print('Indique el país a buscar')
        datos = input("Ingrese el nombre del país: ")
        while not datos.isalpha():
            print('Error, solo se aceptan nombres')
            datos = input("Ingrese el nombre del país: ")
        
        self.buscar_pais(datos)
        
    def buscar_pais(self, dato):
        lista_partidos = []
        for partido in self.partidos:
            home = partido.home
            casa = home.nombre 
            away = partido.away
            fuera = away.nombre
            if casa == dato or fuera == dato:
                lista_partidos.append(partido)
                
        self.imprimir_partidos(lista_partidos)

            
    def buscar_estadio_menu(self):
        print('Indique el estadio a buscar')
        datos = input("Ingrese el nombre del estadio: ")
        while not self.validar_nombre_estadio(datos):
            print('Error, solo se aceptan nombres con letras y espacios')
            datos = input("Ingrese el nombre del estadio: ")
        
        self.buscar_estadio(datos)
        
    def validar_nombre_estadio(self, nombre):
        # Validar que el nombre contenga solo letras y espacios
        for char in nombre:
            if not (char.isalpha() or char.isspace()):
                return False
        return True
    
    def buscar_estadio(self, dato):
        lista_partidos = []
        for partido in self.partidos:
            estadio = partido.estadio
            estadio1 = estadio.nombre
            
            if estadio1 == dato: 
                lista_partidos.append(partido)
                
        if lista_partidos:
            self.imprimir_partidos(lista_partidos)
        else:
            
            print(f"No se encontraron partidos en el estadio '{dato}'.")

    def buscar_fecha_menu(self):
        print('Indique la fecha del partido a buscar')
        datos = input("Ingrese la fecha del partido (YYYY-MM-DD): ")
        while not self.validar_fecha(datos):
            print('Error, escriba la fecha en formato YYYY-MM-DD')
            datos = input("Ingrese la fecha del partido (YYYY-MM-DD): ")
            
        self.buscar_fecha(datos)

    def validar_fecha(self, fecha):
        # Definir el patrón de la expresión regular para "YYYY-MM-DD"
        patron = r"^\d{4}-\d{2}-\d{2}$"
    
        # Usar re.match para verificar si la cadena coincide con el patrón
        if re.match(patron, fecha):
            return True
        else:
            return False

    def buscar_fecha(self, dato):
        lista_partidos = []
        for partido in self.partidos:
            fecha = partido.fecha
            if fecha == dato:
                lista_partidos.append(partido)
        
        if lista_partidos:
            self.imprimir_partidos(lista_partidos)
        else:
            print(f"No se encontraron partidos en la fecha '{dato}'.")
                    
    def imprimir_partidos(self,lista):
        for partido in lista:
            print(partido)

