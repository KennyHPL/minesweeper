import pygame as pg
import minesweeper as ms

board_size = 20
board = ms.Board(board_size, 75)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
OFFSET = 100
# This sets the margin between each cell
MARGIN = 1
board.set_rects(WIDTH, HEIGHT, MARGIN, OFFSET)
#pylint: disable=no-member
pg.init()
myfont = pg.font.SysFont('Comic Sans MS', 20)
screen = pg.display.set_mode((700, 700))
pg.font.init()
pg.display.set_caption('Minesweeper')
clock = pg.time.Clock()
done = False
while(not done):
    #Scan for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
      
    #Fill the screen with white
    screen.fill((255, 255, 255))

    for r in range(board.num_cols):
        for c in range(board.num_rows):
            rect = board.rects[(r, c)]
            COLOR = (77,100,100)
            if(board.board[r][c] == 0):
                COLOR = (255, 255, 0)
            elif(board.board[r][c] == 'X'):
                COLOR = (255, 0, 0)
            if(rect.collidepoint(pg.mouse.get_pos())):
                COLOR = (0,255,0)
            pg.draw.rect(screen, COLOR,
            [(MARGIN + WIDTH) * c + MARGIN + OFFSET,
             (MARGIN + HEIGHT)* r + MARGIN + OFFSET,
              WIDTH,HEIGHT])
            text = myfont.render(str(board.board[r][c]), False, (0,0,0))
            screen.blit(text, ((MARGIN + WIDTH) * c + OFFSET+MARGIN+7, (MARGIN + WIDTH) * r+ OFFSET+MARGIN+5))
    
    #print mouse position to screen
    textSurface = myfont.render('Mouse Pos: {}'.format(pg.mouse.get_pos()), False, (0,0,0))
    screen.blit(textSurface, (30,30))
    #Update the screen 30 FPS
    pg.display.flip()
    clock.tick(60)

pg.quit()