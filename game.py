import os

import pygame

from game_state import GameState
from stats_tracker import StatsTracker

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

pygame.init()

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

# Set up the screen size as a percentage of the display size
SCREEN_SIZE_X = int(screen_width * 0.5)  # 75% of the screen width
SCREEN_SIZE_Y = int(screen_height * 0.75)  # 75% of the screen height

circle_size = 75

mouse_pressed = False
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_SIZE_X, SCREEN_SIZE_Y])

game_state = GameState(SCREEN_SIZE_X, SCREEN_SIZE_Y, is_train=False, category_to_train="same_same_same_different")

# Run until the user asks to quit
running = True


clock = pygame.time.Clock()
stats_tracker = StatsTracker()

while running:

    clock.tick(60)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((100, 100, 100))
    prev_mouse_state = game_state.update(screen, stats_tracker)
    game_state.draw(screen)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.

stats_tracker.save_raw_stats()

pygame.quit()
