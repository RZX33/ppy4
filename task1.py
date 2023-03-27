import math


def panel_calc(room_length, room_width, panel_length, panel_width, panel_box):

    room_area = room_length*room_width*1.1
    panel_area = panel_length*panel_width
    panel_quantity = math.ceil(room_area/panel_area)
    return math.ceil(panel_quantity/panel_box)
print(panel_calc(4, 4, 0.20, 1, 10))