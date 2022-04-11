import json
from typing import Dict, List
from pathlib import Path
from models.line_data import Stop, LineData, Lines
from graph import Node

def load_json_data(path):
    with open(path, "r") as f:
        return json.loads(f.read())

# ETL bellow this point
def load_data(path):
    with open(path, "r") as f:
        data = json.loads(f.read())
    lines = []
    for line in data["lines"]:
        stops = []
        for stop in line["stops"]:
            stops.append(Stop(on_line=line["line_name"], stop_name=stop))
        line_data = LineData(line_name=line["line_name"], stops=stops)
        lines.append(line_data)
    return Lines(lines=lines)

def find_adjacent(data, current_stop):
    for index, stop in enumerate(data.stops):
        if stop == current_stop and index+1 < len(data.stops):
            yield data.stops[index+1]
        if stop == current_stop and index-1 >= 0:
            yield data.stops[index-1]
        else:
            continue

def build_adj_list(data: Lines):
    output = {}
    for line in data.lines:
        for index, stop in enumerate(line.stops):
            if stop.stop_name not in output:
                output[stop.stop_name] = set()
            for adjacent in find_adjacent(line, stop):
                output[stop.stop_name].add(adjacent)
    return output

def convert_to_node_objects(data: Dict[str, List[Stop]]):
    output = {}
    nodes = []
    for i in data:
        for stop in data[i]:
            if i not in output:
                output[i] = []
            else:
                new_node = Node(stop.stop_name, stop.on_line)
                output[i].append(new_node)
    return output

def swap_set_for_array(data):
    output = {}
    for stop in data:
        output[stop] = list(data[stop])
    return output
