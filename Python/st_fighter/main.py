import pygame

pygame.init()

#create window

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#arka plan img
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")


def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))


run = True

while run:

    #draw bg
    draw_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    




pygame.quit()







