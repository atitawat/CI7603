#Initial

def read_test_file(fname):
    '''taken file then return (vertex, vertices)'''

    # Parse Vertices
    with open(fname, 'r') as file:
        for line in file:
            line = line.rstrip()
            line = line.split()
            vertex, con_nodes = line[0], line[1:]

    return (vertex, con_nodes)

class Vertex:
    '''for color: red for visited
        black for unvisited'''
    def __init__(self, n):
        self.name = n           # name of the vertex
        self.neighbors = []     # store the name of vertices that connected to the vertex

        self.distance = 9999    # distance from the source
        self.color = 'black'    # black for unvisited

    def add_neighbor(self, v):
        '''Accept a letter name of a vertex that will add it to the neighbors list'''
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    '''store all the vertices in a dictionary object'''
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        '''add vertices to the vertex dictionary
        we check whether vertex variable pased in is acctually a vertex object not accidentlly
        assign str or other type to {vertices}'''
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices: 
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        '''takes the letter name of the vertex at either end
            of that edge'''
        if u in self.vertices and v in self.vertices:
            for key, val in self.vertices.items():
                if key == u:
                    val.add_neighbor(v)
                if key == v:
                    val.add_neighbor(u)
            return True
        else:
            return False


    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].distance))

    def bfs(self, start_vert):
        queue = []
        start_vert.distance = 0
        start_vert.color = 'red'
        for v in start_vert.neighbors:
            self.vertices[v].distance = start_vert.distance + 1
            queue.append(v)

        while len(queue) > 0:
            u = queue.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    queue.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance +1

g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
