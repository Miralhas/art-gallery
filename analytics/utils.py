from random import random

def color_generator(qtd=1):
    bg_color = []
    border_color = []
    for _ in range(qtd):
        r = random() * 255
        g = random() * 255
        b = random() * 255
        bg_color.append(f"rgba({r}, {g}, {b}, {0.5})")
        border_color.append(f"rgba({r}, {g}, {b}, {0.5})")

    return [bg_color, border_color]


def single_color_bar_vs_all_others(index, quantity):
    bg_color = []
    border_color = []

    r = random() * 255
    g = random() * 255
    b = random() * 255
    random_background_color = f"rgba({r}, {g}, {b}, {0.07})"
    random_border_color = f"rgba({r}, {g}, {b}, {0.1})"

    for i in range(quantity):
        if i == index:
            r = random() * 255
            g = random() * 255
            b = random() * 255
            bg_color.append(f"rgba({r}, {g}, {b}, {1})")
            border_color.append(f"rgba({r}, {g}, {b}, {1})")
        else:
            bg_color.append(random_background_color)
            border_color.append(random_border_color)

    return [bg_color, border_color]

