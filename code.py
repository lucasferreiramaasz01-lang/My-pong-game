import pygame
from pygame.locals import *
import sys
from constants import *
import random
from random import randint, randrange



def Jogo(Screen):
    pygame.init()

    Clock = pygame.time.Clock()

    Running = True

    class Ball:     
        def __init__(self):
            self.x = SCREEN_WIDHT // 2
            self.y = SCREEN_HEIGHT // 2
            self.initial_x = self.x
            self.initial_y = self.y
            self.initial_speed = 10
            self.radius = 10
            self.speed = self.initial_speed
            self.x_dir = int(self.speed*(randrange(-1, 2, 2)))
            self.y_dir = int(self.speed*(randrange(-1, 2, 2)))
        def update(self, Screen):
            self.draw(Screen)
            if self.x_dir > 0:
                self.x_dir+= 0.025
            else:
                self.x_dir-=0.025
            self.x += int(self.x_dir)
            if self.y_dir >0:
                self.y_dir+=0.025
            else:
                self.y_dir-=0.025
            self.y += int(self.y_dir)
            if (self.x - self.radius <= 30 and self.y >= bar1.y - bar1.bar_width and self.y <= bar1.y + bar1.bar_width) or (self.x + self.radius >= SCREEN_WIDHT - 30 and self.y >= bar2.y - bar2.bar_width and self.y <= bar2.y + bar2.bar_width):
                self.x_dir *= -1
            if self.y- self.radius <= 0 or self.y + self.radius >= SCREEN_HEIGHT:
                self.y_dir *= -1
        def is_out(self):
            if self.x - self.radius < 0:
                return 1
            elif self.x + self.radius > SCREEN_WIDHT:
                return 2
            return 0
        def draw(self, Screen):
            pygame.draw.circle(Screen, (255, 255, 255), (self.x, self.y), self.radius)
        def Reset(self):
            self.speed = self.initial_speed
            self.x = self.initial_x
            self.y = self.initial_y
            self.x_dir = self.speed*(randrange(-1, 2, 2))
            self.y_dir = self.speed*(randrange(-1, 2, 2))
    class Bar():
        def __init__(self, arg):
            if arg == 1:
                self.x = 30
                self.y = SCREEN_HEIGHT // 2
            else:
                self.x = SCREEN_WIDHT - 30
                self.y = SCREEN_HEIGHT // 2
            self.initial_x = self.x
            self.initial_y = self.y
            self.speed = 15
            self.bar_width = 50
            self.moveup = False
            self.movedown = False

        def draw(self, Screen):
            pygame.draw.line(Screen, (255, 255, 255), (self.x, self.y - self.bar_width), (self.x, self.y + self.bar_width), 5)
        
        def update(self, Screen):
            if self.moveup:
                if self.y - self.bar_width > 0:
                    self.y -= self.speed
            if self.movedown:
                if self.y + self.bar_width < SCREEN_HEIGHT:
                    self.y += self.speed
            self.draw(Screen)
        def move(self, direction, pressed):
            if not pressed:
                self.moveup = False
                self.movedown = False
            elif direction == "up":
                self.moveup = True
                self.movedown = False
            elif direction == "down":
                self.movedown = True
                self.moveup = False
        def Reset(self):
            self.x = self.initial_x
            self.y = self.initial_y
    ball = Ball()
    bar1 = Bar(1)
    bar2 = Bar(2)
    All_bars = [bar1, bar2]

    def WaitStart(Screen):
        Waitingg = True
        while Waitingg:
            Clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        Waitingg = False
            Screen.fill(BACKGROUND_COLOR)
            for bar in All_bars:
                bar.draw(Screen)
            ball.draw(Screen)
            pygame.display.flip()
    def Start(Screen):
        PLaying = True
        while PLaying:
            Clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        bar1.move("up", True)
                    if event.key == K_s:
                        bar1.move("down", True)
        
                    if event.key == K_UP:
                        bar2.move("up", True)
                    if event.key == K_DOWN:
                        bar2.move("down", True)
        
                if event.type == KEYUP:
                    if event.key == K_w:
                        bar1.move("up", False)
                    if event.key == K_s:
                        bar1.move("down", False)
        
                    if event.key == K_UP:
                        bar2.move("up", False)
                    if event.key == K_DOWN:
                        bar2.move("down", False)
            Screen.fill(BACKGROUND_COLOR)
            for bar in All_bars:
                bar.update(Screen)
            ball.update(Screen)
            if ball.is_out() == 1:
                return "P1"
            elif ball.is_out() == 2:
                return "P2"
            pygame.display.flip()
    def Reset():
        bar1.Reset()
        bar2.Reset()
        ball.Reset()
    Waiting = True
    P1_hp = 3
    P2_hp = 3
    while Running:
        Clock.tick(FPS)
        if Waiting:
            WaitStart(Screen)
            Waiting = False
        else:
            Dmg = Start(Screen)
            if Dmg == "P1":
                P1_hp = P1_hp - 1
            elif Dmg == "P2":
                P2_hp = P2_hp - 1
            Reset()
            Waiting = True
        if P1_hp <= 0 or P2_hp <= 0:
            Result = [P1_hp, P2_hp]
            return Result
            Running = False
        pygame.display.flip()
