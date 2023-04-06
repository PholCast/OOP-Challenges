from module_pygame import clock, BLUE, RED, STARTING_BLUE_BLOBS,STARTING_RED_BLOBS
import pygame
from draw_environment import draw_environment
from Blob import Blob
def main():
    blue_blobs = dict(enumerate([Blob(BLUE) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([Blob(RED) for i in range(STARTING_RED_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([blue_blobs,red_blobs])
        clock.tick(60)
 
if __name__ == '__main__':
  main()