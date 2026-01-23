"""
Flappy Bird Game - NSI Project
A simple Flappy Bird game implementation using Pygame.
This module handles the main game loop and state management (menu, game, gameover).
"""

import pygame
from settings import*
import os

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird NSI")

curdir = os.path.dirname(os.path.abspath(__file__))

MENU_MUSIC = f"{curdir}/sound_effects/menu_music.mp3"
background = pygame.image.load(f"{curdir}/images/background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_menu = pygame.image.load(f"{curdir}/images/background_menu.png").convert()
background_menu = pygame.transform.scale(background_menu, (WIDTH, HEIGHT))
gameover_background = pygame.image.load(f"{curdir}/images/gameover_background.png").convert()
gameover_background = pygame.transform.scale(gameover_background, (WIDTH, HEIGHT))
start_button = pygame.image.load(f"{curdir}/images/start_button.png").convert_alpha()
start_button = pygame.transform.scale(start_button, (200, 200))
start_rect = start_button.get_rect(center=(400, 370))
# start_rect.inflate_ip(-40, -40)
button_rect = start_button.get_rect()
button_rect.size = (200, 74)
button_rect.center = (start_rect.centerx, start_rect.centery)

clock = pygame.time.Clock()
running = True
game_state = "menu"
menu_music_playing = False
# Load sound effects
try:
    start_sound = pygame.mixer.Sound(f"{curdir}/sound_effects/start_sound.mp3")
except:
    start_sound = None

while running:
    clock.tick(FPS)
    if game_state == "menu" and not menu_music_playing:
        pygame.mixer.music.load(MENU_MUSIC)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)  # boucle infinie
        menu_music_playing = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    if start_sound:
                        start_sound.play()
                    pygame.mixer.music.stop()
                    menu_music_playing = False
                    game_state = "game"

        if game_state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: 
                    game_state = "gameover"
        
        if game_state == "gameover":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m: 
                    game_state = "menu"
    
    if game_state == "menu":
        screen.blit(background_menu, (0, 0))
        screen.blit(start_button, start_rect)
        # pygame.draw.rect(screen, (0,0,0), button_rect, 2)
    

    elif game_state == "game":
         screen.blit(background, (0, 0)) 

    elif game_state == "gameover":
        screen.blit(gameover_background, (0, 0))
    pygame.display.flip()

pygame.quit()
