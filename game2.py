import pygame
import time
from play import supes
from sateek import khelo
pygame.init()
if __name__=="__main__":
    a=int(raw_input("Enter number of Squares: "))
    mekhelega=khelo(a)
    mekhelega.disp()