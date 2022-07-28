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
            circle = projectile.get_circle()
            center = circle.get_center()
            x = center.get_x()
            y = center.get_y()
            destroy = False
            if x < 0 or x > SCREEN_WIDTH:
                destroy = True
            elif y > SCREEN_HEIGHT:
                destroy = True
            if destroy:
                cast.remove_actor(PROJECTILES_GROUP, projectile)