import queue as cola

# Nodo con constructor y un metodo para agregar a la pila
class Nodo(object):
    def __init__(self, nombre_ciudad):
        self.nombre_ciudad = nombre_ciudad
        self.hijos = []

    def agregar_nodo_hijo(self, hijo):
        self.hijos.append(hijo)

# Separa los datos de ViajeRomania y los ingresa a un diccionario
def ConvertirRutaADiccionario():
    NodoArbol = [nodes.split('-') for nodes in ViajeRomania.split('*')][:-1]
    NodoArbol = {str(NodoPadre): [str(NodoHijo) for NodoHijo in NodoHijos.split()]
                  for NodoPadre, NodoHijos in NodoArbol}
    return NodoArbol

# Funcion que de diccionario lo convierte en un nodo con sub nodos (arbol)
def DiccionarioANodos():
    NodosDiccionario = {nodo: Nodo(nodo) for nodo in NodosArbol}
    for NodoPadre, NodoHijos in NodosArbol.items():
        for NodoHijo in NodoHijos:
            NodosDiccionario[NodoPadre].agregar_nodo_hijo(NodosDiccionario[NodoHijo])

    Ciudades = NodosDiccionario.values()
    return Ciudades

# Mostramos las ciudades que estan dentro de la Clase nodo
def MostrarCiudades():
    print('')
    print('--------- Lista de Ciudades ---------')
    print('')
    for ciudad in CiudadesRomania:
        print(ciudad.datos, ":",", ".join((str(ciudad_contigua.datos) for ciudad_contigua in ciudad.hijos) if ciudad.hijos else "No tiene vecinos"))

    print('')

# Busqueda en profundidad para una ruta
def BusquedaEnProdunfidad(arbol,NodoIncio,NodoFin):
    global Encontrado
    Encontrado = False
    pila = []

    print("Recorrido con algoritmo de Profundidad (DSF)")
    pila.append(NodoIncio)

    while pila:
        print("Pila: ", pila)
        NodoActual = pila.pop()
        if NodoActual not in Visitados:
            if NodoActual == NodoFin:
                print("Se encontró el destino: ", NodoActual)
                Encontrado = True
                Visitados.append(NodoActual)
                print("Ciudades Visitados: ", Visitados)
                print("Iteraciones: " +str(len(Visitados)))
                ReiniciarVisitados()

            else:
                print("Ciudad Actual: ", NodoActual)
                Visitados.append(NodoActual)

        for ciudad in arbol:
            if ciudad.nombre_ciudad == NodoActual:
                for vecinos in ciudad.hijos:
                    if vecinos.nombre_ciudad not in Visitados:
                        pila.append(vecinos.nombre_ciudad)

        if Encontrado == True:
            break

#Reiniciar Visitados
def ReiniciarVisitados():
    del Visitados[:]

ViajeRomania = ('Arad-Zerind Sibiu Timisoara*'
                'Zerind-Arad Oradea*'
                'Sibiu-Faragas RimnicuVilcea Arad*'
                'Timisoara-Lugoj Arad*'
                'Oradea-Sibiu Zerind*'
                'Faragas-Bucharest Sibiu*'
                'RimnicuVilcea-Craiova Pitesti Sibiu*'
                'Lugoj-Mehadia Timisoara*'
                'Mehadia-Dubreta Lugoj*'
                'Dubreta-Craiova Mehadia*'
                'Craiova-RimnicuVilcea Pitesti Dubreta*'
                'Pitesti-Bucharest RimnicuVilcea Craiova*'
                'Bucharest-Pitesti Faragas Giurgiu Urziceni*'
                'Giurgiu-Bucharest*'
                'Urziceni-Bucharest Vaslui Hirsova*'
                'Hirsova-Urziceni Eforie*'
                'Eforie-Hirsova*'
                'Vaslui-Urziceni Iasi*'
                'Iasi-Vaslui Neamt*'
                'Neamt-Iasi*')

NodosArbol = ConvertirRutaADiccionario()
CiudadesRomania = DiccionarioANodos()
Visitados = []
busquedas = BusquedaEnProdunfidad(CiudadesRomania, 'Arad', 'Bucharest')

