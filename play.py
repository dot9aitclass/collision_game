import pygame
import time
from random import randint
class supes:
    def __init__(self,hdw,hdh):
        self.sup=pygame.image.load("square.png")
        self.x,self.y=0,10
        self.xspeed=0
        self.yspeed=0
        self.h=340
        self.w=340
