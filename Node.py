from Vector import Vector
import pygame
import math


class Node:
    def __init__(self, x, y, squaresize, heuristic_value, wall_pos_str, node_wall):
        self.pos = Vector(x, y)
        self.h_value = heuristic_value
        self.g_score = math.inf
        self.came_from = 0
        self.f_score = math.inf
        self.squaresize = squaresize
        self.wall = wall_pos_str
        self.node_wall = node_wall

    def draw_node(self, win, colour):
        pygame.draw.rect(win, colour, (self.pos.x+4, self.pos.y+4, 8, 8))
        pygame.display.update()

        # font = pygame.font.Font('freesansbold.ttf', 8)
        # text = font.render(f'{self.h_value}', True, (255, 255, 255))
        # text_rect = text.get_rect()
        # text_rect.center = (self.pos.x, self.pos.y)
        # win.blit(text, text_rect)




