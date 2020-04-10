vertex_dict = {}

with open('./in.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        line = line.split()
        #print(line)
        vertex, vertices = line[0], line[1:]
        vertex_dict[vertex] = vertices

print(vertex_dict)