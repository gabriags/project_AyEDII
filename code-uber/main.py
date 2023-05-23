# MAPA:
'''
Consiste de dos conjuntos <E,C>. E es un conjunto de esquinas {e1,e2,e3, ….} y C las calles que conectan dichas esquinas.
C es un conjunto de ternas ordenadas {<e1,e2,c>,<e3,e4,c>, <e2,e1,c>} que expresa la dirección y el largo de las calles (c = distancia entre e1 y e2).
'''

# 1 - Representar esquinas y calles como un grafo dirigido y ponderado mediante listas de adyacencia.

class Vertex:
    def __init__(self,key):
        self.key = key
    color = None
    parent = None
    distance = None
    f = None

class Graph:
    # vertices_list = [v1,v2,v3,...,vn]
    # edges_list = [(v1,v2),(v2,v3),...,(vi,vj)]
    def __init__(self,vertices_list,edges_list):
        self.vertices_list = vertices_list
        self.edges_list = edges_list
    
        self.adj_list = [[] for _ in range(len(self.vertices_list))]
        
        for i in range(len(edges_list)):
            edge_u = edges_list[i][0]
            edge_v = edges_list[i][1]
            weight = edges_list[i][2]
            self.adj_list[edge_u.key - 1].append((edge_v,weight))
            #self.adj_list[edges_list[i][1].key - 1].append(edges_list[i][0])
    
    def draw_graph(self):
        for i in range(len(self.adj_list)):
            print('|',i+1,'|-->',end="")
            for vertex in self.adj_list[i]:
                print('|',vertex[0].key,'(w:',vertex[1],')|',end="")
            print()


e1 = Vertex(1)
e2 = Vertex(2)
e3 = Vertex(3)
e4 = Vertex(4)
e5 = Vertex(5)
e6 = Vertex(6)

esquinas = [e1,e2,e3,e4,e5,e6]

calles = [(e1,e2,100),(e1,e4,100),(e2,e5,50),(e3,e5,150),(e3,e6,100),(e4,e2,80),(e5,e4,120)]

mapa_uber = Graph(esquinas,calles)

mapa_uber.draw_graph()

#print(mapa_uber.adj_list[4])

# DIRECCIONES

'''
Dirección: Consiste de un par de tuplas {<ex,d>, <ey,d>} donde e es una esquina dentro del mapa y d es un entero
que representa la distancia de esa dirección con la esquina e.
Ej: la dirección d1 = {<ex,10>, <ey,5>} indica que d1 esta en la siguiente posición dentro
del mapa e1___________10____________d1_______5_____e2


'''

# UBICACIONES FIJAS

'''
Consiste de una tupla <Nombre, Dirección>. Donde Dirección representa
una dirección posible en el mapa y Nombre puede ser cualquiera de estos caracteres.
● H: hospital
● A: almacén
● T: tienda
● S: supermercado
● E: escuela
● K: kiosco
● I: iglesia

'''



# UBICACIONES MOVILES

'''
Consiste de una 3-tupla <Nombre, Dirección, Monto>. Donde Dirección
representa una dirección posible en el mapa, Monto un valor numérico para indicar
saldo/tarifa y Nombre puede ser cualquiera de estos caracteres.
● P: persona
● C: auto
'''

# INDICACIONES

'''
Si dada la configuración inicial de un mapa y la ubicación en el mismo de lugares fijos y
componentes móviles (autos y personas). Implementar las siguientes funcionalidades:
1. Cargar nuevos lugares, personas y autos dentro del mapa
2. Conocer, dado un lugar, persona o auto la dirección del mismo.
3. Conocer, dado una persona que se encuentra en el mapa cuáles son los 10 autos
más cercanos que esa persona puede pagar.
4. Conocer, dado dos direcciones en el mapa cual es el camino más cercano para llegar
de uno a otro.
'''

# class HashTable():
#     def __init__(self,size):
#         self.size = size
#         self.table = [[] for _ in range(size)]
    
#     def _hash(self,address):
#         return hash(address) % self.size
    
#     # def add_location(self,name,address,amount):
#     #     print(address)


#     #     # index = self._hash(address)
#     #     # if name[0] != 'P' or name[0] != 'C':
#     #     #     self.table[index].append((name,address))
#     #     # else:
#     #     #     self.table[index].append((name,address,amount))


direcciones_mapa = {}

def add_location(map,name,address,amount):
    map[name] = {'address':address,'amount': amount}

def get_address(map,name):
    address = map[name]['address']
    return address

def at_same_location(map,name1,name2):
    if get_address(map,name1) == get_address(map,name2):
        return True
    return False



add_location(direcciones_mapa,'H1',[(e1,10),(e2,5)],None)
add_location(direcciones_mapa,'C1',[(e1,8),(e2,5)],1200)
add_location(direcciones_mapa,'P1',[(e3,10),(e5,5)],200)

print(at_same_location(direcciones_mapa,'H1','C1'))



# print(get_address(direcciones_mapa,'C1'))
# print(at_same_location(direcciones_mapa,'H1','C1'))

# print(direcciones_mapa.keys())
