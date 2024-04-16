import pygame

from game_classes import GameBoard

class GameState:
    def __init__(self):
        self.pause = False
        self.game_board = GameBoard()
        self.game_board.fill_board()
        self.prev_mouse_state = False

    def update(self, screen):    
        mouse_state = pygame.mouse.get_pressed()[0]
        self.game_board.update(pygame.mouse.get_pos(), screen, mouse_state and not self.prev_mouse_state)
        self.prev_mouse_state = mouse_state

    def draw(self, screen):
        self.game_board.draw(screen, pygame.mouse.get_pos())
