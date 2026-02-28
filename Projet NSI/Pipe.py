import os
import pygame  
import random
from settings import *
pygame.display.init()
curdir = os.path.dirname(os.path.abspath(__file__)) # Get the current directory path

PIPE_IMG = pygame.image.load(f"{curdir}/images/pipe.png") #Load the pipe image
PIPE_IMG = pygame.transform.scale(PIPE_IMG, (80, 500)) #Scale the pipe image to the desired size

# Define the Pipe class
class Pipe:
    def __init__(self, x):
        """Initializes the Pipe. Loads the pipe image and sets the initial position of the pipe.
        The pipe is randomly positioned vertically to create a gap for the bird to pass through. 
        """ 
        self.gap = 160
        self.x = x
        self.speed = 2

        self.height = random.randint(150, 450)

        self.top_rect = pygame.Rect(self.x, 0, 80, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + self.gap, 80, HEIGHT)

        self.top_img = pygame.transform.flip(PIPE_IMG, False, True)  # Flip the pipe image for the top pipe
        self.bottom_img = PIPE_IMG
        self.passed = False

    def update(self):
        self.x -= self.speed
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        screen.blit(self.top_img, (self.top_rect.x, self.top_rect.bottom - self.top_img.get_height())) #Draw the top pipe
        screen.blit(self.bottom_img, (self.bottom_rect.x, self.bottom_rect.y)) #Draw the bottom pipe

    def off_screen(self):
        return self.x < -80