from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        self._draw_label(cast, LEVEL_GROUP, LEVEL_FORMAT, stats.get_level())
        self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT, stats.get_lives())
        self._draw_label(cast, SCORE_GROUP, SCORE_FORMAT, stats.get_score())
        #self._draw_label(cast, HEALTH_GROUP, HEALTH_FORMAT, stats.get_health())
        #self._draw_label(cast, PROJECTILE_POWER_GROUP, PROJECTILE_POWER_FORMAT, stats.get_projectile_power())
        #self._draw_label(cast, SHOOTING_POWER_GROUP, SHOOTING_POWER_FORMAT, stats.get_shooting_power())

    # **********************************************************************************************
    # You found the bug. Great job!
    # **********************************************************************************************
    # todo: fix the bug by making sure the text value is set to the appropriate variable.
    def _draw_label(self, cast, group, format_str, data):
        the_value_to_display = format_str.format(data)
        label = cast.get_first_actor(group)
        text = label.get_text()
        #text.set_value(format_str)
        text.set_value(the_value_to_display)
        position = label.get_position()
        self._video_service.draw_text(text, position)