from cliente import Cliente
from api_partidos import ApiPartidos

class ApiClientes:
    clientes=[]

    @classmethod
    def crear_cliente(cls):
        partidos_disponibles=ApiPartidos.partidos

        cedula = input("Escriba su cedula: ")
        while not cedula.isnumeric():
            print("Error, debe ingresar solo numeros")
            cedula = input("Escriba su cedula: ")

        nombre = input("Escriba su nombre: ")
        while not nombre.isalpha() and nombre.isspace():
            print("Error, debe ingresar solo letras")
            nombre = input("Escriba su nombre: ")

        edad= input("Cuantos años tienes:")
        while not edad.isnumeric():
            print("Error, debe ingresar solo numeros")
            edad = input("Cuantos años tienes:")    

        print("Partidos disponibles:")
        for i, partido in enumerate(partidos_disponibles):
            print(f"{partido}")

        partido_index = (input("Elija el partido (número): ")) 
        while not partido_index.isnumeric() or int(partido_index) not in range(1, 37):
            print("Partido no existente")
            partido_index= (input("Elija el partido (número): "))

        partido_index = int(partido_index) -1
    

        partido = partidos_disponibles[partido_index]
        print("""
                Si es General: solo podrá ver el partido en su asiento
                El precio es de $35
                Si es VIP; podrá disfrutar del restaurante del estadio, es decir, podrá adquirir productos de dicho restaurante. 
                El precio de una entrada VIP es de $75""")
        
        tipo_entrada = input("Escriba el tipo de entrada (General o Vip): ")
        while tipo_entrada != "General" and tipo_entrada != "Vip":
            print("Error, escribiste algo mal")
            tipo_entrada = input("Escriba el tipo de entrada (General o Vip): ")
                                 
        cliente = Cliente(nombre, cedula, edad, partido, tipo_entrada)
        cls.clientes.append(cliente)
        cls.guardar_clientes("clientes.txt")
   
        

    @classmethod
    def guardar_clientes(cls, filename):
        with open(filename, 'w') as file:
            for cliente in cls.clientes:
                partido=cliente.partido
                partido_id=partido.id
                file.write(f"Cliente: {cliente.nombre};{cliente.cedula};{cliente.edad};{partido_id};{cliente.tipo_entrada}\n")
    
    
    @classmethod
    def cargar_clientes(cls, filename):
        cls.clientes = []
        with open(filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith("Cliente:"):
                parts = line.strip().split(': ')[1].split(';')
                partido_id=parts[3]
                partido = cls.buscar_partido_cliente(partido_id)
                cliente = Cliente(parts[0], parts[1], parts[2], partido , parts[4])
                cls.clientes.append(cliente)

    @classmethod
    def buscar_partido_cliente(cls, partido_id):
        partidos=ApiPartidos.partidos
        for partido in partidos:
            if partido.id == partido_id:
                return partido
