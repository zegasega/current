import pygame

pygame.init()

pygame.display.set_caption("Santa Dash!")
win = pygame.display.set_mode((1200, 800))
santa = pygame.image.load("santa1.png").convert_alpha()
map = pygame.image.load("santadashmap.png").convert_alpha()
x = 100
y = 500
vel = 1

currentSantaFrame = "santa1.png"

#Gameloop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            y -= vel
        if keys[pygame.K_s]:
            y += vel
        if keys[pygame.K_a]:
            x -= vel
        if keys[pygame.K_d]:
            x += vel

    santa = pygame.image.load(currentSantaFrame).convert_alpha()

    win.blit(map, (0, 0))
    win.blit(santa, (x, y))

    if (currentSantaFrame == "santa1.png"):
        currentSantaFrame = "santa2.png"

    else:
        currentSantaFrame = "santa1.png"

    pygame.display.update()