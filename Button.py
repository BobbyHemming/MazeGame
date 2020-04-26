import pygame

pygame.font.init()
font = pygame.font.SysFont("comicsans", 40)


class Button:

    def __init__(self, x, y, width, height, colour="", text=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text

    def draw(self, win):

        if self.text != "":
            if self.colour == "dark":
                text = font.render(self.text, 1, (200, 200, 200))
                win.blit(text, ((self.x + int(self.width / 2 - text.get_width() / 2)), int(self.y + (self.height / 2 - text.get_height() / 2))))
            elif self.colour == "light":
                text = font.render(self.text, 1, (255, 255, 255))
                win.blit(text, ((self.x + int(self.width/2 - text.get_width()/2)), int(self.y + (self.height/2 - text.get_height()/2))))

    def isOver(self, pos):

        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


