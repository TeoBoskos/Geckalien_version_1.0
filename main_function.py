import pygame
from draw_function import draw
from movement import handle_keys
from movement import fall_time_logic
from score import score_plat
from platforms import on_platform_check
from pytmx.util_pygame import load_pygame
from level import load_layer

def main(WIDTH, HEIGHT, WIN, BG, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VEL, PLAYER_HEALTH, health_font, health_surface, PLAYER_SCORE, score_font, score_surface, health_rect, score_rect):
    """
    The main function is responsible for multiple things. First of all,
    it sets up the main game loop. Furthermore, it sets the game window,
    background, the player, the platforms and the sound effects. It also
    handles the player's movement, jump mechanics and collisions with things
    like platforms. The function also manages the player's health and score,
    playing sound effects for jumping, scoring, and taking damage. The game
    loop continuously updates the game state, including the player's position,
    jumping and falling mechanics, and interactions with platforms, while
    rendering the updated game scene. The loop exits when the player quits the
    game or their health reaches zero.

    It takes the parameters `WIDTH`, `HEIGHT`, `WIN`, `BG`, `PLAYER_WIDTH`, `PLAYER_HEIGHT`,
    `PLAYER_VEL`, `PLAYER_HEALTH`, `health_font`, `health_surface`, `PLAYER_SCORE`,
    `score_font`, `score_surface`, `health_rect` and `score_rect`.

    It doesn't return anything.
    """

    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    # The tile size.
    TILE_SIZE = 25

    # CSV paths
    ground_layer_path = 'test_csv_Background layer.csv'
    platform_layer_path = 'test_csv_Platforms.csv'

    # Load ground and platform layers.
    ground = load_layer(ground_layer_path, TILE_SIZE)
    platforms = load_layer(platform_layer_path, TILE_SIZE)

    # Combine ground and platforms into a single list.
    all_platforms = ground + platforms

    # Sound effect paths.
    JUMP_SFX_PATH = "Audio/jump_sound_ef.mp3"
    DAMAGE_SFX_PATH = "Audio/damage_sound_ef.mp3"
    SCORE_SFX_PATH = "Audio/score_sound_ef.mp3"

    # Sound effects.
    jump_sfx = pygame.mixer.Sound(JUMP_SFX_PATH)
    damage_sfx = pygame.mixer.Sound(DAMAGE_SFX_PATH)
    score_sfx = pygame.mixer.Sound(SCORE_SFX_PATH)

    # Load the player image.
    PLAYER_IMAGE_PATH = "Graphics/player_model.png"
    player_image = pygame.image.load(PLAYER_IMAGE_PATH)

    # Grass block image.
    GRASS_BLOCK_PATH = "Graphics/tilesets/pixel_art_correct.png"
    grass_block_image = pygame.image.load(GRASS_BLOCK_PATH)

    GROUND_LEVEL = HEIGHT - PLAYER_HEIGHT - 25  # This is the y-coordinate where the player stands on the ground.
    is_jumping = False
    is_falling = False
    landing = False  # This variable indicates if the player is landing. It's only set to true for a single frame.
    landing_timer = 0  # This is a timer to set landing back to false after one frame.
    scored = False  # This variable tells us if the player just scored.
    was_in_air = False  # This variable tells us if the player was previously on air.
    upwards = False  # This variable tells us if the player is moving upwards or downwards.
    jump_limit = 7  # Number of allowed jumps.
    jump_made = 0  # Counter for jumps made.
    jump_velocity = 15  # Velocity for jump.
    fall_velocity = 0  # Velocity for fall.
    fall_time = 0  # This variable acts as a timer for how much time the player falls.
    gravity = 1  # Gravity to control descent rate.

    # Variables for sfx.
    jump_has_played = False  # This variable tells us if the sound for jumping has played.
    score_has_played = False  # Same for the sound for scoring.

    health_surface = health_font.render("HP: {}".format(PLAYER_HEALTH), False, pygame.Color('red'))
    score_surface = score_font.render("SCORE: {}".format(PLAYER_SCORE), False, pygame.Color('blue'))

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if PLAYER_HEALTH <= 0:  # CHANGE THIS!!!
            run = False         # CHANGE THIS!!!
            break               # CHANGE THIS!!!

        #  Call the handle_keys function and update the variables.
        is_jumping, upwards, jump_made, jump_velocity, fall_velocity, jump_sfxn, jump_has_played = handle_keys(player, PLAYER_VEL, jump_made, jump_limit, is_jumping,
        upwards, jump_velocity, fall_velocity, WIDTH, jump_sfx, jump_has_played)

        if is_jumping:
            player.y -= jump_velocity  # By lowering the player's y position, he goes up to the air.
            jump_velocity -= gravity  # By lowering gravity, the player slowly stops going up and then starts going down.
            was_in_air = True
            if player.y < 600:
                fall_time += 1
            if jump_velocity <= 0:
                upwards = False
            if jump_velocity < -15:  # Terminal velocity
                jump_velocity = -15

        PLAYER_HEALTH, is_jumping, is_falling, fall_time, damage_sfx = fall_time_logic(player, GROUND_LEVEL, PLAYER_HEALTH, is_jumping, is_falling, fall_time, damage_sfx)

        # Ensure the player doesn't go below the ground level
        if player.y >= GROUND_LEVEL:
            player.y = GROUND_LEVEL
            is_jumping = False
            is_falling = False
            upwards = False
            jump_velocity = 15
            fall_velocity = 0
            jump_made = 0  # Resets jumps made when landing.
            jump_has_played = False

        # Call the `on_platform_check` function to execute the logic regarding platforms.       
        on_platform, platforms, upwards, was_in_air, landing, landing_timer, scored, is_jumping, jump_velocity, fall_velocity, jump_made, jump_has_played = on_platform_check(player, PLAYER_HEIGHT, platforms, upwards, was_in_air, landing, landing_timer, scored, is_jumping, jump_velocity, fall_velocity, jump_made, jump_has_played)

        #  If not on any platform and not jumping, apply gravity.
        if not on_platform and not is_jumping:
            fall_velocity += gravity
            player.y += fall_velocity
            if player.y < 700:
                is_falling = True
            if player.y >= GROUND_LEVEL:
                player.y = GROUND_LEVEL
                fall_velocity = 0  # Reset fall velocity to its initial value.

        #  Call the score_plat function and update the variables.
        PLAYER_SCORE, landing_timer, landing, scored = score_plat(landing, landing_timer, scored, PLAYER_SCORE)

        if PLAYER_SCORE % 10 == 0 and not score_has_played and PLAYER_SCORE != 0:
            score_sfx.play()
            score_has_played = True
        elif PLAYER_SCORE % 10 != 0:
            score_has_played = False

        #  Update health_surface with health's current value.
        health_surface = health_font.render("HP: {}".format(PLAYER_HEALTH), False, pygame.Color('red'))
        #  Same goes for the score surface.
        score_surface = score_font.render("SCORE: {}".format(PLAYER_SCORE), False, pygame.Color('cyan'))

        draw(player, all_platforms, WIN, BG, health_surface, score_surface, health_rect, score_rect, grass_block_image, player_image)

    pygame.quit()