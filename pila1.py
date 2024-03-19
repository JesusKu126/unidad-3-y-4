from queue import Queue
def sumar_colas(cola1, cola2):
    if cola1.qsize() != cola2.qsize():
        raise ValueError("Las colas deben tener la misma cantidad de elementos")
    resultado = Queue()
    while not cola1.empty() and not cola2.empty():
        elemento1 = cola1.get()
        elemento2 = cola2.get()
        suma = elemento1 + elemento2
        resultado.put(suma)
    return resultado
def crear_cola_desde_entrada(tamano):
    cola = Queue()
    print(f"Ingrese {tamano} elementos para la cola (separados por espacio):")
    elementos = input().split()
    for elemento in elementos:
        cola.put(int(elemento))
    return cola
tamaño = int(input("Ingrese el tamaño de las colas: "))
print("Ingrese los datos para la primera cola:")
cola1 = crear_cola_desde_entrada(tamaño)
print("Ingrese los datos para la segunda cola:")
cola2 = crear_cola_desde_entrada(tamaño)
try:
    resultado = sumar_colas(cola1, cola2)
    print("\nResultado de la suma de colas:")
    while not resultado.empty():
        print(resultado.get())
except ValueError as e:
    print("Error:", e)
