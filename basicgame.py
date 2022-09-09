import pygame
import numpy as np
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500


def game1(pf_rows, pf_columns):
    pygame.init()
    # set up play field
    pf_data = np.zeros( (pf_rows, pf_columns) )
    pf_update = True
    circle_radius = 25
    player = 0
    # Set up the drawing window

    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])


    # Run until the user asks to quit

    running = True
    screen.fill(BLUE)

    while running:


        # Did the user click the window close button?

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False


        # Fill the background with white


        # Draw a solid blue circle in the center

        # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        if pf_update == True:
            pf_draw(pf_data, circle_radius, screen)
            pygame.display.flip()
            pf_update = False

        player_display = player + 1
        in_string = "Player: " + str(player_display) + " Column:"
        next_move = input(in_string)


        column = int(next_move) - 1
        for i in reversed(range(pf_rows)):
            if pf_data[i, column] == 0:
                pf_data[i, column] = player_display
                break
        player ^= 1





        pf_update = True




    # Done! Time to quit.

    pygame.quit()



def pf_draw(pf_data, circle_radius, screen):
    num_rows, num_cols = pf_data.shape
    block_size_x = WINDOW_WIDTH / (num_cols + 1)
    block_size_y = WINDOW_HEIGHT / (num_rows + 1)
    for x in range(0, num_cols, 1):
        for y in range(0, num_rows, 1):
            pos_state = pf_data[y, x]
            if pos_state == 1:
                pygame.draw.circle(screen, (RED), (block_size_x * (x + 1), block_size_y * (y + 1)), circle_radius)
            elif pos_state == 2:
                pygame.draw.circle(screen, (YELLOW), (block_size_x * (x + 1), block_size_y * (y + 1)), circle_radius)
            else:
                pygame.draw.circle(screen, (WHITE), (block_size_x * (x+1), block_size_y * (y+1)), circle_radius)

    return screen