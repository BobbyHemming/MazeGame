import pygame
import random
import numpy
from Node import Node
from Heuristic import heuristic
import pygame.freetype
from Vector import Vector
from CollisionFinder import collision_detection
import math
game_border = 10


class Wall(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.image = pygame.Surface((rect[2], rect[3]))
        self.image.fill((0, 200, 0))
        self.rect = self.image.get_rect(topleft=(rect[0], rect[1]))
        self.rect = pygame.Rect(rect)

    def draw(self, win):
        wall_colour_green = (0, 200, 0)
        rand_num = numpy.random.random()
        # pygame.draw.rect(win, (rand_num*100, rand_num*100, rand_num*100), (self.rect.x, self.rect.y, 16, 16))
        pygame.draw.rect(win, wall_colour_green, self.rect)


class Maze:

    def __init__(self, gridsize, squaresize):
        self.gridsize = gridsize
        self.squaresize = squaresize
        self.start = self.set_start_finish()[0]
        self.finish = self.set_start_finish()[1]
        self.maze = [[0 for x in range(int(self.gridsize / self.squaresize))] for y in
                     range(int(self.gridsize / self.squaresize))]
        self.walls = []
        # self.walls = [Wall((350, 100, 2, 200))]

    def build_walls(self):
        """A function that creates wall objects at random nodes across the maze it also
        calculates the heuristic values at each node for the A* Algorithm"""
        global game_border
        wall_width = 1
        number_squares = int(self.gridsize/self.squaresize)

        for col in range(number_squares):
            for row in range(number_squares):

                rect1 = (game_border+col*self.squaresize, game_border+row*self.squaresize, wall_width, self.squaresize)
                rect2 = (game_border+col*self.squaresize, game_border+row*self.squaresize, self.squaresize, wall_width)
                x, y = game_border + int(col*16), game_border + int(16*row)

                walls_on = True
                number = numpy.random.random()
                wall_pos_str = ''

                node_wall = 0
                if 0.98 > number > 0.5 and walls_on:
                    self.walls.append((Wall(rect1)))
                    wall_pos_str = 'left'
                    node_wall = Wall(rect1)
                elif 0.02 < number < 0.5 and walls_on:
                    self.walls.append((Wall(rect2)))
                    wall_pos_str = 'top'
                    node_wall = Wall(rect2)

                self.maze[col][row] = Node(x, y, self.squaresize, heuristic(Vector(x, y), self.finish, 16), wall_pos_str, node_wall)

    def draw_walls(self, win):
        """A function that draws the walls of the maze, the star and
        finish points and any other objects contained within the maze"""

        # Define colours to be used:
        wall_colour_green = (0, 200, 0)
        wall_colour_bright_green = (0, 255, 0)
        for wall in self.walls:
            wall.draw(win)
        pygame.draw.rect(win, wall_colour_green, (10, 10, 720, 720), 2)

        # Start Finish blocks
        rand_colour = (numpy.random.random()*255, numpy.random.random()*255, numpy.random.random()*255)
        pygame.draw.rect(win, rand_colour, (self.start.x+2, self.start.y+2, 12, 12))
        pygame.draw.rect(win, rand_colour, (self.finish.x+2, self.finish.y+2, 12, 12))

    def collision_checker(self, player):
        """Looks for player collisions with walls, if collision reset
        to player to a valid position. If no collison, move the player"""
        #  TODO fix small bug when moving up and left into walls, collision detected, but not dealt with...
        wall_collisions = collision_detection(player, self.walls)
        if wall_collisions[1]:
            for wall in wall_collisions[0]:
                if player.vel.x > 0:  # Player is moving to the right
                    player.pos.x = wall.rect.left - player.size - 1
                    player.vel.x = 0
                elif player.vel.x < 0:  # Player is moving to the left
                    player.pos.x = wall.rect.right + 1
                    player.vel.x = 0
                if player.vel.y > 0:  # Player is moving to the bottom
                    player.pos.y = wall.rect.top - player.size - 1
                    player.vel.y = 0
                elif player.vel.y < 0:  # Player is moving to the top
                    player.vel.y = 0
                    player.pos.y = wall.rect.bottom + 1
            pygame.time.wait(1)

        else:
            player.update()

    def set_start_finish(self):
        number = numpy.random.random()
        number_squares = self.gridsize/self.squaresize
        random_start = 90 - 2*number*number_squares
        random_finish = 630 + 2*numpy.random.random()*number_squares
        return Vector(42, 42), Vector(698, 698)



















# """vvvvvvvvvvv Test purposes ONLY vvvvvvvvv"""
# if 10 < row < 20 and col == 19:  # row=(10 and 19) col=19
#     rect4 = (game_border+col*self.squaresize, game_border+row*self.squaresize + self.squaresize,
#              wall_width, self.squaresize)
#     wall_pos_str = 'left'
#     self.walls.append(Wall(rect4))
#
#
# if 10 < col < 40 and row == 20:  # col=(10 and 19) row=20
#     rect3 = (game_border + col * self.squaresize, game_border + row * self.squaresize,
#     self.squaresize, wall_width)
#     wall_pos_str = 'top'
#     self.walls.append(Wall(rect3))
#
# if 19 < row < 40 and col == 19:  # row=(10 and 19) col=19
#     rect5 = (game_border+col*self.squaresize, game_border+row*self.squaresize + self.squaresize,
#              wall_width, self.squaresize)
#     wall_pos_str = 'left'
#     self.walls.append(Wall(rect5))
# """^^^^^^^^ Test purposes ONLY ^^^^^^^^^"""


