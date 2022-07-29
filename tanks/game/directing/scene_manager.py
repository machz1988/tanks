import csv
from constants import *
from levels import *
from game.casting.animation import Animation
from game.casting.projectile import Projectile
from game.casting.rectangle import Rectangle
from game.casting.terrain import Terrain
from game.casting.meter import Meter
from game.casting.label import Label
from game.casting.point import Point
from game.casting.tank import Tank
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_tank_action import CollideTankAction
from game.scripting.collide_terrain_action import CollideTerrainAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_projectiles_action import DrawProjectilesAction
from game.scripting.draw_projections_action import DrawProjectionsAction
from game.scripting.draw_terrain_action import DrawTerrainAction
from game.scripting.draw_tanks_action import DrawTanksAction
from game.scripting.draw_stats_action import DrawStatsAction
from game.scripting.draw_messages_action import DrawMessagesAction
from game.scripting.draw_meters_action import DrawMetersAction
from game.scripting.draw_welcome_action import DrawWelcomeAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.generate_aim_action import GenerateAimAction
from game.scripting.handle_keys_pressed import HandleKeysPressed
from game.scripting.handle_mouse_pressed import HandleMousePressed
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_projectiles_action import MoveProjectilesAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_mouse_service import RaylibMouseService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    MOUSE_SERVICE = RaylibMouseService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_TERRAIN_ACTION = CollideTerrainAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_TANK_ACTION = CollideTankAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_PROJECTILES_ACTION = DrawProjectilesAction(VIDEO_SERVICE)
    DRAW_PROJECTIONS_ACTION = DrawProjectionsAction(VIDEO_SERVICE)
    DRAW_TANKS_ACTION = DrawTanksAction(VIDEO_SERVICE)
    DRAW_TERRAIN_ACTION = DrawTerrainAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_RACKET_ACTION= DrawMessagesAction(VIDEO_SERVICE)
    DRAW_METERS_ACTION = DrawMetersAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    GENERATE_AIM_ACTION = GenerateAimAction(MOUSE_SERVICE)
    HANDLE_KEYS_PRESSED = HandleKeysPressed(KEYBOARD_SERVICE)
    HANDLE_MOUSE_PRESSED = HandleMousePressed(MOUSE_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_PROJECTILES_ACTION = MoveProjectilesAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        #self._add_stats(cast)
        #self._add_level(cast)
        #self._add_lives(cast)
        #self._add_score(cast)
        #self._add_tanks(cast)
        #self._add_terrain(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script_dialogs(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_health(cast)
        self._add_shooting_power(cast)
        self._add_projectile_power(cast)
        self._add_terrain(cast)
        self._add_tanks(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        #script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))

        
    def _prepare_try_again(self, cast, script):
        #self._add_ball(cast)
        #self._add_racket(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        #self._add_update_script(script)
        self._reset_healths(cast)
        self._add_output_script_dialogs(script)

    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)
        self._add_input_script(script)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_ball(cast)
        self._add_racket(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script_dialogs(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------

    def _add_terrain(self, cast):
        """Adds the terrain on a new scene
        Args:
            cast (Cast): the cast of actors
        """
        cast.clear_actors(TERRAIN_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level()
        terrain = Terrain(LEVELS[level]["terrain"], TERRAIN_IMAGE)
        cast.add_actor(TERRAIN_GROUP, terrain)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_MEDIUM, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_MEDIUM, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_MEDIUM, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_health(self, cast):
        cast.clear_actors(HEALTH_GROUP)
        # health 1
        text = Text(HEALTH_STRING, FONT_FILE, FONT_SMALL)
        position = HEALTH_LABEL1_POSITION
        label = Label(text, position)
        holder = Rectangle(HEALTH_1_POSITION, HEALTH_1_SIZE)
        health = Meter(label, holder, HEALTH_MAX, HEALTH_MIN, HEALTH_MAX, GREEN)
        cast.add_actor(HEALTH_GROUP, health)
        # health 1
        text = Text(HEALTH_STRING, FONT_FILE, FONT_SMALL)
        position = HEALTH_LABEL2_POSITION
        label = Label(text, position)
        holder = Rectangle(HEALTH_2_POSITION, HEALTH_2_SIZE)
        health = Meter(label, holder, HEALTH_MAX, HEALTH_MIN, HEALTH_MAX, GREEN)
        cast.add_actor(HEALTH_GROUP, health)
    
    def _add_projectile_power(self, cast):
        cast.clear_actors(PROJECTILE_POWER_GROUP)
        # projectile power 1
        text = Text(PROJECTILE_POWER_STRING, FONT_FILE, FONT_SMALL)
        position = PROJECTILE_POWER_LABEL1_POSITION
        label = Label(text, position)
        holder = Rectangle(PROJECTILE_POWER_1_POSITION, PROJECTILE_POWER_1_SIZE)
        projectile_power = Meter(label, holder, PROJECTILE_DEFAULT_POWER, PROJECTILE_POWER_MIN, PROJECTILE_POWER_MAX, RED)
        cast.add_actor(PROJECTILE_POWER_GROUP, projectile_power)
        # projectile power 2
        #text = Text(PROJECTILES_POWER_STRING, FONT_FILE, FONT_SMALL)
        position = PROJECTILE_POWER_LABEL2_POSITION
        label = Label(text, position)
        holder = Rectangle(PROJECTILE_POWER_2_POSITION, PROJECTILE_POWER_2_SIZE)
        projectile_power = Meter(label, holder, PROJECTILE_DEFAULT_POWER, PROJECTILE_POWER_MIN, PROJECTILE_POWER_MAX, RED)
        cast.add_actor(PROJECTILE_POWER_GROUP, projectile_power)

    def _add_shooting_power(self, cast):
        cast.clear_actors(SHOOTING_POWER_GROUP)
        # shooting power 1
        text = Text(SHOOTING_POWER_STRING, FONT_FILE, FONT_SMALL)
        label = Label(text, SHOOTING_POWER_LABEL1_POSITION)
        holder = Rectangle(SHOOTING_POWER_1_POSITION, SHOOTING_POWER_1_SIZE)
        shooting_power = Meter(label, holder, SHOOTING_POWER_DEFAULT, SHOOTING_POWER_MIN, SHOOTING_POWER_MAX, YELLOW)
        cast.add_actor(SHOOTING_POWER_GROUP, shooting_power)
        # shooting power 2
        text = Text(SHOOTING_POWER_STRING, FONT_FILE, FONT_SMALL)
        label = Label(text, SHOOTING_POWER_LABEL2_POSITION)
        holder = Rectangle(SHOOTING_POWER_2_POSITION, SHOOTING_POWER_2_SIZE)
        shooting_power = Meter(label, holder, SHOOTING_POWER_DEFAULT, SHOOTING_POWER_MIN, SHOOTING_POWER_MAX, YELLOW)
        cast.add_actor(SHOOTING_POWER_GROUP, shooting_power)    

    def _add_stats(self, cast):
        #cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_tanks(self, cast):
        cast.clear_actors(TANKS_GROUP)
        terrain = cast.get_first_actor(TERRAIN_GROUP)
        pos_tank1 = terrain.get_tank1_position()
        x1 = pos_tank1.get_x()
        y1 = pos_tank1.get_y()
        pos_tank1 = Point(x1,y1)
        pos_tank2 = terrain.get_tank2_position()
        x2 = pos_tank2.get_x()
        y2 = pos_tank2.get_y()
        pos_tank2 = Point(x2,y2)
        tank1 = Tank(pos_tank1, TANK1_SIZE, TANK1_VELOCITY, TANK1_IMAGE, TANK1_SCALE, TANK1_ROTATION)
        tank2 = Tank(pos_tank2, TANK2_SIZE, TANK2_VELOCITY, TANK2_IMAGE, TANK2_SCALE, TANK2_ROTATION)
        cast.add_actor(TANKS_GROUP, tank1)
        cast.add_actor(TANKS_GROUP, tank2)

    def _reset_healths(self, cast):
        healths = cast.get_actors(HEALTH_GROUP)
        for health in healths:
            health.update_value(HEALTH_MAX)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script_dialogs(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        #script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_TERRAIN_ACTION)
        script.add_action(OUTPUT, self.DRAW_TANKS_ACTION)
        script.add_action(OUTPUT, self.DRAW_PROJECTIONS_ACTION)
        script.add_action(OUTPUT, self.DRAW_PROJECTILES_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_METERS_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_PROJECTILES_ACTION)
        script.add_action(UPDATE, self.COLLIDE_TANK_ACTION)
        script.add_action(UPDATE, self.COLLIDE_TERRAIN_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)
    
    def _add_input_script(self, script):
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.HANDLE_KEYS_PRESSED)
        script.add_action(INPUT, self.GENERATE_AIM_ACTION)
        script.add_action(INPUT, self.HANDLE_MOUSE_PRESSED)