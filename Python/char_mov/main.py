import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Char_Mov")

player_img = pygame.image.load('spaceship.png')



playerX = 370
playerY = 480

def player():
    screen.blit(player_img,(playerX,playerY))



run = True
 
while run:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
           
    player()
    pygame.display.update()

pygame.quit()