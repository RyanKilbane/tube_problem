import json
from pathlib import Path
from load_data import load_json_data
from models.line_data import Stop, LineData, Lines

def bfs(graph, start, stop):
    explored = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            if isinstance(node, str):
                neighbours = graph[node]
            else:
                neighbours = graph[node.stop_name]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == stop:
                    return new_path
            explored.append(node)


# def bfs_objects(graph, start: str, stop: str):
#     pass