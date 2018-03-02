import pygame
import sys
import re
from pygame.locals import *
import pymunk
import pyparticles

pygame.init()
width = 500
height = 900
screenDim = (width,height)
screen = pygame.display.set_mode(screenDim)
pygame.display.set_caption("Cave Man Bird Hunter")

# Load images
screen.fill((255,255,255))
background = pygame.image.load("background3.png").convert()
background = pygame.transform.scale(background,(width,height))

rescalePlayer = 1
player = pygame.image.load("pizzajesus.png").convert_alpha()
player = pygame.transform.scale(player,(50,75))
playerWidth = player.get_rect().width
playerHeight = player.get_rect().height

player1 = pygame.image.load("plady1.png").convert_alpha()
player1 = pygame.transform.scale(player1,(40,60))
player1Width = player1.get_rect().width
player1Height = player1.get_rect().height

blackbird = pygame.image.load("blackbird.png").convert_alpha()
blackbird = pygame.transform.scale(blackbird,(50,75))
blackbirdWidth = blackbird.get_rect().width
blackbirdHeight = blackbird.get_rect().height

redbird = pygame.image.load("redbird.png").convert_alpha()
redbird = pygame.transform.scale(redbird,(50,75))
redbirdWidth = redbird.get_rect().width
redbirdHeight = redbird.get_rect().height

seesaw = pygame.image.load("seesawA.png").convert_alpha()
seesaw = pygame.transform.scale(seesaw,(150,300))
seesawWidth = seesaw.get_rect().width
seesawHeight = seesaw.get_rect().height

screen.blit(background,(0,0))
screen.blit(player, (100,100))
screen.blit(player1, (200,800))
screen.blit(blackbird, (400,200))
screen.blit(redbird, (50,100))
screen.blit(seesaw,(100,650))

finished = False
while finished == False:

# 8 - loop through the events
     for event in pygame.event.get():
         if event.type==pygame.QUIT:
            finished = True
            pygame.quit()
            sys.exit(0)

     pygame.display.flip()
