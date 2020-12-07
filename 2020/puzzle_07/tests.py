import pytest

from solver import parse_line, parse_data, create_graph


@pytest.fixture
def data():
    return """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split("\n")


def test_parse_line():
    line = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    expected_data = {
        "color": "light-red",
        "children": [
            {
                "color": "bright-white",
                "amount": 1
            },
            {
                "color": "muted-yellow",
                "amount": 2
            }
        ]
    }
    data = parse_line(line)
    assert data == expected_data


def test_create_graph(data):
    data = parse_data(data)
    graph = create_graph(data)
    assert len(graph.nodes) == 9

    node = graph.nodes.get("light-red")
    assert node.color == "light-red"
    assert len(node.children) == 2
    assert node.children[0]["color"] == "bright-white"
    assert node.children[0]["amount"] == 1
    assert node.children[1]["color"] == "muted-yellow"
    assert node.children[1]["amount"] == 2

    node = graph.nodes.get("dotted-black")
    assert len(node.children) == 0


if __name__ == "__main__":
    pytest.main([__file__])
