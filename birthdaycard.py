import pygame
import time
pygame.init()
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("birthdaycard")
image1=pygame.image.load("images//not_images.jpeg")
image1=pygame.transform.scale(image1,(1000,1000))
while True:
    font=pygame.font.SysFont("calibri",50)
    text1=font.render("Happy Birthday",True,"black")
    screen.blit(image1,(0,0))
    screen.blit(text1,(400,20))
    pygame.display.update()
    time.sleep(2)
    image2=pygame.image.load("images//birthday.jpeg")
    image2=pygame.transform.scale(image2,(1000,1000))
    screen.blit(image2,(0,0))
    pygame.display.update()
    time.sleep(2)
    image3=pygame.image.load("images//bday.jpeg")
    image3=pygame.transform.scale(image3,(1000,1000))
    screen.blit(image3,(0,0))
    text3=font.render("HI",True,"black")
    screen.blit(text3,(400,40))
    pygame.display.update()
    time.sleep(2)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()