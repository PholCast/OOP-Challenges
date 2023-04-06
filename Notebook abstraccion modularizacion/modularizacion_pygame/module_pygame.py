#Tomado de: https://www.geeksforgeeks.org/understanding-code-reuse-modularity-python-3/
import pygame
 
STARTING_BLUE_BLOBS = 6
STARTING_RED_BLOBS = 5
 
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (0,215,0)
 
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()
 


