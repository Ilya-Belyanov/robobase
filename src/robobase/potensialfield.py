import math

import numpy as np


def gradient_based_planner(f, start_coords, end_coords, max_its):
    gradient_x = np.gradient(f, axis=0)
    gradient_y = np.gradient(f, axis=1)
    route = [start_coords]
    cur_coords = np.array(start_coords)
    for _ in range(max_its):
        direction = np.array([gradient_x[int(cur_coords[0])][int(cur_coords[1])],
                              gradient_y[int(cur_coords[0])][int(cur_coords[1])]])
        direction = direction / math.sqrt(direction[0] ** 2 + direction[1] ** 2)

        cur_coords = np.array([cur_coords[0] - direction[0], cur_coords[1] - direction[1]])

        if cur_coords[0] < 1:
            cur_coords[0] = 0
        elif cur_coords[0] > len(f) - 1:
            cur_coords[0] = len(f) - 1
        if cur_coords[1] < 1:
            cur_coords[1] = 0
        elif cur_coords[1] > len(f[0]) - 1:
            cur_coords[1] = len(f[0]) - 1

        route.append(list(map(int, cur_coords)))
        dist_to_end = end_coords - cur_coords
        if dist_to_end[0] ** 2 + dist_to_end[1] ** 2 < 4:
            route.append(end_coords)
            break
    return route
