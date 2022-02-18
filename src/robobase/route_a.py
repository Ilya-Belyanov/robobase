import math

from .routecommon import Node, create_graph, id_by_coord, path_from_to, neighbors


class NodeA(Node):
    """node for A* algorithm graph"""
    g = float('inf')
    f = float('inf')


def h_function(node_coord, dest_coords):
    return math.sqrt((node_coord[0] - dest_coords[0])**2 + (node_coord[1] - dest_coords[1])**2)


def min_f_id(list_id, graph):
    result = list_id[0]
    for i in list_id:
        if graph[i].f < graph[result].f:
            result = i
    return result


def a_star_grid(input_map, start_coords, dest_coords):
    graph = create_graph(input_map, NodeA)
    start_id = id_by_coord(start_coords, graph)
    graph[start_id].g = 0
    graph[start_id].f = h_function(graph[start_id].coord, dest_coords)
    not_watched = list([start_id])
    while len(not_watched) != 0:
        current_id = min_f_id(not_watched, graph)
        not_watched.remove(current_id)
        graph[current_id].is_watched = True
        near_id = neighbors(current_id, graph)
        for n_id in near_id:
            if graph[n_id].g > graph[current_id].g + 1:
                graph[n_id].g = graph[current_id].g + 1
                graph[n_id].f = graph[current_id].f + h_function(graph[n_id].coord, dest_coords)
                graph[n_id].parent_id = current_id
            if not graph[n_id].is_watched:
                not_watched.append(n_id)
    return path_from_to(graph, start_coords, dest_coords)
