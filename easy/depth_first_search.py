class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    # O(V + E) time | O(V) space
    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array

    def show(self, n):
        print(n.name)
        for c in n.children:
            print([c.name for c in n.children])
            self.show(c)


if __name__ == "__main__":
    # d = {
    #     "graph": {
    #         "nodes": [
    #             {"children": ["B", "C", "D"], "id": "A", "value": "A"},
    #             {"children": ["E", "F"], "id": "B", "value": "B"},
    #             {"children": [], "id": "C", "value": "C"},
    #             {"children": ["G", "H"], "id": "D", "value": "D"},
    #             {"children": [], "id": "E", "value": "E"},
    #             {"children": ["I", "J"], "id": "F", "value": "F"},
    #             {"children": ["K"], "id": "G", "value": "G"},
    #             {"children": [], "id": "H", "value": "H"},
    #             {"children": [], "id": "I", "value": "I"},
    #             {"children": [], "id": "J", "value": "J"},
    #             {"children": [], "id": "K", "value": "K"}
    #         ],
    #         "startNode": "A"
    #     }
    # }

    g = Node("A")
    g.add_child("B").add_child("C").add_child("D")
    g.children[0].add_child("E").add_child("F")
    g.children[2].add_child("G").add_child("H")
    g.children[0].children[1].add_child("I").add_child("J")
    g.children[2].children[0].add_child("K")

    print(g.depth_first_search([]))
