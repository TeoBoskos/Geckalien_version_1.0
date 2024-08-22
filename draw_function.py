import pygame
from pytmx.util_pygame import load_pygame

def draw(player, platforms, WIN, BG, health_surface, score_surface, health_rect, score_rect, grass_block_image, player_image):
    """
    This function is responsible for drawing and displaying certain elements on a screen.
    Specifically is draws the player, the platforms, the health surface, the score surface.

    It doesn't return anything. 
    """

    WIN.blit(BG, (0, 0))
    WIN.blit(player_image, (player.x, player.y))
    WIN.blit(health_surface, health_rect)
    WIN.blit(score_surface, (220, 50))

    for platform in platforms:  # It's like 'i in array' because 'platforms' is an array.
        WIN.blit(grass_block_image, (platform.x, platform.y))

    pygame.display.update()