import numpy as np
import pygame
import sys
import math


LIGHTBROWN = (255, 204, 153)
DARKBROWN = (80, 25, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ROW_COUNT = 8
COL_COUNT = 8
SQUARESIZE = 100


# Functions ----------------------------------------------------------------------------------------------------------

def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board

def draw_board(board):
    for c in range(0, COL_COUNT, 2):
        for r in range(0, ROW_COUNT , 2):
            pygame.draw.rect(screen, LIGHTBROWN, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))

    for c in range(1, COL_COUNT, 2):
        for r in range(1, ROW_COUNT, 2):
            pygame.draw.rect(screen, LIGHTBROWN, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))


    for c in range(0, COL_COUNT, 2):
         for r in range(1, ROW_COUNT, 2):
            pygame.draw.rect(screen, DARKBROWN, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))

    for c in range(1, COL_COUNT, 2):
        for r in range(0, ROW_COUNT, 2):
            pygame.draw.rect(screen, DARKBROWN, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))

def place_starting_pieces(board):  # Pawn 1, Rook 2, Knight 3, Bishop 4, Queen 5, King 6 / black negative
    for c in range(COL_COUNT):
        board[1][c] = -1
        board[6][c] = 1
    board[0][0] = -2
    board[0][7] = -2
    board[0][1] = -3
    board[0][6] = -3
    board[0][2] = -4
    board[0][5] = -4
    board[0][3] = -5
    board[0][4] = -6

    board[7][0] = 2
    board[7][7] = 2
    board[7][1] = 3
    board[7][6] = 3
    board[7][2] = 4
    board[7][5] = 4
    board[7][3] = 5
    board[7][4] = 6

def move_piece(board, col, row, pick_drop,turn):
    if turn == 0: #White turn
        if pick_drop == 0:
            picked_piece = int(board[row][col]) #Pick piece
            if picked_piece >= 1:
                board[row][col] = 0
                pick_drop += 1
                return picked_piece, col, row, pick_drop, turn
            elif pick_drop == 0:
                print("Invalid white pick")
                return picked_piece, col, row, pick_drop, turn
        else:
            if board[row][col] <= 0 and not (row == row_store and col == col_store): #Check not same color or posision
                board[row][col] = picked_piece_store #Place piece
                pick_drop -= 1
                print(board)
                print("Placed white piece")
                turn += 1
                return pick_drop, turn
            else:
                print("Invalid white placement")
                return pick_drop, turn

    if turn == 1: # Black turn
        if pick_drop == 0: # Choose piece
            picked_piece = int(board[row][col])
            if picked_piece <= -1:
                board[row][col] = 0
                pick_drop += 1
                return picked_piece, col, row, pick_drop, turn
            elif pick_drop == 0:
                print("Invalid black pick")
                return picked_piece, col, row, pick_drop, turn
        else:
            if board[row][col] >= 0 and not (row == row_store and col == col_store): #Check not same color or posision
                board[row][col] = picked_piece_store
                pick_drop -= 1
                print(board)
                print("Placed black piece")
                turn -= 1
                return pick_drop, turn
            else:
                print("Invalid black placement")
                return pick_drop, turn

def draw_piece(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            # White
            if board[c][r] == 1:
                pawn_rect = r*SQUARESIZE, c*SQUARESIZE
                screen.blit(pawn, pawn_rect)
            elif board[c][r] == 2:
                rook_rect = r * SQUARESIZE, c * SQUARESIZE
                screen.blit(rook, rook_rect)
            elif board[c][r] == 3:
                knight_rect = (r * SQUARESIZE) + 5, (c * SQUARESIZE) + 10
                screen.blit(knight, knight_rect)
            elif board[c][r] == 4:
                bishop_rect = r * SQUARESIZE, c * SQUARESIZE
                screen.blit(bishop, bishop_rect)
            elif board[c][r] == 5:
                queen_rect = r * SQUARESIZE, c * SQUARESIZE
                screen.blit(queen, queen_rect)
            elif board[c][r] == 6:
                king_rect = r * SQUARESIZE, c * SQUARESIZE
                screen.blit(king, king_rect)

            # Black
            elif board[c][r] == -1:
                pawn_rect_b = r*SQUARESIZE, c*SQUARESIZE
                screen.blit(pawn_b, pawn_rect_b)
            elif board[c][r] == -2:
                rook_rect_b = r * SQUARESIZE, c * SQUARESIZE
                screen.blit(rook_b, rook_rect_b)
            elif board[c][r] == -3:
                knight_rect_b = r * SQUARESIZE, c * SQUARESIZE
                screen.blit(knight_b, knight_rect_b)
            elif board[c][r] == -4:
                bishop_rect_b = (r * SQUARESIZE) +15, (c * SQUARESIZE) + 15
                screen.blit(bishop_b, bishop_rect_b)
            elif board[c][r] == -5:
                queen_rect_b = r * SQUARESIZE, c * SQUARESIZE
                screen.blit(queen_b, queen_rect_b)
            elif board[c][r] == -6:
                king_rect_b = r * SQUARESIZE, c * SQUARESIZE
                screen.blit(king_b, king_rect_b)
#---------------------------------------------------------------------------------------------------------------------

game_over = False
turn = 0
picked_piece = 0
row_store = 0
col_store = 0
pick_drop = 0
pygame.init()
pygame.display.set_caption("Sjakk")

width = COL_COUNT * SQUARESIZE
height = ROW_COUNT * SQUARESIZE
size = width, height
screen = pygame.display.set_mode(size)

# White
pawn = pygame.image.load("pawn.png")
pawn = pygame.transform.scale(pawn,(int(SQUARESIZE),int(SQUARESIZE)))
rook = pygame.image.load("rook.png")
rook = pygame.transform.scale(rook,(int(SQUARESIZE),int(SQUARESIZE)))
knight = pygame.image.load("knight.png")
knight = pygame.transform.scale(knight,(int(SQUARESIZE-20),int(SQUARESIZE-20)))
bishop = pygame.image.load("bishop.png")
bishop = pygame.transform.scale(bishop,(int(SQUARESIZE),int(SQUARESIZE)))
queen = pygame.image.load("queen.png")
queen = pygame.transform.scale(queen,(int(SQUARESIZE),int(SQUARESIZE)))
king = pygame.image.load("king.png")
king = pygame.transform.scale(king,(int(SQUARESIZE),int(SQUARESIZE)))
# Black
pawn_b = pygame.image.load("pawn_b.png")
pawn_b = pygame.transform.scale(pawn_b,(int(SQUARESIZE),int(SQUARESIZE)))
rook_b = pygame.image.load("rook_b.png")
rook_b = pygame.transform.scale(rook_b,(int(SQUARESIZE),int(SQUARESIZE)))
knight_b = pygame.image.load("knight_b.png")
knight_b = pygame.transform.scale(knight_b,(int(SQUARESIZE),int(SQUARESIZE)))
bishop_b = pygame.image.load("bishop_b.png")
bishop_b = pygame.transform.scale(bishop_b,(int(SQUARESIZE-25),int(SQUARESIZE-25)))
queen_b = pygame.image.load("queen_b.png")
queen_b = pygame.transform.scale(queen_b,(int(SQUARESIZE),int(SQUARESIZE)))
king_b = pygame.image.load("king_b.png")
king_b = pygame.transform.scale(king_b,(int(SQUARESIZE),int(SQUARESIZE)))


board = create_board()
place_starting_pieces(board)
draw_board(board)
draw_piece(board)
print(board)
print("Starting pieces placed")
pygame.display.update()


# Main loop
while not game_over:
    for event in pygame.event.get():    #Sjekker events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            posy = event.pos[1]
            col = int(math.floor(posx / SQUARESIZE))
            row = int(math.floor(posy / SQUARESIZE))
            if pick_drop == 0: # Pick = 0, Drop = 1
                picked_piece_store, col_store, row_store, pick_drop, turn = move_piece(board, col, row, pick_drop,turn)
            else:
                pick_drop, turn = move_piece(board, col, row, pick_drop,turn)

        elif pick_drop == 1:  # Drag piece
            # White
            if picked_piece_store == 1 and turn == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                pawn_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(pawn, pawn_drag)
                pygame.display.update()
                draw_board(board)
            elif picked_piece_store == 2 and turn == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                rook_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(rook, rook_drag)
                pygame.display.update()
                draw_board(board)
            elif picked_piece_store == 3 and turn == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                knight_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(knight, knight_drag)
                pygame.display.update()
                draw_board(board)
            elif picked_piece_store == 4 and turn == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                bishop_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(bishop, bishop_drag)
                pygame.display.update()
                draw_board(board)
            elif picked_piece_store == 5 and turn == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                queen_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(queen, queen_drag)
                pygame.display.update()
                draw_board(board)
            elif picked_piece_store == 6 and turn == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                king_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(king, king_drag)
                pygame.display.update()
                draw_board(board)
            # Black
            elif picked_piece_store == -1 and turn == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                pawn_b_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(pawn_b, pawn_b_drag)
                pygame.display.update()
                draw_board(board)
            elif picked_piece_store == -2 and turn == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                rook_b_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(rook_b, rook_b_drag)
                pygame.display.update()
                draw_board(board)
            elif picked_piece_store == -3 and turn == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                knight_b_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(knight_b, knight_b_drag)
                pygame.display.update()
                draw_board(board)
            elif picked_piece_store == -4 and turn == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                bishop_b_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(bishop_b, bishop_b_drag)
                pygame.display.update()
                draw_board(board)
            elif picked_piece_store == -5 and turn == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                queen_b_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(queen_b, queen_b_drag)
                pygame.display.update()
                draw_board(board)
            elif picked_piece_store == -6 and turn == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                king_b_drag = int(mouse_x-50), int(mouse_y-50)
                draw_piece(board)
                screen.blit(king_b, king_b_drag)
                pygame.display.update()
                draw_board(board)
        else:
            draw_piece(board)
            pygame.display.update()
            draw_board(board)

