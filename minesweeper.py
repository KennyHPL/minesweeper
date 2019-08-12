from random import randint, sample
import pygame as pg

class Cell:
    '''
    Creates a cell with width*height at with the top left corner at
    (left, top) (x, y)
    '''
    def __init__(self, left, top, width, height):
        self.is_mine = False
        self.surrounding_mines = 0
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pg.Rect(left, top, width, height)
    
    def draw_cell(self, screen, color):
        pg.draw.rect(screen, color, self.top, self.width, self.height)

    def get_rect(self):
        return self.rect

class Board:
    '''
    Creates an N x N board with n mines generated
    '''
    def __init__(self, N, num_mines):
        self.num_rows = N
        self.num_cols = N
        self.num_mines = num_mines
        self.mines = set()
        self.board = [[0 for x in range(self.num_rows)] for y in range(self.num_cols)]
        self.cells = {}

        s = set()
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                s.add(tuple([i, j]))
        
        for _ in range(self.num_mines):
            pos = sample(s, 1)[0]
            s -= {pos}
            #pylint: disable=unsubscriptable-object
            self.board[pos[0]][pos[1]] = 'X'
        
        directions = {(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)}

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                surrounding_mines = 0
                if(self.board[i][j] == 'X'):
                    continue
                for direction in directions:
                    r = i + direction[0]
                    c = j + direction[1]
                    if(r >= self.num_rows or c >= self.num_cols or r < 0 or c < 0):
                        continue
                    if(self.board[r][c] == 'X'):
                        surrounding_mines += 1
                self.board[i][j] = surrounding_mines
                    

    def print_board(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                print(self.board[i][j], end=' ')
            print()