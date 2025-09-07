import pygame
from OTTO.StateMachine import *
from OTTO.Helper import *

class Player():
    def __init__(self , x , y) -> None:
        self.pos = [x , y]
        self.speed = 100
        self.SpriteSheet = load_image("oldhero.png")
        self.state = 0
        self.frame_no = 0
        self.animation_timer = 0
        self.animation_time = 100
        self.dir = 0

    def Update(self , dt):
        dt /= 1000
        max_frames = 6
        if self.state == 0:
            max_frames = 6
        elif self.state == 1:
            max_frames = 8
        elif self.state == 5:
            max_frames = 3

        if self.animation_timer >= self.animation_time:
            self.animation_timer = 0
            self.frame_no = (self.frame_no + 1) % max_frames

        self.pos[0] += self.speed * dt * self.dir
        # self.pos[0] += self.speed * dt * self.dir

        self.animation_timer += dt * 1000
    
    def Draw(self , screen):
        draw_rect = (128 * self.frame_no , 128 * self.state , 128 , 128)
        screen.blit(self.SpriteSheet , self.pos , draw_rect)