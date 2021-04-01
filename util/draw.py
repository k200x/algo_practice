import matplotlib.pyplot as plt
import networkx as nx


# mock data
def init_graph():
    G = nx.Graph()
    G.add_edge(0, 1, weight=2)
    G.add_edge(0, 3, weight=6)
    G.add_edge(1, 2, weight=3)
    G.add_edge(1, 3, weight=8)
    G.add_edge(1, 4, weight=5)
    G.add_edge(2, 4, weight=7)
    G.add_edge(3, 4, weight=9)
    return G


def draw_graph(G):
    options = {
        "font_size": 24,
        "node_size": 1000,
        "node_color": "white",
        "edgecolors": "blue",
        "linewidths": 3,
        "width": 3,
    }
    nx.draw_networkx(G, **options)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()


def draw_weight_graph(G):
    options = {
        "font_size": 24,
        "node_size": 1000,
        "node_color": "white",
        "edgecolors": "blue",
        "linewidths": 3,
        "width": 3,
    }

    pos = nx.nx_agraph.graphviz_layout(G)

    ax = plt.gca()
    ax.margins(0.20)
    nx.draw_networkx(G, pos, **options)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def convert_adjacent_matrix_to_graph(a_m: list) -> nx.Graph:
    G = nx.Graph()
    for u in range(0, len(a_m)):
        for v in range(0, len(a_m[u])):
            if v > u and a_m[u][v] > 0:
                G.add_edge(u, v, weight=a_m[u][v])
    return G
