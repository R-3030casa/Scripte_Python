'''Faça um programa em Python que abra e reproduza o áudio de um arquivo em MP3.'''
import pygame
pygame.init()
pygame.mixer.music.load('Odeon.mp3')
pygame.mixer.music.play()
pygame.event.wait()
