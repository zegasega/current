import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Street Fighter")

#load images
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()


#fnc for drawing bg
def draw_bg():

 fighter_1.draw(screen)
 fighter_2.draw(screen)


    sclaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(sclaled_bg,(0,0))

#create two instances of fighters

fighter_1 = Fighter(200,310)
fighter_2 = Fighter(700,310)


run = True
while run:
    draw_bg()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    pygame.display.update()
    
            

pygame.quit()
