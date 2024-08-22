import pygame
from pytmx.util_pygame import load_pygame

def handle_keys(player, PLAYER_VEL, jump_made, jump_limit, is_jumping, upwards, jump_velocity, fall_velocity, WIDTH, jump_sfx, jump_has_played):
  """
  This function is responsible for most of the code that is triggered when a key is pressed.
  As of now, it handles the left and the right arrow keys, ensuring that the player moves
  left and right when they are pressed accordingly, and it also handles the up arrow key,
  thereby ensuring that the player jumps when it is pressed.

  It takes the parameters `player`, `PLAYER_VEL`, `jump_made`, `jump_limit`, `is_jumping`, `upwards`,
  `jump_velocity`, `fall_velocity`, `WIDTH`, `jump_sfx` and `jump_has_played`.

  It returns the new values of the parameters `is_jumping`, `upwards`, `jump_made`, `jump_velocity`,
  `fall_velocity`, `jump_sfx` and `jump_has_played`.
  """

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
    player.x -= PLAYER_VEL
  if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
    player.x += PLAYER_VEL

  if keys[pygame.K_UP] and jump_made < jump_limit:
    is_jumping = True
    upwards = True
    jump_made += 1
    jump_velocity = 15  # Reset jump velocity.
    fall_velocity = 0  # Also reset the fall velocity.
    if not jump_has_played:
      jump_sfx.play()
      jump_has_played = True

  return is_jumping, upwards, jump_made, jump_velocity, fall_velocity, jump_sfx, jump_has_played


def fall_time_logic(player, GROUND_LEVEL, PLAYER_HEALTH, is_jumping, is_falling, fall_time, damage_sfx):
  """
  This function handles much of the logic regarding the `fall_time` variable.
  If the player is falling, `fall_time` is incremented. Then after it reaches
  a certain value, it is reset. It is also reset if the player hits the ground
  or a platform.

  Parameters:
    `player`, `GROUND_LEVEL`, `PLAYER_HEALTH`, `is_jumping`, `is_falling`, `fall_time`, `damage_sfx`.
    
  Returns:
    It returns the parameters: `PLAYER_HEALTH`, `is_jumping`, `is_falling`, `fall_time`, `damage_sfx`.
  """

  if is_falling:
    if player.y < 400:
      fall_time += 1

  print(fall_time)

  if fall_time >= 80 and player.y == GROUND_LEVEL:  # If the player is falling for too much time and hits the ground level, he takes damage.
    PLAYER_HEALTH -= 5
    damage_sfx.play()
    fall_time = 0  # fall_time is reset.

  if player.y == GROUND_LEVEL:
    fall_time = 0            

  if is_jumping == False and is_falling == False:
    fall_time = 0  # fall_time is reset.

  return PLAYER_HEALTH, is_jumping, is_falling, fall_time, damage_sfx