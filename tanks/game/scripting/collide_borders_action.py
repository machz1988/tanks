from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        projectiles = cast.get_actors(PROJECTILES_GROUP)
        for projectile in projectiles:
            body = projectile.get_body()
            position = body.get_position()
            x = position.get_x()
            y = position.get_y()
            destroy = False
            if x < 0 or x > SCREEN_WIDTH:
                destroy = True
            elif y > SCREEN_HEIGHT:
                destroy = True
            if destroy:
                cast.remove_actor(PROJECTILES_GROUP, projectile)