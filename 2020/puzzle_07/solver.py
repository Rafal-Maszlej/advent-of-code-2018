from collections import deque
from typing import Dict, List


class Node:
    def __init__(self, color):
        self.color = color
        self.children = list()


class Graph:
    def __init__(self):
        self.nodes = dict()

    def is_child(self, node, color):
        deck = deque([child["color"] for child in node.children])

        while deck:
            node_color = deck.popleft()

            if node_color == color:
                return True

            node = self.nodes.get(node_color)
            deck.extend([child["color"] for child in node.children])

        return False

    def get_total_amount(self, node):
        deck = deque()

        for child in node.children:
            c = [child["color"]] * child["amount"]
            deck.extend(c)

        amount = 0

        while deck:
            node = self.nodes.get(deck.popleft())
            amount += 1

            for child in node.children:
                c = [child["color"]] * child["amount"]
                deck.extend(c)

        return amount


def create_graph(data: List) -> Graph:
    graph = Graph()

    for node_data in data:
        node = Node(node_data["color"])
        node.children = [
            {
                "color": child["color"],
                "amount": child["amount"]
            }
            for child in node_data["children"]
        ]
        graph.nodes[node.color] = node

    return graph


def parse_line(line: str) -> Dict:
    *color, line = line.strip().strip(".").replace(" bags contain", "").replace(" bags", "").replace(" bag", "").split(" ", maxsplit=2)

    if "no other" in line:
        children = []
    else:
        children = [
            {
                "color": "-".join(child[1:]),
                "amount": int(child[0])
            }
            for child in [color.strip().split(" ") for color in line.split(",")]
        ]
    return {
        "color": "-".join(color),
        "children": children
    }


def parse_data(data: List[str]) -> List:
    return [parse_line(line) for line in data]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.readlines()

    data = parse_data(data)
    graph = create_graph(data)

    # puzzle 1
    counter = 0

    for node in graph.nodes.values():
        if graph.is_child(node, "shiny-gold"):
            counter += 1

    assert counter == 164

    # puzzle 2
    node = graph.nodes.get('shiny-gold')
    amount = graph.get_total_amount(node)
    assert amount == 7872
