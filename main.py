import pygame, sys,cuerpo

cuerpo1 = cuerpo.Cuerpo()

pygame.init()
BLANCO = [255,255,255]
tamaño= 630,630
screen = pygame.display.set_mode(tamaño)
screen.fill(BLANCO)
x= 0
y = 0
run = True
#cuerpo1.mapasudoku()
#cuerpo1.recorrermapa()

while run:
    for i in range(0,9):
        x = x + 70
        pygame.draw.line(screen,[0,0,0], [x,0],[x,630], 1)

    for l in range(0,9):
        y = y + 70
        pygame.draw.line(screen,[0,0,0], [0,y],[630,y], 1)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run= False
    pygame.display.flip()
pygame.quit()