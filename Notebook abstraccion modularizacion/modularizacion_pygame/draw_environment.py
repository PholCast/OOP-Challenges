import pygame
from module_pygame import game_display,WHITE


def draw_environment(blob_list):
    game_display.fill(WHITE)
 
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            
            pygame.draw.rect(game_display, blob.color, [blob.x,blob.y,blob.size,blob.size], 0)
            blob.move()
 
    pygame.display.update()
