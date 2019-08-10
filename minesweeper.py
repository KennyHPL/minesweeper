from random import randint, sample
import pygame as pg
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
        self.rects = {}

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
    
    def set_rects(self, WIDTH, HEIGHT, MARGIN, OFFSET):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.rects.update({(i, j):
                pg.Rect((MARGIN + WIDTH) * j + MARGIN + OFFSET,
                        (MARGIN + HEIGHT)* i + MARGIN + OFFSET,
                         WIDTH,HEIGHT)})