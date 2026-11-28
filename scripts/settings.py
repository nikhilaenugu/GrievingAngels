import os
#Ensure the game finds the files no matter where it is run from
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Screen
SCREEN_WIDTH, SCREEN_HEIGHT= 1280, 720
FPS = 60

# Tiles: art is drawn at 40 x 40 and scaled x2 to 80 x 80 on screen
TILE_SIZE = 40
SCALE = 2
DISPLAY_WIDTH, DISPLAY_HEIGHT = SCREEN_WIDTH//SCALE , SCREEN_HEIGHT//SCALE

# Game states
MENU = "menu"
PLAYING = "playing"
PAUSED = "paused"
CAUGHT = "caught"
ESCAPED = "escaped"

# Files
MAP_PATH = os.path.join(BASE_DIR, "data", "map", "map.json")
FLOOR_IMG_PATH = os.path.join(BASE_DIR, "data", "images", "tile.png")

# Marker IDs, as stored in map.json
EXIT_LEFT_ID = "1"
EXIT_RIGHT_ID = "2"
PLAYER_START_ID = "3"
KEY_SPOT_ID = "4"
ANGEL_START_ID = "5"
JUNCTION_ID = "6"
SPAWN_POINT_ID = "7"