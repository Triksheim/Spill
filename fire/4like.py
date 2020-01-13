import numpy as np
import pygame
import sys
import math
import time

BLUE = (0, 0 ,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ROW_COUNT = 6
COL_COUNT = 7

# Functions --------------------------------------------------------------------------------------------
def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board


def drop_piece(board, col, turn):
    global valid

    for r in range(ROW_COUNT-1, -1, -1):
        if board[r][col] == 0:
            print(r)
            board[r][col] = turn + 1
            break
        elif r == 0:
            print("Column full")
            valid = False
            return valid

    print(board)


def check_win(board,piece):
    # Check horizontal
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical
    for r in range(ROW_COUNT-3):
        for c in range(COL_COUNT):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check synkende diagonal
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check stigende diagonal
    for c in range(COL_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[r][c] == 0:
                pygame.draw.circle(screen, BLACK, (
                int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    #pygame.display.update()

#--------------------------------------------------------------------------

board = create_board()
game_over = False
valid = True
turn = 0
print(board)

pygame.init()
pygame.display.set_caption("Fire like")
SQUARESIZE = 100
width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT +1) * SQUARESIZE

size = (width,height)
RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)

pygame.font.init()
font = pygame.font.SysFont("Arial", 100)
textred = font.render(" Red Won!",0, (255, 0, 0))
textyellow = font.render(" Yellow Won!",0, (255, 255, 0))



# Main loop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        #print(mouse_x)
        if turn == 0:
            pygame.draw.circle(screen, RED, (int(mouse_x), int(SQUARESIZE / 2)), RADIUS)
        elif turn == 1:
            pygame.draw.circle(screen, YELLOW, (int(mouse_x), int(SQUARESIZE / 2)), RADIUS)




        pygame.display.update()
        draw_board(board)
        pygame.draw.circle(screen, BLACK, (int(mouse_x), int(SQUARESIZE / 2)), RADIUS)

        if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:
            posx = event.pos[0]
            col = int(math.floor(posx/SQUARESIZE))
            time.sleep(0.2)
            drop_piece(board, col, turn)
            if valid:
                turn += 1
            else:
                valid = True

            if check_win(board, 1):
                print("Player 1 won!")
                game_over = True
            draw_board(board)

        elif event.type == pygame.MOUSEBUTTONDOWN and turn == 1 and not game_over:
            posx = event.pos[0]
            pygame.event.clear()
            col = int(math.floor(posx / SQUARESIZE))
            time.sleep(0.2)
            drop_piece(board, col, turn)
            check_win(board, 2)
            if valid:
                turn -= 1
            else:
                valid = True

            if check_win(board, 2):
                print("Player 2 won!")
                game_over = True
            draw_board(board)

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if turn == 1:
        screen.blit(textred,(150,0))
    else:
        screen.blit(textyellow, (100, 0))
    pygame.display.update()




