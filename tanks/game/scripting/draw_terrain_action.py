from game.scripting.action import Action
from game.casting.rectangle import Rectangle
from game.casting.point import Point
from game.casting.image import Image
import constants


class DrawTerrainAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service 
        
    def execute(self, cast, script, callback):
        terrain = cast.get_first_actor(constants.TERRAIN_GROUP)
        surface = terrain.get_surface()
        image = terrain.get_image()
        for i in range(len(surface)):
            position = surface[i].get_position()
            self._video_service.draw_image(image, position)