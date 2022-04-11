import argparse
import json
from pathlib import Path
from load_data import load_json_data, load_data, build_adj_list, convert_to_node_objects
from models.line_data import Stop, LineData, Lines
from bfs import bfs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", required=True)
    parser.add_argument("--stop", required=True)
    args = parser.parse_args()
    graph = load_data("line_data.json")
    graph = build_adj_list(graph)
    # print(graph)

    path = bfs(graph, args.start, args.stop)
    path_str = '\n'.join(str(i) for i in path)
    print(path_str)

main()