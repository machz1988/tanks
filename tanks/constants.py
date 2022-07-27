from game.casting.color import Color
from game.casting.point import Point

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Tanks"
#FRAME_RATE = 60
FRAME_RATE = 30
GRAVITY = 200
TIME_RATE = 0.03

# SCREEN
#SCREEN_WIDTH = 1040
#SCREEN_HEIGHT = 680
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "tanks/tanks/assets/fonts/zorque.otf"
FONT_SMALL = 16
FONT_MEDIUM = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "tanks/tanks/assets/sounds/boing.wav"
WELCOME_SOUND = "tanks/tanks/assets/sounds/start.wav"
OVER_SOUND = "tanks/tanks/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
SADDLEBROWN = Color(139, 69, 19)
SIENNA = Color(160, 82, 45)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "tanks/tanks/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5
MAXIMUM_HEALTH = 100

# HUD
HUD_MARGIN = 5
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
HEALTH_GROUP = "health"
PROJECTILE_POWER_GROUP = "projectile_power"
SHOOTING_POWER_GROUP = "shooting_power"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"
HEALTH_FORMAT = "HEALTH: {}"
PROJECTILE_POWER_FORMAT = "PROJECTILE POWER: {}"
SHOOTING_POWER_FORMAT = "SHOOTING POWER: {}"

# PROJECTILES
PROJECTILES_GROUP = "projectiles"
PROJECTILE_SIZE = Point(14,14)
PROJECTILE_IMAGE = "tanks/tanks/assets/images/projectile.png"
PROJECTILE_SCALE = 0.5
PROJECTILE_ROTATION = 0.0

PROJECTILE_V0_MIN = 100
PROJECTILE_V0_MAX = 500
PROJECTILE_DEFAULT_V0 = 350
PROJECTILE_POWER_MIN = 10
PROJECTILE_POWER_MAX = 50
PROJECTILE_DEFAULT_POWER = 20

PROJECTILE_EXAMPLE_V0 = 350
PROJECTILE_EXAMPLE_POWER = 20
PROJECTILE_EXAMPLE_ANGLE = 60

# PROJECTIONS
PROJECTIONS_GROUP = "projections"
PROJECTION_SIZE = Point(14, 14)
PROJECTION_IMAGE = "tanks/tanks/assets/images/projectile.png"
PROJECTION_COLOR = WHITE
PROJECTION_RADIUS = 7
PROJECTION_SCALE = 0.5
PROJECTION_ROTATION = 0.0
PROJECTIONS_NUMBER = 10
#PROJECTION_TIME_RATE = TIME_RATE * 10

# TERRAIN
TERRAIN_GROUP = "terrain"
TERRAIN_IMAGE = "tanks/tanks/assets/images/ground_texture.png"

# TANKS
TANKS_GROUP = "tanks"
TANK1_SIZE = Point(20,20)
TANK2_SIZE = Point(20,20)
TANK1_VELOCITY = Point(0, 0)
TANK2_VELOCITY = Point(0, 0)
TANK1_IMAGE = "tanks/tanks/assets/images/tank1.png"
TANK2_IMAGE = "tanks/tanks/assets/images/tank2.png"
TANK1_SCALE = 0.1
TANK2_SCALE = 0.1
TANK1_ROTATION = 0
TANK2_ROTATION = 0

# RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGES = [f"tanks/tanks/assets/images/{n:03}.png" for n in range(100, 103)]
RACKET_WIDTH = 106
RACKET_HEIGHT = 28
RACKET_RATE = 6
RACKET_VELOCITY = 7

# BRICK
BRICK_GROUP = "bricks"
BRICK_IMAGES = {
    "b": [f"tanks/tanks/assets/images/{i:03}.png" for i in range(10,19)],
    "g": [f"tanks/tanks/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"tanks/tanks/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"tanks/tanks/assets/images/{i:03}.png" for i in range(40,49)]
}
BRICK_WIDTH = 80
BRICK_HEIGHT = 28
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"

COLUMNS = 40
ROWS = 20
CELL_SIZE = 20
#MAX_X = 900
#MAX_Y = 600
FONT_SIZE = 15
#CAPTION = "Tank"

ID_PLAYER1 = "Tank 1"
ID_PLAYER2 = "Tank 2"
X_POSITION_PLAYER1 = 100
X_POSITION_PLAYER2 = 800

#PLAYERS_MIN_HEALTH = 0
PLAYERS_MAX_HEALTH = 100

# Kind of meters
HEALTH_METER = "health_meter"
SHOOTING_POWER_METER = "shooting_power_meter"
PROJECTILE_POWER_METER = "projectile_power_meter"
METERS_SIZE = Point(80, 15)

AUDIO_DIRECTORY = "cse210-06/tank_game/assets/audios"
HIT_TANK = "cse210-06/tank_game/assets/audios/hit_tank.wav"
HIT_TERRAIN = "cse210-06/tank_game/assets/audios/hit_terrain.wav"
SHOT = "cse210-06/tank_game/assets/audios/shot.wav"