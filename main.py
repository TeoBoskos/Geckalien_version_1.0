import pygame
import time
import random
from draw_function import draw  # Import the draw function.
from main_function import main  # Import the main function.
from pytmx.util_pygame import load_pygame

pygame.init()  # Starts pygame. Crucial for the program to work.

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geckalien Demo")

FONT_PATH = 'Pixeltype.ttf'
BG_PATH = "jungle-demo-background.jpeg"

BG = pygame.transform.scale(pygame.image.load(BG_PATH), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5  # Sets up the player's horizontal speed.
PLAYER_HEALTH = 100
PLAYER_SCORE = 0  # The initial value of the score is 0.

health_font = pygame.font.Font(FONT_PATH, 50)
health_surface = health_font.render("HP: {}".format(PLAYER_HEALTH), False, pygame.Color('red'))
health_rect = health_surface.get_rect(topleft = (50, 50))

score_font = pygame.font.Font(FONT_PATH, 50)
score_surface = score_font.render("SCORE: {}".format(PLAYER_SCORE), False, pygame.Color('blue'))
score_rect = score_surface.get_rect(topleft = (220, 50))

if __name__ == "__main__":
    main(WIDTH, HEIGHT, WIN, BG, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VEL, PLAYER_HEALTH, health_font, health_surface, PLAYER_SCORE, score_font, score_surface, health_rect, score_rect)