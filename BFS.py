#Initial

#def bfs(node, graph,):

#def dfs(node, graph);

def readTestFile(fname):
    lines = []
    with open(fname, 'r') as f:
        for line in f:
            lines.append(line.rstrip())
    

def main():
    dir = input('Enter your test file:')
    readTestFile(dir)

if __name__ == "__main__":
    main()