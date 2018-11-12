import pygame
import time
from random import randint
from play import supes
class khelo:
    def __init__(self,numb):
        self.hdw=1920
        self.hdh=1080
        self.stop=False
        self.can=pygame.display.set_mode((self.hdw,self.hdh))
        pygame.display.set_caption("Games Saar")
        self.clock=pygame.time.Clock()
        self.numb=numb
        self.obj=0
    def disp(self):
        self.manysupes=[supes(self.hdw,self.hdh) for i in xrange(self.numb)]
        self.manysupes[0].x=10
        for j in xrange(1,self.numb):
            for k in xrange(0,self.numb-j):
                self.manysupes[j].x=(j*self.manysupes[0].w)+(j+1)*10
                if self.manysupes[j].x<(self.hdw-self.manysupes[0].w-10):
                    self.can.blit(self.manysupes[j].sup,(self.manysupes[j].x,self.manysupes[j].y))
                else:
                    self.manysupes[j].x=(self.manysupes[0].w*k)+(k+1)*10
                    self.manysupes[j].y=self.manysupes[0].h+20
                    self.can.blit(self.manysupes[j].sup,(self.manysupes[j].x,self.manysupes[j].y))
        while not self.stop:
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    self.obj=self.mouse()                    
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        self.manysupes[self.obj].xspeed=20                      
                    if event.key==pygame.K_LEFT:
                        self.manysupes[self.obj].xspeed=-20
                    if event.key==pygame.K_UP:
                        self.manysupes[self.obj].yspeed=-20
                    if event.key==pygame.K_DOWN:
                        self.manysupes[self.obj].yspeed=+20
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                        self.manysupes[self.obj].xspeed=0
                        self.manysupes[self.obj].yspeed=0
            self.manysupes[self.obj].x=self.manysupes[self.obj].x+self.manysupes[self.obj].xspeed
            self.manysupes[self.obj].y=self.manysupes[self.obj].y+self.manysupes[self.obj].yspeed
            self.can.fill((255,255,255))
            if self.manysupes[self.obj].x<0 or self.manysupes[self.obj].x>self.hdw-self.manysupes[0].w:
                self.manysupes[self.obj].x-=self.manysupes[self.obj].xspeed
            if self.manysupes[self.obj].y<0 or self.manysupes[self.obj].y>self.hdh-self.manysupes[0].h:
                self.manysupes[self.obj].y-=self.manysupes[self.obj].yspeed
            for i in xrange(0,self.numb):
                if i!=self.obj:
                    if (self.manysupes[i].x<=self.manysupes[self.obj].x<=self.manysupes[i].x+self.manysupes[0].w) or (self.manysupes[i].x<=self.manysupes[self.obj].x+self.manysupes[0].w<=self.manysupes[i].x+self.manysupes[0].w):
                        if (self.manysupes[i].y<=self.manysupes[self.obj].y<=self.manysupes[i].y+self.manysupes[0].h) or (self.manysupes[i].y<=self.manysupes[self.obj].y+self.manysupes[0].h<=self.manysupes[i].y+self.manysupes[0].h):
                            self.can.fill((255,255,0))
                    elif (self.manysupes[i].y<self.manysupes[self.obj].y<self.manysupes[i].y+self.manysupes[0].h) or (self.manysupes[i].y<self.manysupes[self.obj].y+self.manysupes[0].h<self.manysupes[i].y+self.manysupes[0].h):
                        if (self.manysupes[i].x<self.manysupes[self.obj].x<self.manysupes[i].x+self.manysupes[0].w) or (self.manysupes[i].x<self.manysupes[self.obj].x+self.manysupes[0].w<self.manysupes[i].x+self.manysupes[0].w):
                            self.can.fill((255,255,0))
            for j in self.manysupes:
                self.can.blit(j.sup,(j.x,j.y))
            #self.can.blit(self.manysupes[self.obj].sup,(self.manysupes[self.obj].x,self.manysupes[0].y))
            pygame.display.update()
            self.clock.tick(60)

    def mouse(self):
        self.flag=1
        self.mouse_pos= pygame.mouse.get_pos()
        #self.mouse_press= pygame.mouse.get_pressed()
        for i in xrange(0,self.numb):
            if self.manysupes[i].x+self.manysupes[0].w>=self.mouse_pos[0]>=self.manysupes[i].x and self.manysupes[i].y+self.manysupes[0].h>=self.mouse_pos[1]>=self.manysupes[i].y:
                self.flag=0
                return i
        if self.flag==1:
            return self.obj