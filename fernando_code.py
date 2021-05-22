import queue as cola
# Clase Nodo con su constructor y un metodo para agregar a los hijos
class Nodo(object):
    def __init__(self, datos):
        self.datos = datos
        self.hijos = []

    def agregar_nodo_hijo(self, hijo):
        self.hijos.append(hijo)

#Funcion que se encargara de de traducir el texto en un diccionario para poder despues utilizar el diccionario
def IngresarRutaADiccionario():
    NodoArbol = [nodos.split('-') for nodos in viajeRumania.split('*')][:-1]
    NodoArbol = {str(NodoPadre): [str(NodoHijo) for NodoHijo in NodoHijos.split()]
                  for NodoPadre, NodoHijos in NodoArbol}
    return NodoArbol

#Funcion que de diccionario lo hara un nodo con sub nodos para poder utilizarlo
def IngresarDiccionarioAClaseNodo():
    nodosGenerados = {nodo: Nodo(nodo) for nodo in NodosArbol}
    for NodoPadre, NodoHijos in NodosArbol.items():
        for NodoHijo in NodoHijos:
            nodosGenerados[NodoPadre].agregar_nodo_hijo(nodosGenerados[NodoHijo])

    Ciudades = nodosGenerados.values()
    return  Ciudades

def IngresarViajeADiccionario():
    NodoArbol = [nodos.split('-') for nodos in viajeRumaniaCostos.split('*')][:-1]
    NodoArbol = {str(NodoPadre): set([str(NodoHijo) for NodoHijo in NodoHijos.split()])
                  for NodoPadre, NodoHijos in NodoArbol}
    return NodoArbol
# Imprimimos la ciudades que estan dentro de la Clase nodo
def MostrarCiudades():
    print("-----------------------------------------")
    print("-- Lista de ciudades y ciudades vecinas--")
    print("-----------------------------------------")
    for ciudad in ListaCiudades:
        print(ciudad.datos, ":",", ".join((str(vecinos.datos) for vecinos in ciudad.hijos) if ciudad.hijos else "No tiene vecinos"))

    print("")

#Reiniciar Visitados
def ReiniciarVisitados():
    del Visitados[:]

#Busqueda en profundidad encuentra una ruta y muestra como lo encuentra mediante la Clase Nodo, solo sirve para una ruta
def BusquedaProdunfidad(grafo,Comienzo,NodoBuscado):
    global Encontrado
    Encontrado = False
    pila = []

    print("Lista de recorrido en Profundidad")
    pila.append(Comienzo)
    print("----------------------------")
    MostrarCiudades()
    print("----------------------------")

    while pila:
        print("Pila: ",pila)
        NodoActual = pila.pop()
        if NodoActual not in Visitados:
            if NodoActual == NodoBuscado:
                print("Ciudad Actual: " + NodoActual + " Se Encontro")
                Encontrado = True
                Visitados.append(NodoActual)
                print("Ciudades Visitados: ", Visitados)
                print("Iteraciones: " +str(len(Visitados)))
                ReiniciarVisitados()
                print("----------------------------")

            else:
                print("Ciudad Actual: " + NodoActual)
                Visitados.append(NodoActual)

        for ciudad in grafo:
            if ciudad.datos == NodoActual:
                for vecinos in ciudad.hijos:
                    if vecinos.datos not in Visitados:
                        pila.append(vecinos.datos)

        if Encontrado == True:
            break

#Busqueda en amplitud encuentra una ruta y muestra como lo encuentra la Clase Nodo, solo sirve para una ruta
def BusquedaAmplitud(grafo,Comienzo,NodoBuscado):
    global Encontrado
    Encontrado = False
    cola = []

    print("Lista de recorrido en Amplitud")
    cola.append(Comienzo)

    print("----------------------------")
    MostrarCiudades()
    print("----------------------------")
    while cola:
        print("cola: ", cola)
        NodoActual = cola.pop(0)
        if NodoActual not in Visitados:
            if NodoActual == NodoBuscado:
                print("Nodo Actual: " + NodoActual + " Se Encontro")
                Encontrado = True
                Visitados.append(NodoActual)
                print("Nodos Visitados: ", Visitados)
                print("Iteraciones: " + str(len(Visitados)))
                ReiniciarVisitados()
            else:
                print("Nodo Actual: " + NodoActual)
                Visitados.append(NodoActual)

        for ciudad in grafo:
            if ciudad.datos == NodoActual:
                for vecinos in ciudad.hijos:
                    if vecinos.datos not in Visitados:
                        cola.append(vecinos.datos)

        if Encontrado == True:
            break;

#Hace la busqueda en profundidad mediante la clase Nodo, convirtiendolo en un diccionario para que se mas facil la busqueda
#Y alamacene todas las rutas
def RutasDeProfundidad(grafo, Comienzo, NodoBuscado):
    NodoADiccionario = {ciudad.datos: {str(vecinos.datos) for vecinos in ciudad.hijos}
                        for ciudad in grafo}
    pila = [(Comienzo, [Comienzo])]
    while pila:
        (NodoActual, ruta) = pila.pop()
        for siguiente in NodoADiccionario[NodoActual] - set(ruta):
            if siguiente == NodoBuscado:
                yield ruta + [siguiente]
            else:
                pila.append((siguiente, ruta + [siguiente]))

#Hace la busqueda en amplitud mediante la clase Nodo, convirtiendolo en un diccionario para que se mas facil la busqueda
#Y alamacene todas las rutas
def RutasAmplitud(grafo, Comienzo, NodoBuscado):
    NodoADiccionario = {ciudad.datos: {str(vecinos.datos) for vecinos in ciudad.hijos}
                        for ciudad in grafo}
    cola = [(Comienzo, [Comienzo])]
    while cola:
        (NodoActual, ruta) = cola.pop(0)
        for siguiente in NodoADiccionario[NodoActual] - set(ruta):
            if siguiente == NodoBuscado:
                yield ruta + [siguiente]
            else:
                cola.append((siguiente, ruta + [siguiente]))

#Hace la busqueda en amplitud mediante un diccionario ya definido y almacena la ruta con menor costo
def RutaCostos(grafo, Comienzo, NodoBuscado):
    if Comienzo not in grafo:
        return print("La ciudad que busca no esta en el mapa!")
    if NodoBuscado not in grafo:
        return print("No se puede encontrar una ruta")

    colaPrioridad = cola.PriorityQueue()
    colaPrioridad.put((0, [Comienzo]))

    while not colaPrioridad.empty():
        Nodo = colaPrioridad.get()
        NodoActual = Nodo[1][len(Nodo[1]) - 1]

        if NodoBuscado in Nodo[1]:
            print("La ruta que debes tomar es: " + str(Nodo[1]) + ", el costo del viaje es: " + str(Nodo[0]))
            break

        costo = Nodo[0]
        for nodoVecino in grafo[NodoActual]:
            visitados = Nodo[1][:]
            visitados.append(nodoVecino)
            colaPrioridad.put((costo + grafo[NodoActual][nodoVecino], visitados))

#Mostramos todas las rutas de dsf con Inicio Arad - Bucharest o si esque el usuario ingresa una ciudadInicio o Destino
def MostrarRutasDSF(Comienzo, Destino):
    MostrarCiudades()
    print("------------------------------")
    print("-- Busqueda por Profundidad --")
    print("------------------------------")
    contador = 1
    if Comienzo == "" or Destino == "":
        RutasVisitadas = RutasDeProfundidad(ListaCiudades, 'Arad', 'Bucharest')
    else:
        RutasVisitadas = RutasDeProfundidad(ListaCiudades, Comienzo, Destino)

    for rutas in RutasVisitadas:
        print("Ruta N° "+str(contador)+" "+str(rutas))
        print("Ciudades visitadas: ",len(rutas),rutas)
        contador=contador+1
        print("-----------------")
    print("")

#Top 3 rutas de dsf(Arad - Bucharest)
def MostrarTop3RutasDSF():
    print("-----------------------------")
    print("---- Top 3 rutas por DSF ----")
    print("-----------------------------")
    contador = 1
    RutasVisitadas = RutasDeProfundidad(ListaCiudades, 'Arad', 'Bucharest')
    rutasOrdenadas = sorted(RutasVisitadas, key=len)
    for top3 in rutasOrdenadas[:3]:
        print("Ruta N° " + str(contador) + " " + str(top3))
        print("Ciudades visitadas: ", len(top3), top3)
        contador = contador + 1
        print("-----------------")
    print("")

#Mostramos todas las rutas de bsf con Inicio Arad - Bucharest o si esque el usuario ingresa una ciudadInicio o Destino
def MostrarRutasBSF(Comienzo, Destino):
    print("-----------------------------")
    print("--- Busqueda por Amplitud ---")
    print("-----------------------------")
    contador = 1
    if Comienzo == "" or Destino == "":
        RutasVisitadas = RutasAmplitud(ListaCiudades, 'Arad', 'Bucharest')
    else:
        RutasVisitadas = RutasAmplitud(ListaCiudades, Comienzo, Destino)
    for rutas in RutasVisitadas:
        print("Ruta N° "+str(contador)+" "+str(rutas))
        print("Ciudades visitadas: ",len(rutas),rutas)
        contador=contador+1
        print("-----------------")
    print("")

#Top 3 rutas de bsf(Arad - Bucharest)
def MostrarTop3RutasBSF():
    print("-----------------------------")
    print("---- Top 3 rutas por BSF ----")
    print("-----------------------------")
    contador = 1
    RutasVisitadas = RutasAmplitud(ListaCiudades, 'Arad', 'Bucharest')
    rutasOrdenadas = sorted(RutasVisitadas, key=len)
    for top3 in rutasOrdenadas[:3]:
        print("Ruta N° " + str(contador) + " " + str(top3))
        print("Ciudades visitadas: ", len(top3), top3)
        contador = contador + 1
        print("-----------------")
    print("")

#Mostramos la ruta con menor costo de ucs con Inicio Arad - Bucharest o si esque el usuario ingresa una ciudadInicio o Destino
def MostrarRutasUCS(Comienzo, Destino):
    print("-----------------------------")
    print("--- Busqueda por Costos ---")
    print("-----------------------------")
    contador = 1
    if Comienzo == "" or Destino == "":
        RutaCostos(ViajeRumaniaCostos, 'Arad', 'Bucharest')
    else:
        RutaCostos(ViajeRumaniaCostos, Comienzo, Destino)

    print("-----------------")
    print("")

#Ingresos de Menu de DSF O BSF
def DSFOBSF():
    print("Estas rutas estan definidas con Ciudad Origen Arad a Ciudad Destino Bucharest")
    estrategia = input("Escriba la estrategia(DSF o BSF): ")
    if estrategia == "DSF" or estrategia == "dsf":
        MostrarRutasDSF("","")
        MostrarTop3RutasDSF()
    elif estrategia == "BSF" or estrategia == "bsf":
        MostrarRutasBSF("","")
        MostrarTop3RutasBSF()
    else:
        print("Solo puedes digitar -> BSF o bsf - DSF o dsf")

#Ingresos de Menu de UCS
def UCS():
    print("Estas rutas estan definidas con Ciudad Origen Arad a Ciudad Destino Bucharest")
    MostrarRutasUCS("","")

#Ingresos de Menu para escoger la ciudad que queremos mediante las busquedas dsf,bsf o ucs
def EscogerCiudadInicioACiudadDestino():
    print("Te mostraremos las ciudades que puedes escoger y destinos: ")
    print("Ciudades: ",[ciudades.datos for ciudades in ListaCiudades])
    print("Ingresar la ciudad como se muestra en la lista de arriba")

    ciudadInicio = input("Ingresa la ciudad de inicio: ")
    ciudadDestino = input("Ingresa la ciudad de destino: ")

    estrategia = input("Escriba la estrategia(DSF,BSF,UCS): ")
    if estrategia == "DSF" or estrategia == "dsf":
        MostrarRutasDSF(ciudadInicio,ciudadDestino)
    elif estrategia == "BSF" or estrategia == "bsf":
        MostrarRutasBSF(ciudadInicio,ciudadDestino)
    elif estrategia == "UCS" or estrategia == "ucs":
        MostrarRutasUCS(ciudadInicio,ciudadDestino)
    else:
        print("Solo puedes digitar -> BSF o bsf - DSF o dsf")
#Lo colocamos para cargarlo
viajeRumania = ('Arad-Sibiu Zerind Timisoara*'
                'Zerind-Oradea Arad*'
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
#Diccionario de ciudades con costos
ViajeRumaniaCostos = {
    'Arad':{'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Sibiu': {'Faragas': 99, 'RimnicuVilcea': 80, 'Arad': 140},
    'Timisoara': {'Lugoj': 111, 'Arad': 118},
    'Oradea': {'Sibiu': 151, 'Zerind': 71},
    'Faragas': {'Bucharest': 211, 'Sibiu': 99},
    'RimnicuVilcea': {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Dubreta': 75, 'Lugoj': 70},
    'Dubreta': {'Craiova': 120, 'Mehadia': 75},
    'Craiova': {'RimnicuVilcea': 146, 'Pitesti': 138, 'Dubreta': 120},
    'Pitesti': {'Bucharest': 101, 'RimnicuVilcea': 97, 'Craiova': 38},
    'Bucharest': {'Pitesti': 101, 'Faragas': 211, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}
# Guardamos el texto de viaje a rumania en un diccionario
NodosArbol = IngresarRutaADiccionario()
# Alamacenamos las Ciudades del diccionario en la Clase Nodo
ListaCiudades = IngresarDiccionarioAClaseNodo()
Visitados = []
opcion = 0
while opcion != 4:
    print("""
    -----------------------------------
    ----------- Menu de Rutas ---------
    -----------------------------------
    [1]. Rutas con BSF y DSF
    [2]. Rutas Con UCS
    [3]. Buscar Ruta con cualquier ciudad
    [4]. Salir
    """)
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        DSFOBSF()
    elif opcion == 2:
        UCS()
    elif opcion == 3:
        EscogerCiudadInicioACiudadDestino()
    elif opcion == 4:
        exit(0)
    else:
        print("Escoja un opcion correcta")
