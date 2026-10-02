from utils import display_graph_from_dict

graphe = {
    "A": ["B"],
    "B": [],
    "C": ["A", "B"],
    "D": ["C"],
    "E": ["C", "D"]
}

display_graph_from_dict(graphe)