"""
Flappy Bird Game - NSI Project
A simple Flappy Bird game implementation using Pygame.
This module handles the main game loop and state management (menu, game, gameover).
"""

import pygame
from settings import*
from Bird import Bird
from Pipe import Pipe   
import os

# Initialize Pygame and create the game window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird NSI")
clock = pygame.time.Clock()
curdir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory path

# Load music and background images
MENU_MUSIC = f"{curdir}/sound_effects/menu_music.mp3"
background = pygame.image.load(f"{curdir}/images/background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_menu = pygame.image.load(f"{curdir}/images/background_menu.png").convert()
background_menu = pygame.transform.scale(background_menu, (WIDTH, HEIGHT))
gameover_background = pygame.image.load(f"{curdir}/images/gameover_background.png").convert()
gameover_background = pygame.transform.scale(gameover_background, (WIDTH, HEIGHT))
start_button = pygame.image.load(f"{curdir}/images/start_button.png").convert_alpha()
start_button = pygame.transform.scale(start_button, (200, 200))
restart_button = pygame.image.load(f"{curdir}/images/restart_button.png").convert_alpha()
restart_button = pygame.transform.scale(restart_button, (200, 200))
restart_rect = restart_button.get_rect(center=(400, 370))
start_rect = start_button.get_rect(center=(400, 370))
button_rect = start_button.get_rect()
button_rect.size = (200, 74)
button_rect.center = (start_rect.centerx, start_rect.centery)
button_rect2 = restart_button.get_rect()
button_rect2.size = (200, 74)
button_rect2.center = (restart_rect.centerx, restart_rect.centery)

# Load sound effects
try:
    start_sound = pygame.mixer.Sound(f"{curdir}/sound_effects/start_sound.mp3")
except:
    start_sound = None


bird = Bird() # Create the Bird
pipes = [] # List to hold the pipes
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500) # Spawn a new pipe every 1.5 seconds
bg_x = 0 # Background x position for scrolling effect
scroll_speed = 2 # Speed at which the background scrolls
running = True
game_state = "menu"
menu_music_playing = False

# Main game loop
while running:
    clock.tick(FPS)
    if game_state == "menu" and not menu_music_playing:
        pygame.mixer.music.load(MENU_MUSIC) # Load menu music
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)  # infinite loop
        menu_music_playing = True


############### EVENT HANDLING BASED ON GAME STATE ###############
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
                    bird = Bird()  # Reset bird position
                    bg_x = 0 # Reset background position
                    pipes = [] # Clear existing pipes
                    game_state = "game"

        if game_state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    bird.jump()
            if event.type == SPAWNPIPE:
                pipes.append(Pipe(WIDTH)) # Spawn a new pipe at the right edge of the screen

        # Handle game over state and return to menu
        if game_state == "gameover":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect2.collidepoint(event.pos):
                    game_state = "menu"


############### GRAPHICS BASED ON GAME STATE ###############
    if game_state == "menu":
        screen.blit(background_menu, (0, 0))
        screen.blit(start_button, start_rect)
        # pygame.draw.rect(screen, (0,0,0), button_rect2, 2) # Uncomment to see the button hitbox for debugging
    

    elif game_state == "game":
        # Scroll the background to create a moving effect
        bg_x -= scroll_speed
        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x + WIDTH, 0))
        if bg_x <= -WIDTH:
            bg_x = 0
        bird.update()
        bird.draw(screen)

        ############# Update and draw pipes, and check for collisions with the bird #############
        for pipe in pipes:
            pipe.update()
            pipe.draw(screen)
            pipes = [pipe for pipe in pipes if not pipe.off_screen()] # Remove pipes that have moved off screen 
        
        for pipe in pipes:
            if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect): 
                game_state = "gameover"

        #Check if the bird has hit the top or bottom of the screen
        if bird.rect.top <= 0 or bird.rect.bottom >= HEIGHT:
            game_state = "gameover"

    elif game_state == "gameover":
        screen.blit(gameover_background, (0, 0))
        # screen.blit(restart_button, restart_rect) # Uncomment to show the restart button, in need of a better restart button image
    pygame.display.flip()

pygame.quit()

