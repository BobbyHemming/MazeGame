import pygame
from pygame.math import Vector2
from Vector import Vector
gridsize = 720
game_border = 10


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector(x, y)
        self.vel = Vector(0, 0)
        self.size = size
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size, self.size)

    def draw(self, win):
        pygame.draw.rect(win, (0, 200, 0), (self.pos.x, self.pos.y, self.size, self.size))

    def update(self):
        if Vector(game_border, game_border) < self.pos + self.vel < Vector(gridsize, gridsize):
            self.pos.x += self.vel.x
            self.pos.y += self.vel.y


def corner_coords(player, win):

    font = pygame.font.Font('freesansbold.ttf', 8)
    corners = [Vector(player.pos.x - 15, player.pos.y - 10), Vector(player.pos.x + 15 + player.size, player.pos.y - 10),
                   Vector(player.pos.x - 15, player.pos.y + player.size + 10),
                   Vector(player.pos.x + 15 + player.size, player.pos.y + player.size + 10)]
    text_points = [Vector(player.pos.x, player.pos.y), Vector(player.pos.x + player.size, player.pos.y),
                       Vector(player.pos.x, player.pos.y + player.size),
                       Vector(player.pos.x + player.size, player.pos.y + player.size)]
    for a in range(4):
        text = font.render(f'{(text_points[a].x, text_points[a].y)}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (corners[a].x, corners[a].y)
        win.blit(text, text_rect)


