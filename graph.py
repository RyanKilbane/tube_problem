class Node:
    def __init__(self, node_name, line, adjacent=None):
        self.node_name = node_name
        self.line = line
        self.adj = adjacent
        self.is_explored = False

    def __hash__(self):
        return hash(self.node_name)

    def __eq__(self, value):
        return hash(value) == hash(self.node_name)

    def __str__(self):
        return f"take {self.node_name} on {self.line}\n"
