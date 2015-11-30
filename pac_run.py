from pac_class import Maze, Shadow, PacMan
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

    ghosts = [Shadow(main_maze.values)]
    player1 = PacMan(main_maze.values)
    main_maze.print_maze()
    
    while main_maze.live:
        time.sleep(1)
        player1.move(player_move)
        for ghost in ghosts:
            ghost.move(main_maze)
        main_maze.print_maze()


def player_move():
    pass

if __name__ == '__main__':
    main()