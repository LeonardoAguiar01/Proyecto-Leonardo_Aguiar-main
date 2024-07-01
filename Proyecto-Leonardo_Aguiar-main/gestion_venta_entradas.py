from api_clientes import ApiClientes

class Gestion_venta_entradas():
    
    def __init__(self) -> None:
        pass
    
    def main(self):
        print('-- Gestión de ventas de entradas')
        while True:
            print('''
    1. Registrar Cliente
    =========================
    2. Salir
    ''')
            seleccion = input("Ingrese el número correspondiente a su selección: ")
            while not seleccion.isnumeric() or int(seleccion) not in range(1, 3):
                print('Error')
                seleccion = input("Ingrese el número correspondiente a su selección: ")

            if seleccion == '1':
                ApiClientes.crear_cliente()
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
