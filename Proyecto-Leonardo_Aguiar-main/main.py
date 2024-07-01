from api_equipos import ApiEquipos
from api_estadios import ApiEstadios
from api_partidos import ApiPartidos
from gestion_partidos import Gestion_partidos
from api_clientes import ApiClientes
from gestion_venta_entradas import Gestion_venta_entradas


class Main():
    
    def __init__(self):
        self.gestion_partidos = Gestion_partidos()
        self.gestion_entradas = Gestion_venta_entradas()
    
    def mostrar_menu(self):
        print('-- Bienvenido a Eurocopa 2024')
        while True:
            print('''
    1. Gestión de partidos y estadios
    2. Gestión de venta de entradas
    3. Gestión de asistencia a partidos
    4. Gestión de restaurantes
    5. Gestión de venta de restaurantes
    6. Indicadores de gestión 
    =========================
    7. Salir
    ''')
                
            seleccion = input("Ingrese el número correspondiente a su selección: ")
            while not seleccion.isnumeric() or int(seleccion) not in range(1, 8):
                print('Error: Selección inválida')
                seleccion = input("Ingrese el número correspondiente a su selección: ")

            if seleccion == '1':
                self.gestion_partidos.main()
            elif seleccion == '2':
                self.gestion_entradas.main()
            elif seleccion == '3':
                print("Opción en construcción: Gestión de asistencia a partidos")
            elif seleccion == '4':
                print("Opción en construcción: Gestión de restaurantes")
            elif seleccion == '5':
                print("Opción en construcción: Gestión de venta de restaurantes")
            elif seleccion == '6':
                print("Opción en construcción: Indicadores de gestión")
            else:
                print('Gracias por su visita. Vuelva pronto...')
                break

            ans = input('¿Desea continuar? [y/n]: ')
            while ans.lower() not in ['y', 'n']:
                print('Respuesta inválida')
                ans = input('¿Desea continuar? [y/n]: ')
                
            if ans == 'n':
                print('Gracias por su visita. Vuelva pronto...')
                break


if __name__ == '__main__':
    print('=== Sistema de Gestión Eurocopa 2024 ===')
    ApiEquipos.cargar_equipos('equipos.txt')
    ApiEstadios.cargar_estadios('estadios.txt')
    ApiPartidos.cargar_partidos('partidos.txt')
    ApiClientes.cargar_clientes('clientes.txt')
    main = Main()
    main.mostrar_menu()
