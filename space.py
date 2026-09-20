import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1000,1000))
rocket=pygame.image.load("images//rocket.png")
rocket=pygame.transform.scale(rocket,(175,300))
space=pygame.image.load("images//space.jpeg")
space=pygame.transform.scale(space,(1000,1000))
rocketx=400
rockety=400
keys=[False,False,False,False]
while rockety<1000:
    screen.blit(space,(0,0))
    screen.blit(rocket,(rocketx,rockety))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key==K_w:
                keys[0]=True
            if i.key==K_s:
                keys[1]=True
            if i.key==K_a:
                keys[2]=True
            if i.key==K_d:
                keys[3]=True
        if i.type==pygame.KEYUP:
            if i.key==K_w:
                keys[0]=False
            if i.key==K_s:
                keys[1]=False
            if i.key==K_a:
                keys[2]=False
            if i.key==K_d:
                keys[3]=False
    if keys[0]:
        if rockety>0:
            rockety -=5
    elif keys[1]:
        if rockety<900:
            rockety +=5
    elif keys[2]:
        if rocketx>0:
            rocketx -=5
    elif keys[3]:
        if rocketx<925:
            rocketx +=5
    rockety +=2
print ("GAME OVER")