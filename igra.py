# Питон-скрипт генерирует экраны со словом,
# обозначающим один из цветов радуги, с добавленным чёрным.
# Но нужно не прочитать это слово, а назвать цвет букв,
# которыми это слово написано.
# Сам цвет выбирается случайным образом из названной восьмёрки и почти всегда отличается от оттенка,
# который обозначает само слово. В этом собственно и заключается тренировка памяти и внимательности:
# нужно абстрагироваться от названия цвета, заложенного в слове, и определить только колер его букв.


import os
import time
import random
import pygame
from pygame.locals import *

TEXT = ["КРАСНЫЙ", 'ОРАНЖЕВЫЙ',  'ЖЁЛТЫЙ', 'ЗЕЛЁНЫЙ', 'ГОЛУБОЙ', 'СИНИЙ', 'ФИОЛЕТОВЫЙ', 'ЧЁРНЫЙ']
FONT_COLOR = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "blak"]
FONT_RGB = [(255, 0, 0), (255, 165, 0), (00, 128, 0), (255, 255, 0), (0, 0, 255), (75, 0, 130), (75, 0, 130),
            (127, 0, 255), (0, 0, 0)]

num = len(TEXT)

pygame.init()
W, H = pygame.display.Info().current_w, pygame.display.Info().current_h
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Неразбериха с цветом")
FONT_SIZE = int(H / 4)

clock = pygame.time.Clock()
FPS = 60


def draw_text(win_text, bg=(255, 255, 255)):
    win.fill(bg)
    pos = win_text.get_rect(center=(W // 2, H // 2))

    win.blit(win_text, pos)
    pygame.display.update()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_index(list, target):
    for J in range(len(list)):
        if list[J] == target:
            return J
    return -1


def get_color_text():
    font_color_index = random.randint(0, 999) % num
    txt_index = random.randint(0, 999) % num
    while (font_color_index == txt_index):
        txt_index = random.randint(0, 999) % num
    return font_color_index, txt_index


def get_text_container_chars():
    font_color_index, txt_index = get_color_text()
    txt = TEXT[txt_index]
    font_rgb = FONT_RGB[font_color_index]

    return FONT_RGB[font_color_index], TEXT[txt_index]


def main():
    fnt = pygame.font.SysFont("Arial", FONT_SIZE, bold=True)
    for J in range(5):
        clear_screen()
        font_rgb, txt = get_text_container_chars()

        win_text = fnt.render(txt, 1, font_rgb)
        draw_text(win_text)

        time.sleep(1.3)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                raise SystemExit
            else:
                pygame.event.pump()
                break
        clock.tick(FPS / 10)


if __name__ == "__main__":
    main()