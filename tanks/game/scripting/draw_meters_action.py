import constants
from game.scripting.action import Action

class DrawMetersAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service 
        
    def execute(self, cast, script, callback):
        healths = cast.get_actors(constants.HEALTH_GROUP)
        shooting_powers = cast.get_actors(constants.SHOOTING_POWER_GROUP)
        projectile_powers = cast.get_actors(constants.PROJECTILE_POWER_GROUP)
        for health in healths:
            label = health.get_label()
            label_t = label.get_text()
            label_p = label.get_position()
            holder = health.get_holder()
            value_holder = health.get_value_holder()
            color = health.get_color()
            self._video_service.draw_text_pro(label_t, label_p, 0, color)
            self._video_service.draw_rectangle(holder, constants.WHITE, True)
            self._video_service.draw_rectangle(value_holder, color, True)
        for shooting_power in shooting_powers:
            label = shooting_power.get_label()
            label_t = label.get_text()
            label_p = label.get_position()
            holder = shooting_power.get_holder()
            value_holder = shooting_power.get_value_holder()
            color = shooting_power.get_color()
            self._video_service.draw_text_pro(label_t, label_p, 0, color)
            self._video_service.draw_rectangle(holder, constants.WHITE, True)
            self._video_service.draw_rectangle(value_holder, color, True)
        for projectile_power in projectile_powers:
            label = projectile_power.get_label()
            label_t = label.get_text()
            label_p = label.get_position()
            holder = projectile_power.get_holder()
            value_holder = projectile_power.get_value_holder()
            color = projectile_power.get_color()
            self._video_service.draw_text_pro(label_t, label_p, 0, color)
            self._video_service.draw_rectangle(holder, constants.WHITE, True)
            self._video_service.draw_rectangle(value_holder, color, True)

