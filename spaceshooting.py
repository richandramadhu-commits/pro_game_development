import pygame 
pygame.init()
screen=pygame.display.set_mode((1000,1000))
ssw,ssh=110,80
space=pygame.image.load("images//space.png")
red=pygame.image.load("images//spaceship_red.png")
yellow=pygame.image.load("images//spaceship_yellow.png")
Red=pygame.transform.rotate(pygame.transform.scale(red,(ssw,ssh)),270)
Yellow=pygame.transform.rotate(pygame.transform.scale(yellow,(ssw,ssh)),90)
def draw(r,y):
    screen.blit(space,(0,0))
    screen.blit(Red,(r.x,r.y))
    screen.blit(Yellow,(y.x,y.y))
    pygame.display.update()
r=pygame.Rect(700,500,ssw,ssh)
y=pygame.Rect(100,500,ssw,ssh)
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    draw(r,y)