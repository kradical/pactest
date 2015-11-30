from enum import Enum


class GameComponents(Enum):
    food = '*'
    wall = '#'
    pacman = 'P'
    shadow = 's'


class Maze:
    def __init__(self, input_filename):
        # must be a valid maze
        self.xlen = 0
        self.ylen = 0
        self.values = []
        self.read_input(input_filename)
        self.graph = Graph(self.values, self.xlen, self.ylen)
        self.live = True
    
    def read_input(self, file_name):
        with open(file_name, 'r') as fp:
            # TODO validate it is a well formed maze
            # TODO error no pacman or ghosts!!
            # try to validate not square/rectangular maze
            for line in fp:
                self.ylen += 1
                current_line_len = 0
                for char in line.strip():
                    current_line_len += 1
                    self.values.append(GameComponents(char))
                if current_line_len > self.xlen:
                    self.xlen = current_line_len
            
    def print_maze(self):
        maze_string = ''.join(map(lambda x: x.value, self.values))
        print('\n'.join(maze_string[i:i+self.xlen] for i in range(0, len(maze_string), self.xlen)), end='\n\n')


class Graph:
    def __init__(self, maze_values, x, y):
        self.num_nodes = x * y
        self.adj = [[] for i in range(self.num_nodes)]
        self.initialize_edges(maze_values, x, y)

    def initialize_edges(self, maze_values, x, y):
        for ndx in range(self.num_nodes):
            if maze_values[ndx] != GameComponents.wall:
                for neighbour in (ndx + 1, ndx + x, ndx - 1, ndx - x):
                    if maze_values[neighbour] != GameComponents.wall:
                        self.adj[ndx].append(neighbour)


# eventually extend to all the pacman ghosts 
# shadow chases pacman directly       
class Shadow:
    def __init__(self, maze_values):
        self.location = maze_values.index(GameComponents.shadow)
        self.standing_on = GameComponents.food

    def move(self, maze):
        dist = [float('inf') for x in maze.values]
        parent = [None for x in maze.value]

        node_queue = []

        dist[self.location] = 0
        node_queue.append(self.location)

        while node_queue:
            current = node_queue.pop(0)
            for node in maze.graph.adj[current]:
                if maze.values[node] == GameComponents.pacman:
                    pass
                if dist[node] == float('inf'):
                    dist[node] = dist[current] + 1
                    parent[node] = current
                    node_queue.append(node)


class PacMan:
    def __init__(self, maze_values):
        self.location = maze_values.index(GameComponents.pacman)

    def move(self, user_move):
        user_move()