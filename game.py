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
    
    #print mouse position to screen
    textSurface = myfont.render('Mouse Pos: {}'.format(pg.mouse.get_pos()), False, (0,0,0))
    screen.blit(textSurface, (30,30))
    #Update the screen 30 FPS
    pg.display.flip()
    clock.tick(144)

pg.quit()