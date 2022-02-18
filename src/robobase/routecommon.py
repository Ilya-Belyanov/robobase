class Node:
    """common node for graph"""
    parent_id = -1
    coord = [-1, -1]
    is_watched = False


def create_graph(input_map: list, node_class):
    graph = {}
    count = 0
    for x_coord, _ in enumerate(input_map):
        for y_coord, _ in enumerate(input_map[x_coord]):
            if not input_map[x_coord][y_coord]:
                node = node_class()
                node.coord = [x_coord, y_coord]
                graph[count] = node
                count += 1
    return graph


def id_by_coord(coord: list, graph: dict):
    for key in graph.keys():
        if graph[key].coord == coord:
            return key
    return -1


def neighbors(key: list, graph: dict):
    coord = graph[key].coord

    near_coords = [[coord[0] + 1, coord[1]],
                   [coord[0] - 1, coord[1]],
                   [coord[0], coord[1] + 1],
                   [coord[0], coord[1] - 1]]

    result = list()
    for n in near_coords:
        id_n = id_by_coord(n, graph)
        if id_n != -1:
            result.append(id_n)
    return result


def path_from_to(graph: dict, start_coords: list, dest_coords: list):
    path = list([dest_coords])
    current_coord = dest_coords
    dest_parent = graph[id_by_coord(current_coord, graph)].parent_id
    if dest_parent == -1:
        return list()
    while current_coord != start_coords:
        parent_id = graph[id_by_coord(current_coord, graph)].parent_id
        current_coord = graph[parent_id].coord
        path.append(current_coord)
    return path[::-1]
