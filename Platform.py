import pygame as py
from settings import *
from player import Player

class Platform:
    def __init__(self):
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))
        self.x = 500
        self.y = 500
    def collision(self):
        if self.pos.x + 100 > self.x and self.pos.x < (self.x + 300) and (self.pos.y + 100) > self.y:
            isOnGround = False
        

        

    
    def draw(self):  
        py.draw.rect(self.screen, (255,0,0), (500,500,300,100))
        py.display.update()


