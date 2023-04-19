#Faça um programa em Python que abra e produza o áudio de um arquivo mp3.

import pygame

pygame.init()
pygame.mixer_music.load('Harry_Potter.mp3')
pygame.mixer_music.play()
pygame.event.wait()
