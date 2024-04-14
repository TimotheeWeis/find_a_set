import random

import pygame

from game_classes import Card

pygame.init()

SCREEN_SIZE_X = 720
SCREEN_SIZE_Y = 1280

circle_size = 75
mouse_pressed = False
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_SIZE_X, SCREEN_SIZE_Y])

first_card = Card(0, 0, 1, 0)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_buttons = pygame.mouse.get_pressed()

    # Fill the background with white
    screen.fill((255, 255, 255))

    if mouse_buttons[0] and not mouse_pressed:
        first_card.draw(screen, 100, 100)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()