import pygame
import numpy as np
#import sys

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

        if check_win(pf_data, player):
            print("Player ", player, " wins!")
            exit()
        player ^= 1





        pf_update = True




    # Done! Time to quit.

    pygame.quit()


def check_win(pf_data, player):
    #shift from 2 player to white + 2 player
    player += 1
    num_rows, num_cols = pf_data.shape
    count = 0
    # check vertical wins
    for column in range(num_cols):
        for row in range(num_rows):
            if pf_data[row, column] == player:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
    count = 0
    # check horizontal wins
    for row in range(num_rows):
        for column in range(num_cols):
            if pf_data[row, column] == player:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
    count = 0
    # check forward-down diagonal wins
    column = 0
    for y in range(0,num_rows - 3):
        row = y
        while row < num_rows and column < num_cols:
            if pf_data[row, column] == player:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
            row += 1
            column += 1
    count = 0
    row = 0
    for x in range(1,num_cols - 3):
        column = x
        while row < num_rows and column < num_cols:
            if pf_data[row, column] == player:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
            row += 1
            column += 1
    count = 0
    # check forward-up diagonal wins
    column = 0
    for y in reversed(range(0, num_rows - 3)):
        row = y
        while row >= 0 and column < num_cols:
            if pf_data[row, column] == player:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
            row -= 1
            column += 1
    count = 0
    row = num_rows - 1
    for x in range(1, num_cols - 3):
        column = x
        while row >= 0 and column < num_cols:
            if pf_data[row, column] == player:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
            row -= 1
            column += 1
    return False



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
