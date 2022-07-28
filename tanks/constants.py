from game.casting.color import Color
from game.casting.point import Point

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Tanks"
#FRAME_RATE = 60
FRAME_RATE = 30

# PHYSICS
GRAVITY = 200
TIME_RATE = 0.03

# SCREEN
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
COLUMNS = 40
ROWS = 20
CELL_SIZE = 20

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "tanks/tanks/assets/fonts/zorque.otf"
#FONT_SIZE = 15
FONT_SMALL = 16
FONT_MEDIUM = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "tanks/tanks/assets/sounds/boing.wav"
WELCOME_SOUND = "tanks/tanks/assets/sounds/start.wav"
OVER_SOUND = "tanks/tanks/assets/sounds/over.wav"
AUDIO_DIRECTORY = "cse210-06/tank_game/assets/audios"
HIT_TANK = "cse210-06/tank_game/assets/audios/hit_tank.wav"
HIT_TERRAIN = "cse210-06/tank_game/assets/audios/hit_terrain.wav"
SHOT = "cse210-06/tank_game/assets/audios/shot.wav"

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
#MAXIMUM_HEALTH = 100

# HUD
HUD_MARGIN = 5
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# HEALTHS
HEALTH_GROUP = "healths"
HEALTH_STRING = "HEALTH"
HEALTH_FORMAT = "HEALTH: {}"
HEALTH_LABEL1_POSITION = Point(5, 42)
HEALTH_LABEL2_POSITION = Point(SCREEN_WIDTH - 140, 42)
HEALTH_MIN = 0
HEALTH_MAX = 100
HEALTH_1_POSITION = Point(75, 42)
HEALTH_2_POSITION = Point(SCREEN_WIDTH - 70, 42)
HEALTH_1_SIZE = Point(65, 15)
HEALTH_2_SIZE = Point(65, 15)

# SHOOTING POWER 
SHOOTING_POWER_GROUP = "shooting_power"
SHOOTING_POWER_STRING = "SHOT POW"
SHOOTING_POWER_FORMAT = "SHOOTING POWER: {}"
SHOOTING_POWER_LABEL1_POSITION = Point(5, 62)
SHOOTING_POWER_LABEL2_POSITION = Point(SCREEN_WIDTH - 140, 62)
SHOOTING_POWER_MIN = 100
SHOOTING_POWER_MAX = 500
SHOOTING_POWER_DEFAULT = 300
SHOOTING_POWER_1_POSITION = Point(75, 62)
SHOOTING_POWER_1_SIZE = Point(65, 15)
SHOOTING_POWER_2_POSITION = Point(SCREEN_WIDTH - 70, 62)
SHOOTING_POWER_2_SIZE = Point(65, 15)

# PROJECTILE POWER
PROJECTILE_POWER_GROUP = "projectiles_power"
PROJECTILE_POWER_STRING = "PROJ POW"
PROJECTILE_POWER_FORMAT = "PROJECTILES POWER: {}"
PROJECTILE_POWER_LABEL1_POSITION = Point(5, 82)
PROJECTILE_POWER_LABEL2_POSITION = Point(SCREEN_WIDTH - 140, 82)
PROJECTILE_POWER_MIN = 10
PROJECTILE_POWER_MAX = 50
PROJECTILE_DEFAULT_POWER = 20
PROJECTILE_POWER_1_POSITION = Point(75, 82)
PROJECTILE_POWER_1_SIZE = Point(65, 15)
PROJECTILE_POWER_2_POSITION = Point(SCREEN_WIDTH - 70, 82)
PROJECTILE_POWER_2_SIZE = Point(65, 15)



# PROJECTILES
PROJECTILES_GROUP = "projectiles"
PROJECTILE_SIZE = Point(14,14)
PROJECTILE_RADIUS = 7
PROJECTILE_IMAGE = "tanks/tanks/assets/images/projectile.png"
PROJECTILE_SCALE = 0.5
PROJECTILE_ROTATION = 0.0
PROJECTILE_EXAMPLE_V0 = 350
PROJECTILE_EXAMPLE_POWER = 20
PROJECTILE_EXAMPLE_ANGLE = 60

# PROJECTIONS
PROJECTIONS_GROUP = "projections"
PROJECTION_SIZE = Point(6, 6)
PROJECTION_IMAGE = "tanks/tanks/assets/images/projectile.png"
PROJECTION_COLOR = WHITE
PROJECTION_RADIUS = 3
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
TANK1_SCALE = 0.05
TANK2_SCALE = 0.05
TANK1_ROTATION = 0
TANK2_ROTATION = 0


# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"