#Initial

def read_test_file(fname) -> dict:
    '''taken file then return dict {vertex: [connecting vertices]}'''
    lines = []
    vertex = {}

    with open(fname, 'r') as file:
        for line in file:
            lines.append(line.rstrip())

    vertex = lambda lines: {lines[0]: lines[1:-1]}

    return vertex

class Vertex:
    
   def __init__(self, name, neighbors, distance, color):
      self.name = name
      self.neighbors = [next for node in neighbors]




    

'''def main():
    dir = input('Enter your test file:')
    read_test_file(dir)

if __name__ == "__main__":
    main()'''