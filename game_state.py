import pygame

from game_classes import GameBoard

class GameState:
    def __init__(self, width, height, is_train=False, category_to_train=None):
        self.pause = False
        self.game_board = GameBoard(width, height, is_train=is_train, category_to_train=category_to_train)
        self.game_board.fill_board()
        self.prev_mouse_state = False

    def update(self, screen, stats_tracker): 
        if not self.pause:   
            mouse_state = pygame.mouse.get_pressed()[0]
            self.game_board.update(pygame.mouse.get_pos(), screen, mouse_state and not self.prev_mouse_state, stats_tracker)
            self.prev_mouse_state = mouse_state

    def draw(self, screen):
        if not self.pause:
            self.game_board.draw(screen, pygame.mouse.get_pos())
