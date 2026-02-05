import os
import pygame
from settings import*
curdir = os.path.dirname(os.path.abspath(__file__))

class Bird:
    def __init__(self):   
        """Initializes the Bird object with images and properties.

        Loads the bird images for the up and down wing positions, scales them,
        and sets the initial position and velocity of the bird.
        """
        self.image_up = pygame.image.load(f"{curdir}/images/bird_wing_up.png").convert_alpha()
        self.image_down = pygame.image.load(f"{curdir}/images/bird_wing_down.png").convert_alpha()
        self.image_up = pygame.transform.scale(self.image_up, (50, 35))
        self.image_down = pygame.transform.scale(self.image_down, (50, 35))
        self.image = self.image_up
        self.rect = self.image.get_rect(center=(150, HEIGHT // 2))

        # Initialize bird's velocity and gravity
        self.velocity = 0  # Current velocity of the bird
        self.gravity = 0.5  # Gravity affecting the bird
        self.jump_strength = -8  # Strength of the jump

    def jump(self):
        self.velocity = self.jump_strength
        if self.image == self.image_up:
            self.image = self.image_down
        else:
            self.image = self.image_up

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)
