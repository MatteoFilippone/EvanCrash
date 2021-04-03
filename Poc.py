import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 1300, 886
screen=pygame.display.set_mode((width, height))
#Movements Array
keys = [False, False, False, False, False]
playerpos=[100,-100]
Sparo1pos=[100,-100]

# 3 - Load images
player = pygame.image.load("Pictures/ReEvanCrash.png")
BackGround = pygame.image.load("Pictures/EvanCrashBackground.png")
Sparo1 = pygame.image.load("Pictures/Sparo1.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(BackGround, (0, 0))

    #Player Position
    screen.blit(player, playerpos)
    screen.blit(Sparo1, Sparo1pos)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            #KeyBord to Move
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True
            elif event.key == pygame.K_SPACE:
                keys[4] = True
        if event.type == pygame.KEYUP:
            #if event.key == pygame.K_w:
            #    keys[0] = False
            if event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_DOWN:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False
    # 9 - Move player
    if keys[0]:
        playerpos[1] -= 200
        keys[0] = False
    elif keys[2]:
        playerpos[1] += 5
    elif playerpos[1] < 685:
        playerpos[1] += 15
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5
  # 10 - Spara Cazzo
    if keys[4]:
        Sparo1pos = [playerpos[0],playerpos[1] +100]
        keys[4] = False
    elif Sparo1pos[0] < 1400:
        Sparo1pos[0] += 15
