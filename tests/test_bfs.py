from pathlib import Path
import json

from tube_problem.bfs import bfs

def test_bfs():
    path = Path().cwd().joinpath("tests").joinpath("resources").joinpath("simple_test_data.json")
    with open(path, "r") as f:
        graph = json.loads(f.read())
    path = bfs(graph, "B", "F")
    assert len(path) == 4

def test_more_complex_bfs():
    path = Path().cwd().joinpath("tests").joinpath("resources").joinpath("complex_test_data.json")
    with open(path, "r") as f:
        graph = json.loads(f.read())
    path = bfs(graph, "B", "G")
    assert len(path) == 4
    assert ["B", "C", "D2", "G"] == path
