import random

import pygame

from game_state import GameState

pygame.init()

SCREEN_SIZE_X = 720

SCREEN_SIZE_Y = 1280

circle_size = 75

mouse_pressed = False
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_SIZE_X, SCREEN_SIZE_Y])

game_state = GameState()

# Run until the user asks to quit
running = True


clock = pygame.time.Clock()

while running:

    clock.tick(60)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((100, 100, 100))
    prev_mouse_state = game_state.update(screen)
    game_state.draw(screen)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
