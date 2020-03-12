import pygame
import math

pygame.init()

winx = 200
winy = 200

cx = 100
cy = 100

delay = 30

win = pygame.display.set_mode((winx,winy))
pygame.display.set_caption("TETRIS")

run = True

while run:
    pygame.time.delay(delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        

    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.circle(win, (255,255,255), (cx,cy), (10)) #circle
    
    pygame.display.flip()

    
pygame.quit()
