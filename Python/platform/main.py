from turtle import screensize
import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


screnn = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Platformer')

#load images

sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')






run = True

while run:

    screnn.blit(bg_img,(0,0))
    screnn.blit(sun_img,(100,100))
    

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
