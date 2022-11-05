import pygame,sys

pygame.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Char")



run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False
            
            
pygame.quit()

    