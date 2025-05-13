## Faça um programa em Python que abra e reproduza o audio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('')
pygame.mixer.music.play()
pygame.event.wait()