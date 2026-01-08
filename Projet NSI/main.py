import pygame
from settings import*

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird NSI")

background = pygame.image.load("images/background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
start_button = pygame.image.load("images/start_button.png").convert_alpha()
start_button = pygame.transform.scale(start_button, (200, 200))
start_rect = start_button.get_rect(center=(150, 320))
# start_rect.inflate_ip(-40, -40)
button_rect = start_button.get_rect()
button_rect.size = (200, 74)
button_rect.center = (start_rect.centerx, start_rect.centery)

clock = pygame.time.Clock()
running = True
game_state = "menu"

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    game_state = "game"

    if game_state == "menu":
        screen.blit(background, (0, 0))
        screen.blit(start_button, start_rect)
        # pygame.draw.rect(screen, (0,0,0), button_rect, 2)

    elif game_state == "game":
        screen.fill((135, 206, 235)) 
    pygame.display.flip()

pygame.quit()
