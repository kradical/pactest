from enum import Enum

class GameComponents(Enum):
    food = '*'
    wall = '#'
    pacman = 'P'
    shadow = 's'

class Maze:
    def __init__(self, input_filename):
        # must be a valid maze
        self.maze = self.read_input(input_filename)
        self.graph = Graph(self.maze)
        self.pacman = Pacman(self.graph)
        self.ghosts = [Shadow(self.graph)]
        self.live = True
    
    def read_input(self, file_name):
        with open(file_name, 'r') as fp:
            # TODO validate it is a well formed maze
            # TODO error no pacman or ghosts!!
            result = []
            for row in fp:
                row_result = []
                for cell in row.strip():
                    row_result.append(GameComponents(cell))
                result.append(row_result)
            return result
            
    def print_maze(self):
        print('\n'.join([''.join(map(lambda x:x.value, row)) for row in self.maze]) + '\n\n')
        
class Graph:
    def __init__(self, maze):
        self.nodes = self.initnodes(maze)
        self.edges = self.initedges(maze)
    
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
                if cell != GameComponents.wall:
                    result.append(Node(i, j, cell))
        return result

class Edge:
    def __init__(self, node1, node2):
        self.first = node1
        self.second = node2
        
class Node:
    def __init__(self, x, y, value):
        self.game_piece = value
        self.x = x
        self.y = y

# eventually extend to all the pacman ghosts 
# shadow chases pacman directly       
class Shadow:
    def __init__(self, graph):
        for node in graph.nodes:
            if node.game_piece == GameComponents.shadow:
                self.x = node.x
                self.y = node.y
                self.standing_on = GameComponents.food

    def move(self):
        print("SMOVING")

class Pacman:
    def __init__(self, graph):
        for node in graph.nodes:
            if node.game_piece == GameComponents.pacman:
                self.x = node.x
                self.y = node.y

    def move(self, user_move):
        user_move()