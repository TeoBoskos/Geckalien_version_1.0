import pygame
from pytmx.util_pygame import load_pygame

def on_platform_check(player, PLAYER_HEIGHT, platforms, upwards, was_in_air, landing, landing_timer, scored, is_jumping, jump_velocity, fall_velocity, jump_made, jump_has_played):
  """
  This function deals with the logic regarding platforms. Firstly, it checks
  if the player lands on a platform from above. If this is true, multiple parameter
  values are changed in order to correctly update the game state. If not true, it
  checks if the player is hitting a platform from below. In this case, the player
  is knocked back to the ground level or on another platform from below.

  Parameters: 
    `player`, `PLAYER_HEIGHT`, `platforms`, `upwards`, `was_in_air`, `landing`, `landing_timer`, `scored`, `is_jumping`, `jump_velocity`, `fall_velocity`, `jump_made`, `jump_has_played`.

  Returns: It returs the parameters `on_platform`, `platforms`, `upwards`, `was_in_air`, `landing`, `landing_timer`, `scored`, `is_jumping`, `jump_velocity`, `fall_velocity`, `jump_made`, `jump_has_played`.
  """

  # Check if the player is still on any platform after moving horizontally and ensure the player can't get on the platform from below.
  on_platform = False
  for platform in platforms:
    if player.colliderect(platform):
      if player.y + PLAYER_HEIGHT <= platform.y + 15 and not upwards:  # If this is true, the player is falling onto the platform from above.
        player.y = platform.y - PLAYER_HEIGHT
        if was_in_air:
          landing = True
          landing_timer = 1
          scored = False
        if landing:
          was_in_air = False
        is_jumping = False
        jump_velocity = 15
        fall_velocity = 0
        jump_made = 0
        on_platform = True
        jump_has_played = False
        break
      elif player.y >= platform.y and upwards:  # If this is true, the player is moving upwards and collides with the platform from below.
        player.y = platform.y + platform.height
        jump_velocity = 0
        fall_velocity = 0
        is_jumping = True
        upwards = False

  return on_platform, platforms, upwards, was_in_air, landing, landing_timer, scored, is_jumping, jump_velocity, fall_velocity, jump_made, jump_has_played