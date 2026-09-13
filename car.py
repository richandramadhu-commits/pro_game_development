import pygame
pygame.init()
screen=pygame.display.set_mode((1000,1000))
clock=pygame.time.Clock()
class Car():
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
        self.x=100
        self.y=500
        self.direction=1
    def accelerate(self):
        self.speed+=10
    def move(self,dt):
        self.x+=self.speed*self.direction*dt
        if self.x>=900:
            self.direction=-1
        if self.x<=100:
            self.direction=1
    def draw(self):
        pygame.draw.rect(screen,"red",
        (self.x-100,self.y-50,200,80))
        pygame.draw.circle(screen,"black",
        (self.x-60,self.y+30),25)
        pygame.draw.circle(screen,"black",
        (self.x+60,self.y+30),25)
        pygame.draw.rect(screen,"blue",
        (self.x-50,self.y-40,100,40))
car=Car("BMW",100)
while True:
    dt=clock.tick(60)/1000
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            quit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            car.accelerate()
    screen.fill("white")
    car.move(dt)
    car.draw()
    pygame.display.update()