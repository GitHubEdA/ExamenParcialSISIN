import queue as cola


# Nodo con constructor y un metodo para agregar a la pila
class Nodo(object):
    def __init__(self, nombre_ciudad):
        self.nombre_ciudad = nombre_ciudad
        self.hijos = []
        self.is_visited = False

    def agregar_nodo_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self):
        return self.nombre_ciudad


# Separa los datos de ViajeRomania y los ingresa a un diccionario
def ConvertirRutaADiccionario(rutas, dict={}):
    rutas = rutas.split('*')
    for ruta in rutas:
        if ruta == '':
            break
        parent, children = ruta.split('-')
        dict[parent] = children.split(' ')
    return dict


# Funcion que de diccionario lo convierte en un nodo con sub nodos (arbol)
def DiccionarioANodos():
    arbol = {}
    for ciudad in NodosArbol:
        arbol[ciudad] = Nodo(ciudad)

    for parent, children in NodosArbol.items():
        for child in children:
            arbol[parent].agregar_nodo_hijo(arbol[child])

    return arbol


# Busqueda en profundidad para una ruta
def BusquedaEnProdunfidad(arbol, ciudad_origen, ciudad_destino):
    pila = []

    print("Recorrido con algoritmo de Profundidad (DSF)")
    pila.append(arbol[ciudad_origen])

    while pila:
        ciudad_actual = pila.pop()

        if ciudad_actual.nombre_ciudad not in CiudadesVisitadas:
            CiudadesVisitadas.append(ciudad_actual.nombre_ciudad)
            if ciudad_actual.nombre_ciudad == ciudad_destino:
                break
            else:
                print("Ciudad Actual: ", ciudad_actual)

        for ciudad in arbol.values():
            if ciudad.nombre_ciudad == ciudad_actual.nombre_ciudad:
                for child in ciudad.hijos:
                    if child.nombre_ciudad not in CiudadesVisitadas:
                        pila.append(child)

def RutasDeProfundidad(arbol, ciudad_origen, ciudad_destino):
    dict = {}
    for ciudad in arbol.values():
        dict[ciudad.nombre_ciudad] = []
        for child in ciudad.hijos:
            dict[ciudad.nombre_ciudad].append(str(child))
    pila = [(ciudad_origen, [ciudad_origen])]
    while pila:
        (ciudad_actual, ruta) = pila.pop()
        valids = [hijo for hijo in dict[ciudad_actual] if hijo not in ruta]
        for siguiente in valids:
            if siguiente == ciudad_destino:
                yield ruta + [siguiente]
            else:
                pila.append((siguiente, ruta + [siguiente]))

# Reiniciar Visitados
def ReiniciarVisitados():
    del CiudadesVisitadas[:]


ViajeRomania = ('Cajamarca-Chiclayo Trujillo Huaraz*'
             'Chiclayo-Piura Cajamarca Trujillo*'
             'Piura-Tumbes Chiclayo*'
             'Tumbes-Piura*'
             'Trujillo-Chiclayo Cajamarca Huaraz Lima*'
             'Huaraz-Cajamarca Trujillo Lima Huanuco*'
             'Huanuco-Huaraz Pasco*'
             'Pasco-Huanuco Lima Junin*'
             'Junin-Pasco Lima Cuzco Huancavelica Cuzco*'
             'Cuzco-Junin Huancavelica Abancay*'
             'Abancay-Cuzco Huancavelica Ica*'
             'Ica-Abancay Huancavelica Lima*'
             'Lima-Ica Huancavelica Junin Pasco Huaraz Trujillo*'
             'Huancavelica-Ica Lima Junin Abancay*')

NodosArbol = ConvertirRutaADiccionario(ViajeRomania)
CiudadesRomania = DiccionarioANodos()
CiudadesVisitadas = []
busquedas = BusquedaEnProdunfidad(CiudadesRomania, 'Cajamarca', 'Cuzco')
rutasVisitadas = RutasDeProfundidad(CiudadesRomania, 'Cajamarca', 'Cuzco')

validRoutes = []

for ruta in rutasVisitadas:
    validRoutes.append(str(ruta))

all_routes = list(dict.fromkeys(validRoutes))

counter = 0
for route in all_routes:
    print(f"Ruta: {counter} - {route}")
    counter = counter + 1
