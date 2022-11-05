import pygame, sys

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Brawler')

sprite_sheet_image = pygame.image.load('chars/adventurer-crouch-00.png').convert_alpha()


BG = (50,50,50)


def get_image(sheet,width,height):
    image = pygame.Surface((width,height)).convert_alpha()
    return image

frame_0 = get_image(sprite_sheet_image,24,24)


run = True

while run:

    #update bg
    screen.fill(BG)


    screen.blit(frame_0,(0,0))
 



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
    
    

    

    pygame.display.update()

pygame.quit()