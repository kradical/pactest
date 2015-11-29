from pac_class import Maze
import sys
import time


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
    print(main_maze.pacman.x, main_maze.pacman.y)
    
    while main_maze.live:
        time.sleep(1)
        for ghost in main_maze.ghosts:
            ghost.move()
        main_maze.pacman.move(lambda: print("PMOVING") )
        main_maze.print_maze()

if __name__ == '__main__':
    main()