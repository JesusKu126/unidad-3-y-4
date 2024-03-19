from queue import Queue
class ServiciosCompaniaSeguros:
    def __init__(self, num_colas):
        self.colas = [Queue() for _ in range(num_colas)]
        self.numero_atencion = 1
    def llegar_cliente(self, servicio):
        cola_elegida = servicio % len(self.colas)
        self.colas[cola_elegida].put(self.numero_atencion)
        numero_atencion = self.numero_atencion
        self.numero_atencion += 1
        return numero_atencion
    def atender_cliente(self, servicio):
        cola_elegida = servicio % len(self.colas)
        if not self.colas[cola_elegida].empty():
            numero_atencion = self.colas[cola_elegida].get()
            return numero_atencion
        else:
            return None
def manejar_entrada(sistema):
    while True:
        entrada = input("Ingrese 'C' para la llegada de un cliente o 'A' para atender: ").upper()
        if entrada == 'C':
            servicio = int(input("Ingrese el número de servicio del cliente: "))
            numero_atencion = sistema.llegar_cliente(servicio)
            print(f"Cliente llegado. Número de atención: {numero_atencion}")
        elif entrada == 'A':
            servicio = int(input("Ingrese el número de servicio que desea atender: "))
            numero_atencion = sistema.atender_cliente(servicio)
            if numero_atencion:
                print(f"Atendiendo cliente. Número de atención: {numero_atencion}")
            else:
                print("No hay clientes en espera para este servicio.")
        else:
            print("Entrada inválida. Por favor, ingrese 'C' o 'A'.")
num_colas = int(input("Ingrese el número de colas de servicios: "))
sistema_seguros = ServiciosCompaniaSeguros(num_colas)
manejar_entrada(sistema_seguros)
