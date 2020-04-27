#Author Atitawat Pol-in
# BADS 2/61 NIDA Thailand

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, from_node, to_node):
        self.graph[from_node] = to_node

    def printGraph(self):
        print(self.graph)

    def bfs(self, start, goal):
        queue = [start]
        expand = []
        while queue:

            path_length = [len(path) for path in queue]
            min_path = min(path_length)
            min_queue = [q for q in queue if len(q) == min_path]

            min_queue = sorted(min_queue, key=lambda x: x[-1])
            dequeue = min_queue.pop(0)
            queue.remove(dequeue)
            expanding = dequeue[-1]

            if expanding in expand:
                dup = '(' + expanding + ')'
                expand.append(dup)
            else:
                expand.append(expanding)

            if expanding == goal:
                list_path = [stir for stir in dequeue]
                prt_path = '-'.join(list_path)
                print('Path:', prt_path)
                print('Expand: {}'.format(" ".join(expand)))
                break

            for connecting in self.graph.get(expanding, []):
                new_path = dequeue+connecting
                if len(new_path) >= 3 and new_path[-1] == new_path[-3]:
                    continue
                else:
                    queue.append(new_path)

    def dfs(self, start, goal):
        queue = [start]
        expand = []
        while queue:

            path_length = [len(path) for path in queue]
            max_path = max(path_length) # using max instead of min
            max_queue = [q for q in queue if len(q) == max_path]

            max_queue = sorted(max_queue, key=lambda x: x[-1])
            dequeue = max_queue.pop(0)
            queue.remove(dequeue)
            expanding = dequeue[-1]

            if expanding in expand:
                dup = '(' + expanding + ')'
                expand.append(dup)
                continue # for skipping loop of death
            else:
                expand.append(expanding)
            if expanding == goal:
                list_path = [stir for stir in dequeue]
                prt_path = '-'.join(list_path)
                print('Path:', prt_path)
                print('Expand: {}'.format(" ".join(expand)))
                break

            for connecting in self.graph.get(expanding, []):
                new_path = dequeue+connecting
                if len(new_path) >= 3 and new_path[-1] == new_path[-3]:
                    continue
                else:
                    queue.append(new_path)

# Main
def main():
    print('''How to use program
1.) Enter file directory:
2.) Enter Search Algorithm Start Stop (BFS or DFS A Z): 
3.) Type "end" when you finish
    ''')

    while True:
        print('Enter file directory (.txt): ')
        _input = input('> ').lower()

        if _input == 'end':
            data = {}
            break

        # Create initial object Parser
        elif '.txt' in _input:
            data = {}

            with open(_input, 'r') as file:
                for line in file:
                    line = line.rstrip()
                    line = line.split()
                    vertex, conn_nodes = line[0], line[1:]
                    data[vertex] = conn_nodes

            g = Graph() # Create Graph object

            for k,v in data.items():
                g.addEdge(k, v)
            print('Graph is Ready!')

            while True:
                print('Enter Search Algorithm')
                _input = input('> ').upper()
                split_input  = _input.split()

                if _input == 'END':
                    return

                elif len(split_input) == 3:
                    mode, start, stop = split_input[0], split_input[1], split_input[2]

                    if mode == 'BFS':
                        g.bfs(start, stop)
                    elif mode == 'DFS':
                        g.dfs(start, stop)

                else:
                    print('Unknown')

        else:
            print('Unknown')


if __name__ == "__main__":
    main()
