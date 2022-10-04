import sys
from time import sleep

import pygame
from pygame.locals import *

from Rps import *

pygame.init()
FPS = pygame.time.Clock()
FPS.tick(144)
DISPLAY = pygame.display.set_mode((1280, 720))
DISPLAY.fill((120, 20, 2))
pygame.display.set_caption("RPS")


class Comp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Comp.png")
        self.rect = self.image.get_rect()
        self.rect.center = (420, 360)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (800, 360)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/rock.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 600)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_over(self, position):
        if 455 < position[0] < 542:
            if 455 < position[1] < 640:
                return True
        return False


class Paper(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/paper.png")
        self.rect = self.image.get_rect()
        self.rect.center = (600, 600)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_over(self, position):
        if 555 < position[0] < 640:
            if 555 < position[1] < 640:
                return True
        return False


class Scissors(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Scissors.png")
        self.rect = self.image.get_rect()
        self.rect.center = (700, 600)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_over(self, position):
        if 655 < position[0] < 740:
            if 555 < position[1] < 640:
                return True
        return False


class WinText():
    def __init__(self, text):
        super().__init__()
        self.font = pygame.font.SysFont('comicsans', 60)
        self.text = text
        self.text_surf = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=(597, 360))
        self.surface = pygame.surface.Surface((444, 444))
        self.rect = self.surface.get_rect(topleft=(597, 360))

    def draw(self, surface):
        surface.blit(self.text_surf, self.rect)

    def update(self, text):
        self.text_surf = self.font.render(text, True, (255, 255, 255))
        self.surface.blit(self.text_surf, self.text_rect)


win_text = WinText("")


def run_game(move):
    attack = get_attack()
    win_text.update(get_winner(move, attack))


running = False
C = Comp()
P = Player()
while True:

    pygame.display.update()
    C.draw(DISPLAY)
    P.draw(DISPLAY)
    Rock().draw(DISPLAY)
    Paper().draw(DISPLAY)
    Scissors().draw(DISPLAY)
    win_text.draw(DISPLAY)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if running:
            sleep(3)
            sys.exit()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            print(pos)
            if Paper().is_over(pos):
                run_game(1)
            if Rock().is_over(pos):
                run_game(0)
            if Scissors().is_over(pos):
                run_game(2)

            running = True
