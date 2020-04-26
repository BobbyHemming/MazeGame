import pygame
import numpy as np
import Player
import Maze
import sys
from astar import a_star
from Vector import Vector
from Button import Button
startButton = Button(75, 50, 100, 30, "dark", "Start Game")


def redraw_menu_screen(win):
    win.fill((0, 0, 0))
    startButton.draw(win)


def menu_screen():
    running = True
    while running:

        redraw_menu_screen(menu_win)
        pygame.display.update()

        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.display.quit(), pygame.quit(), sys.exit()
                running = False

            if event.type == pygame.MOUSEMOTION:

                if startButton.isOver(mousePos):
                    startButton.colour = "light"
                else:
                    startButton.colour = "dark"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.isOver(mousePos):
                    pygame.quit()
                    running = False
                    break



        # pygame.display.update()


def redrawscreen(win, maze):
    # win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (0, 0, width, height), 10)
    pygame.display.flip()
    pygame.display.set_caption('Maze Game')
    player.draw(win)
    maze.draw_walls(win)
    pygame.display.update()


def main():
    running = True
    clock = pygame.time.Clock()
    collision = False
    colour = (255, 0, 0)

    # Shortest path testing
    maze = init_maze(gridsize, squaresize)
    redrawscreen(win, maze)
    start = maze.maze[2][2]
    finish = maze.maze[43][43]
    path = a_star(start, finish, maze.maze, win)
    print(path)

    while path == 0:
        print('Next Maze build attempt!')
        win.fill((0, 0, 0))
        redrawscreen(win, maze)
        maze = init_maze(gridsize, squaresize)
        start2 = maze.maze[2][2]
        finish2 = maze.maze[43][43]
        path = a_star(start2, finish2, maze.maze, win)

    for node in path:
        node.draw_node(win, colour)
    win.fill((0, 0, 0))

    while running:
        clock.tick()
        redrawscreen(win, maze)

        gamestate = True
        if not gamestate:
            #  TODO add endgame code here...
            pass

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.display.quit(), pygame.quit(), sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mousepos = pygame.mouse.get_pos()

            if keys[pygame.K_UP]:
                player.vel.x = 0
                player.vel.y = -4
            elif keys[pygame.K_DOWN]:
                player.vel.x = 0
                player.vel.y = 4
            elif keys[pygame.K_LEFT]:
                player.vel.x = -4
                player.vel.y = 0
            elif keys[pygame.K_RIGHT]:
                player.vel.x = 4
                player.vel.y = 0
            elif keys[pygame.K_f]:
                for node in path:
                    node.draw_node(win, colour)
                pygame.time.wait(800)
                win.fill((0, 0, 0))
                redrawscreen(win, maze)

        pygame.draw.rect(win, (0, 0, 0), (player.pos.x, player.pos.y, 8, 8))
        maze.collision_checker(player)
        finish.draw_node(win, colour)

        pygame.time.wait(1)
        redrawscreen(win, maze)


width, height = 740, 740
pygame.display.set_caption('Maze Game')
win = pygame.display.set_mode((width, height))
menu_win = pygame.display.set_mode((250, 400))

gridsize, squaresize = 720, 16
player = Player.Player(16, 16, 8)
# TODO maybe build small maze initialising function here...
# maze = Maze.Maze(gridsize, squaresize)
# maze.build_walls()


def init_maze(maze_gridsize, maze_squaresize):
    new_maze = Maze.Maze(maze_gridsize, maze_squaresize)
    new_maze.build_walls()
    return new_maze


if __name__ == '__main__':
    pygame.init()
    menu_screen()
    pygame.init()
    pygame.display.set_caption('Maze Game')
    win = pygame.display.set_mode((width, height))
    main()
    pygame.quit()














