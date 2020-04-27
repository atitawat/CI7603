# Geeks for Geeks

class Graph():
    def __init__(self):
        self.vertex = {}

    # for printing the Graph vertexes
    def printGraph(self):
        for i in self.vertex.keys():
            print(i,' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))

    # for adding the edge beween two vertexes
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.keys(): # if key exists append new value
            self.vertex[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = toVertex # if key doesn't exist create new key

    def BFS(self, startVertex):
        # Take a list for stoting already visited vertexes
        visited = [False] * len(self.vertex)

        # create a list to store all the vertexes for BFS
        queue = []

        # mark the source node as visited and enqueue it
        visited[startVertex] = True
        queue.append(startVertex)

        while queue:
            startVertex = queue.pop(0)
            print(startVertex, end = ' ')

            # mark all adjacent nodes as visited and print them
            for i in self.vertex[startVertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':
    data = {}
    with open('../inn.txt', 'r') as file:
        for line in file:
            line = line.rstrip()
            line = line.split()
            vertex, conn_nodes = line[0], line[1:]
            data[vertex] = conn_nodes
    from collections import OrderedDict
    od = OrderedDict(sorted(data.items()))

    g = Graph()

    for k,v in od.items():
        g.addEdge(k, v)

    g.printGraph()
    print('BFS:')
    g.BFS(2)
    