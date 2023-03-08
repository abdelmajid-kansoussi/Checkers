import pygame, sys
from pygame.locals import *


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
YELLOW = (218, 165, 94)
BROWN = (154, 88, 18)
GREEN = (6, 80, 0)
BGCOLOR  = GREEN

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
SQUARE_LENGTH = 50
LEFT_MARGIN = (WINDOW_WIDTH - (BOARD_WIDTH * SQUARE_LENGTH)) / 2
TOP_MARGIN = (WINDOW_HEIGHT - (BOARD_HEIGHT * SQUARE_LENGTH)) / 2

BLACK = "b"
RED = "r"
EMPTY = "."



def main():
    global DISPLAYSURF, CLOCK, RED_KING_PIECE_IMG, RED_PIECE_IMG, BLACK_KING_PIECE_IMG, BLACK_PIECE_IMG
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Checkers")
    CLOCK = pygame.time.Clock()
    RED_PIECE_IMG = pygame.transform.scale(pygame.image.load("images/red-piece.png"), (SQUARE_LENGTH, SQUARE_LENGTH))
    RED_KING_PIECE_IMG = pygame.transform.scale(pygame.image.load("images/red-king-piece.png"), (SQUARE_LENGTH, SQUARE_LENGTH))
    BLACK_PIECE_IMG = pygame.transform.scale(pygame.image.load("images/black-piece.png"), (SQUARE_LENGTH, SQUARE_LENGTH))
    BLACK_KING_PIECE_IMG = pygame.transform.scale(pygame.image.load("images/black-king-piece.png"), (SQUARE_LENGTH, SQUARE_LENGTH))


    board = get_starting_board()


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        DISPLAYSURF.fill(GREEN)
        draw_board(board)
        pygame.display.update()
        CLOCK.tick(FPS)


def get_starting_board():
    board = [[".", "r", ".", "r", ".", "r", ".", "r"],
             ["r", ".", "r", ".", "r", ".", "r", "."],
             [".", "r", ".", "r", ".", "r", ".", "r"],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             ["b", ".", "b", ".", "b", ".", "b", "."],
             [".", "b", ".", "b", ".", "b", ".", "b"],
             ["b", ".", "b", ".", "b", ".", "b", "."]]
    return board

def draw_board(board):
    pygame.draw.rect(DISPLAYSURF, YELLOW, (LEFT_MARGIN - 10, TOP_MARGIN - 10, BOARD_WIDTH * SQUARE_LENGTH + 20, BOARD_HEIGHT * SQUARE_LENGTH + 20))
    pygame.draw.rect(DISPLAYSURF, BROWN, (LEFT_MARGIN - 1, TOP_MARGIN - 1, BOARD_WIDTH * SQUARE_LENGTH + 2, BOARD_HEIGHT * SQUARE_LENGTH + 2), 2)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if i % 2 == 0:
                if j % 2 == 1:
                    pygame.draw.rect(DISPLAYSURF, YELLOW, (j * SQUARE_LENGTH + LEFT_MARGIN, i * SQUARE_LENGTH + TOP_MARGIN, SQUARE_LENGTH, SQUARE_LENGTH))
                else:
                    pygame.draw.rect(DISPLAYSURF, BROWN, (j * SQUARE_LENGTH + LEFT_MARGIN, i * SQUARE_LENGTH + TOP_MARGIN, SQUARE_LENGTH, SQUARE_LENGTH))

            if i % 2 == 1:
                if j % 2 == 1:
                    pygame.draw.rect(DISPLAYSURF, BROWN, (j * SQUARE_LENGTH + LEFT_MARGIN, i * SQUARE_LENGTH + TOP_MARGIN, SQUARE_LENGTH, SQUARE_LENGTH))
                else:
                    pygame.draw.rect(DISPLAYSURF, YELLOW, (j * SQUARE_LENGTH + LEFT_MARGIN, i * SQUARE_LENGTH + TOP_MARGIN, SQUARE_LENGTH, SQUARE_LENGTH))

            if board[i][j] == RED:
                DISPLAYSURF.blit(RED_PIECE_IMG, (j * SQUARE_LENGTH + LEFT_MARGIN, i * SQUARE_LENGTH + TOP_MARGIN, SQUARE_LENGTH, SQUARE_LENGTH))

            if board[i][j] == BLACK:
                DISPLAYSURF.blit(BLACK_PIECE_IMG, (j * SQUARE_LENGTH + LEFT_MARGIN, i * SQUARE_LENGTH + TOP_MARGIN, SQUARE_LENGTH, SQUARE_LENGTH))




def terminate():
    pygame.quit()
    sys.exit()

main()