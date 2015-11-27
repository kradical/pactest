class Maze:
    def __init__(self, input_filename):
        # must be a valid maze
        self.maze = self.read_input(input_filename)
        self.graph = Graph(self.maze)
        # self.pacman = Pacman(self.graph)
        # self.ghost = Ghost(self.graph)
    
    def read_input(self, file_name):
        with open(file_name, 'r') as fp:
            # TODO validate it is a well formed maze
            return [[x for x in line.strip()] for line in fp]
            
    def print_maze(self):
        maze_str = '\n'.join([''.join(x) for x in self.maze])
        print(maze_str, end='\n\n')
        
class Graph:
    def __init__(self, maze):
        self.nodes = self.initnodes(maze)
        self.edges = self.initedges(maze)
        for edge in self.edges:
            print(edge)
    
    def initedges(self, maze):
        result = []
        for node in self.nodes:
            for neighbour in self.neighbours(node):
                result.append(neighbour)
        return result
    
    def neighbours(self, node):
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for direction in directions:
            new_x = node.x + direction[0]
            new_y = node.y + direction[1]

            for neighbour in self.nodes:
                if neighbour.x == new_x and neighbour.y == new_y:
                    result.append(Edge(node, neighbour))
        return result
    
    def initnodes(self, maze):
        result = []
        for j, row in enumerate(maze):
            for i, cell in enumerate(row):
                if cell != '#':
                    result.append(Node(i, j, cell))
        return result

class Edge:
    def __init__(self, node1, node2):
        self.first = node1
        self.second = node2
        
class Node:
    def __init__(self, x, y, value):
        self.value = value
        self.x = x
        self.y = y
       
class Ghost:
    def __init__(self, maze):
        for i, row in enumerate(maze):
            if 'G' in row:
                self.x = i
                self.y = row.index('G')    
    
class Pacman:
    def __init__(self, maze):
        for i, row in enumerate(maze):
            if 'P' in row:
                self.x = i
                self.y = row.index('P')