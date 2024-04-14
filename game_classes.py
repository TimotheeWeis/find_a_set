import pygame

class Card:
    def __init__(self, color, shape, number, shading, width=100, height=50):
        self.color = color
        self.shape = shape
        self.number = number
        self.shading = shading,
        self.width = width
        self.height = height

        self.surface = pygame.Surface((width, height))
        self.surface.fill((50, 50, 50))

    def draw(self, screen, x, y):
        screen.blit(self.surface, (x, y))