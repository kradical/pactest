from pac_class import Maze
import sys


def main():
    if len(sys.argv) != 2:
        print('\ninput format:\n$ python '+sys.argv[0]+' [filename]')
        sys.exit()
    try:
        main_maze = Maze(sys.argv[1])
    except FileNotFoundError:
        print(sys.argv[1] + ' not found.')
        sys.exit()
    main_maze.print_maze()
    
if __name__ == '__main__':
    main()