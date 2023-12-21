from random import random

def color_generator(qtd=1):
    bg_color = []
    border_color = []
    for i in range(qtd):
        r = random() * 255;
        g = random() * 255;
        b = random() * 255;
        bg_color.append(f"rgba({r}, {g}, {b}, {0.5})")
        border_color.append(f"rgba({r}, {g}, {b}, {0.5})")

    return [bg_color, border_color]