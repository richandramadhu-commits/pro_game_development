import pygame
pygame.init()
screen=pygame.display.set_mode((1000,1000))
class Circle():
    def __init__(self,color,position,radius):
        self.color=color
        self.position=position
        self.radius=radius
        self.screen=screen
    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.position,self.radius)
    def grow(self,size):
        self.radius+=size
        pygame.draw.circle(self.screen,self.color,self.position,self.radius)
circle=Circle("red",(500,500),150)
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            circle.draw()
            pygame.display.update()
        elif i.type==pygame.MOUSEBUTTONUP:
            circle.grow(10)
            pygame.display.update()