import code
from code import Jogo
import sys
from constants import *
import pygame
from pygame.locals import *
import os
from os import path
Screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption((TITLE))
Clock = pygame.time.Clock()

images_dir = path.join(path.dirname(__file__), 'Images')
buttons = pygame.image.load(path.join(images_dir, 'GUI.png')).convert_alpha()
Results_png = pygame.image.load(path.join(images_dir, 'Results.png')).convert_alpha()
Results_png = Results_png.subsurface((0,0, 64, 64))
Playing = False
Run = True

class Buttons:
    def __init__(self, start_x, start_y, x, y):
        self.Image = buttons.subsurface((start_x, start_y, 128, 32))
        self.Image = pygame.transform.scale(self.Image, (128*1.5, 32*1.5))
        self.rect = self.Image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
    def draw(self, Screen, x, y):
        Screen.blit(self.Image, self.rect)

    def Click(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        return False
SCREEN_HEIGHT-(SCREEN_HEIGHT//3)
Play_button = Buttons(160, 16, SCREEN_WIDHT//2, 220)
Settings_button = Buttons(160, 64, SCREEN_WIDHT//2, 300)
Exit_button = Buttons(160, 112, SCREEN_WIDHT//2, 380)
All_buttons = [Play_button, Settings_button, Exit_button]

def Menu():
    global Playing
    color_decress = False
    x = BACKGROUND_COLOR[0]
    while not Playing:
        Clock.tick(FPS)
        Screen.fill((int(x), int(x), int(x)))
        if not color_decress:
            x += 0.1
        else:
            x -= 0.1
        if x <= BACKGROUND_COLOR[0]:
            color_decress = False
        elif x >= 40:
            color_decress = True
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    Playing = True
            if event.type == MOUSEBUTTONDOWN:
                if Play_button.Click():
                    Playing = True
                if Exit_button.Click():
                    pygame.quit()
                    sys.exit()
        for button in All_buttons:
            button.draw(Screen, 288, 200)
        pygame.display.flip()

def MakeText(Message, font, x, y, color):
    Text = font.render(Message, True, color)
    Text_rect = Text.get_rect()
    Text_rect.center = (x, y)
    Screen.blit(Text, Text_rect)


def Results(Result):
    Waiting = True
    if Result[0]<=0:
        Win = ["Player 2", Result[1]]
    elif Result[1]<=0:
        Win = ["Player 1", Result[0]]
    else:
        Win = ["Ninguem!", "Nenhum ne"]
    font = pygame.font.SysFont("agencyfb", 40, True, False)

    global Results_png
    Results_png = pygame.transform.scale(Results_png, (500, 500))
    Result_rect = Results_png.get_rect()
    Result_rect.center = (SCREEN_WIDHT//2, SCREEN_HEIGHT//2)

    while Waiting:
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Waiting = False
        Screen.fill(BACKGROUND_COLOR)
        Screen.blit(Results_png, Result_rect)
        MakeText(f"{Win[0]} GANHOU!", font, SCREEN_WIDHT//2, 200, (0,191,255))
        MakeText(f"HP do {Win[0]}: {Win[1]}", font, SCREEN_WIDHT//2, 300, (173,255,47))
        MakeText("Pressione ESC para retornar.", font, SCREEN_WIDHT//2, 400, (255, 255, 255))
        pygame.display.flip()


while Run:
    Clock.tick(FPS)
    if not Playing:
        Menu()
    else:
        Result = Jogo(Screen)
        print(Result[0])
        Playing = False
        Results(Result)
