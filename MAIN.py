#Scuffed Donky KONG (Brian, Leo, Harris)

import pygame
pygame.init()

#constants
WIDTH = 480
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (78,113,228)
GREEN = (55,206,45)
GREY = (181, 181, 181)

#Mario sprite
mario = pygame.sprite.Sprite()
mario_width = 20
mario_height = 40
mario.image = pygame.Surface((mario_width,mario_height))
mario.image.fill(BLUE)
mario.rect = mario.image.get_rect()
mario.rect.bottom = 639
mario_group = pygame.sprite.GroupSingle(mario)

#Sprite sizes
TILE_SIZE = 8

#platforms
platform_list = [[400, 15, WHITE, 0, 100], [400, 15, WHITE, 80, 200], 
[400, 15, WHITE, 0, 300], [400, 15, WHITE, 80, 400], [400, 15, WHITE, 0, 500], 
[120, 15, WHITE, 180, 580], [480, 30, WHITE, 0, 1]]
platforms = pygame.sprite.OrderedUpdates()
for platform_nums in platform_list:
    width, height, colour, x, y = platform_nums
    platform = pygame.sprite.Sprite()
    platform.image = pygame.Surface((width,height))
    platform.image.fill(WHITE)
    platform.rect = platform.image.get_rect()
    platform.rect.left = x
    platform.rect.top = HEIGHT-y
    platforms.add(platform)

#MAIN LOOP --------------------------------------------
game_over = False
grav_change_down = 0
mario_change_down = 0
mario_change_x = 0
while not game_over:
    pygame.time.delay(10)#delays each frame by 10 millisecs
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #Quits Game when escape key pressed
            game_over = True
    keys = pygame.key.get_pressed()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            mario_change_x = TILE_SIZE
        elif event.key == pygame.K_LEFT:
            mario_change_x = -TILE_SIZE
        elif event.key == pygame.K_UP:
            mario.rect.top -= TILE_SIZE
            collisions = pygame.sprite.groupcollide(mario_group, platforms, False, False)
            for platform in collisions:
                mario.rect.top += TILE_SIZE

    #gravity 
    if grav_change_down == 0:
        grav_change_down = 1
    else:
        grav_change_down += 0.20
    mario.rect.bottom += grav_change_down
    collisions = pygame.sprite.groupcollide(mario_group, platforms, False, False)
    for platform in collisions:
        mario.rect.bottom -= grav_change_down
        grav_change_down = 0

    #Border collisions
    if mario.rect.top < 0:
        mario.rect.top += TILE_SIZE
    if mario.rect.right > 480:
        mario.rect.right -= TILE_SIZE
    if mario.rect.left < 0:
        mario.rect.left += TILE_SIZE

    #collision mayhem
    
  
    #updates
    screen.fill((0, 0, 0))
    platforms.draw(screen)
    mario_group.draw(screen)
    pygame.display.update()






