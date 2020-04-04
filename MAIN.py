#Scuffed Donky KONG (Brian, Leo, Harris)

import time
import pygame
pygame.init()

#constants
WIDTH = 480
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
TILE_SIZE = 5
JUMP_SIZE = 4
BARREL_MOVE = 6

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (78,113,228)
GREEN = (55,206,45)
GREY = (181, 181, 181)

#Mario sprite
mario = pygame.sprite.Sprite()
marios = pygame.sprite.OrderedUpdates()
mario_width = 20
mario_height = 40
mario.image = pygame.Surface((mario_width,mario_height))
mario.image.fill(BLUE)
mario.rect = mario.image.get_rect()
mario.rect.bottom = 639
mario_group = pygame.sprite.GroupSingle(mario)
marios.add(mario)

pygame.time.set_timer(pygame.USEREVENT, 3000)

#Barrels
barrels = pygame.sprite.OrderedUpdates()
barrel = pygame.sprite.Sprite()
barrel.image = pygame.Surface((15,15))
barrel.image.fill(GREEN)
barrel.rect = barrel.image.get_rect()
barrel.rect.left = 15
barrel.rect.bottom = 140
barrels.add(barrel)

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
win = False
loose = False
grav_change_down = 0
mario_change_x = 0
pygame.time.set_timer(pygame.USEREVENT, 3000)
while not game_over:
    pygame.time.delay(10)#delays each frame by 10 millisecs
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #Quits Game when escape key pressed
            game_over = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            mario_change_x = TILE_SIZE
        elif event.key == pygame.K_LEFT:
            mario_change_x = -TILE_SIZE
        elif event.key == pygame.K_UP:
            mario.rect.top -= 1
            mario.rect.top += 1
            collisions = pygame.sprite.spritecollide(mario, platforms, False)
            if mario.rect.bottom == platform.rect.top:
                grav_change_down = -JUMP_SIZE
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT and mario_change_x > 0:
            mario_change_x = 0
        if event.key == pygame.K_LEFT and mario_change_x < 0:
            mario_change_x = 0

    #Barrel animation
    if win == False and loose == False:
        y1= 140
        y2 = 240
        for i in range(2):
            if barrel.rect.bottom == y1 and barrel.rect.right <= 460:
                barrel.rect.right += 5
            if barrel.rect.bottom >= y1 and barrel.rect.bottom < y2 and barrel.rect.right == 460:
                barrel.rect.top += 5
            if barrel.rect.bottom == y2 and barrel.rect.right >= 40:
                barrel.rect.right -= 5
            y1 = y1 + 200
            if barrel.rect.bottom >= y2 and barrel.rect.bottom < y1 and barrel.rect.right == 35:
                barrel.rect.top += 5
            y2 = y2 + 200
        if barrel.rect.bottom == 540 and barrel.rect.right <= 460:
            barrel.rect.right += 5
        if barrel.rect.bottom == 540 and barrel.rect.right == 460:
            barrel.rect.bottom = 140
            barrel.rect.left = 15

    #gravity 
    if grav_change_down == 0:
        grav_change_down = 1
    else:
        grav_change_down += 0.08
    mario.rect.bottom += grav_change_down
    collisions = pygame.sprite.spritecollide(mario, platforms, False)
    for platform in collisions:
        if grav_change_down > 0:
            mario.rect.bottom = platform.rect.top
        if grav_change_down < 0:
            mario.rect.top = platform.rect.bottom
        grav_change_down = 0
    
    #collisions
    mario.rect.right += mario_change_x
    collisions = pygame.sprite.spritecollide(mario, platforms, False)
    for platform in collisions:#right
        if mario_change_x > 0:
            mario.rect.right = platform.rect.left
        elif mario_change_x < 0:
            mario.rect.left = platform.rect.right

    #barrel endgame
    pygame.sprite.groupcollide(mario_group, barrels, True, True)
    if len(marios) == 0:
        loose = True
    
    #win 
    if mario.rect.top < 100 and mario.rect.left < 400:
        mario.rect.left = 255
        mario.rect.top = 20
        win = True

    #Border collisions
    if mario.rect.top < 0:
        mario.rect.top = 0
    if mario.rect.right > 480:
        mario.rect.right = 480
    if mario.rect.left < 0:
        mario.rect.left = 0
  
    #clear screen
    screen.fill((0, 0, 0))

    #win sreen
    if win:
        font = pygame.font.Font(None, 36) 
        text_image = font.render("You Win!", True, (255, 255, 255))
        text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100) 
        screen.blit(text_image, text_rect)

    #loose screen
    if loose:
        font = pygame.font.Font(None, 36) 
        text_image = font.render("You Loose!", True, (255, 255, 255))
        text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100) 
        screen.blit(text_image, text_rect)

    
    #updates
    barrels.draw(screen)
    platforms.draw(screen)
    mario_group.draw(screen)
    pygame.display.update()

    






