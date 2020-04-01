#Scuffed Donky KONG (Brian, Leo, Harris)

import pygame
pygame.init()

#constants
WIDTH = 480
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
JUMP_LIMIT = 30
jump_counter = 0

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
mario.rect.bottom = 640
mario_group = pygame.sprite.GroupSingle(mario)

#Sprite sizes
TILE_SIZE = 8

#platforms
platform_list = [[400, 15, WHITE, 0, 100], [400, 15, WHITE, 80, 200], 
[400, 15, WHITE, 0, 300], [400, 15, WHITE, 80, 400], [400, 15, WHITE, 0, 500], [120, 15, WHITE, 180, 580]]
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
while not game_over:
    pygame.time.delay(10)#delays each frame by 10 millisecs
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #Quits Game when escape key pressed
            game_over = True
    keys = pygame.key.get_pressed()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            mario.rect.right += TILE_SIZE
            collisions = pygame.sprite.groupcollide(mario_group, platforms, False, False)
            for platform in collisions:
                mario.rect.right -= TILE_SIZE
        elif event.key == pygame.K_LEFT:
            mario.rect.right -= TILE_SIZE
            collisions = pygame.sprite.groupcollide(mario_group, platforms, False, False)
            for platform in collisions:
                mario.rect.right += TILE_SIZE
        elif event.key == pygame.K_UP:
            mario.rect.top -= TILE_SIZE
            collisions = pygame.sprite.groupcollide(mario_group, platforms, False, False)
            for platform in collisions:
                mario.rect.top += TILE_SIZE

    #gravity 
    mario.rect.bottom += 4
    collisions = pygame.sprite.groupcollide(mario_group, platforms, False, False)
    for platform in collisions:
        mario.rect.bottom -= 4

    
    #Border collisions
    if mario.rect.bottom > 640:
        mario.rect.bottom -= 4
    if mario.rect.top < 0:
        mario.rect.top += TILE_SIZE
    if mario.rect.right > 484:
        mario.rect.right -= TILE_SIZE
    if mario.rect.left < 0:
        mario.rect.left += TILE_SIZE
  
    #updates
    screen.fill((0, 0, 0))
    platforms.draw(screen)
    mario_group.draw(screen)
    pygame.display.update()






