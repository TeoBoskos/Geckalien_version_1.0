import pygame
from pytmx.util_pygame import load_pygame

def score_plat(landing, landing_timer, scored, PLAYER_SCORE):
  """
  This function is responsible for most of the score mechanics. It takes the
  parameters `landing`, `landing_timer`, `scored`, and `PLAYER_SCORE` and
  checks to see if the player has scored when he gets on top of a platform.
  If true, the score is incremented by one.

  It returns the new values of the parameters `PLAYER_SCORE`, `landing_timer`,
  `landing` and `scored`.
  """
  if landing and not scored:
    PLAYER_SCORE += 1
    scored = True

  if landing_timer > 0:
    landing_timer -= 1

  if landing_timer == 0:
    landing = False
    scored = False

  return PLAYER_SCORE, landing_timer, landing, scored