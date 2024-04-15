import random

import pygame

from game_classes import Card, GameBoard

pygame.init()

SCREEN_SIZE_X = 720

SCREEN_SIZE_Y = 1280

circle_size = 75

mouse_pressed = False
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_SIZE_X, SCREEN_SIZE_Y])

game_board = GameBoard()

game_board.fill_board()


# Run until the user asks to quit
running = True
prev_mouse_state = False


def update(prev_mouse_state, screen, game_board):    
    mouse_state = pygame.mouse.get_pressed()[0]
    if mouse_state and not prev_mouse_state:
        game_board.draw(screen, pygame.mouse.get_pos(), True)
    else:
        game_board.draw(screen, pygame.mouse.get_pos(), False)

    game_board.update()

    return mouse_state



while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((100, 100, 100))
    prev_mouse_state = update(prev_mouse_state, screen, game_board)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
