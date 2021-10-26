import os
from pathlib import Path

"""The responsibility of "constants" module is to keep the information about constants used in the game.

    Stereotype:
        Information Holder

    Attributes:
        -       
"""

""" PATH """                    
ABSOLUTE_PATH = os.path.abspath(__file__)
THIS_DIRECTORY = os.path.dirname(ABSOLUTE_PATH)
IMAGE_DIR = os.path.join(THIS_DIRECTORY, 'images') 
SOUND_DIR = os.path.join(THIS_DIRECTORY, 'sounds') 
MAP_DIR = os.path.join(THIS_DIRECTORY, 'tilemaps')

ROOT = Path(__file__).parent

""" SCREEN """ 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

""" SCALE """ 
TILE_SCALING = 1.5
SCALE = 0.2
COIN_SCALING = TILE_SCALING
SHURIKEN_SCALING = 0.1
SHURIKEN_SPEED = 5
KUNAI_SCALING = 0.2
KUNAI_SPEED = 8
SPRITE_PIXEL_SIZE = 32
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

""" MOVEMENT """ 
PLAYER_MOVEMENT_SPEED = 7
GRAVITY = 1.5
PLAYER_JUMP_SPEED = 30
PLAYER_START_X = SPRITE_PIXEL_SIZE * TILE_SCALING * 2
PLAYER_START_Y = SPRITE_PIXEL_SIZE * TILE_SCALING * 3

""" DIRECTION """ 
RIGHT = 0
LEFT_FACING = 1

# Additional lists and constants for objects and enemies

KUNAI_LIST = None

# Layer Name lists for detecting layers in loaded tilemap

""" MAP LAYERS """ 
LAYER_NAME_GROUND = "Ground"
LAYER_NAME_MOVING_PLATFORMS = "Moving Platforms"
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_LADDERS = "Ladders"
LAYER_NAME_PLAYER = "Player"
LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_DONT_TOUCH = "Don't Touch"
LAYER_NAME_KUNAI = "Kunais"
LAYER_NAME_THROW = "Throw"
LAYER_NAME_ENEMIES = "Enemies"

"""ENG GAME"""
PLAY_AGAIN = 14291.0
YOU_WIN = 13969.0
WIN_SOUND = f"{ROOT}/sounds/win_sound.mp3"
