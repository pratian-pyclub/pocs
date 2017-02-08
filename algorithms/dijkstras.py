from collections import defaultdict
class Graph:
    def __init__(self, start, end):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.start = start
        self.end = end

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

small_graph = Graph('a', 'd')
small_graph.add_node('a')
small_graph.add_node('b')
small_graph.add_node('c')
small_graph.add_node('d')

small_graph.add_edge('a', 'b', 1)
small_graph.add_edge('a', 'c', 2)
small_graph.add_edge('b', 'd', 3)
small_graph.add_edge('c', 'd', 4)

small_graph.distances

large_graph = Graph('a', 'c')
large_graph.add_node('a')
large_graph.add_node('b')
large_graph.add_node('c')
large_graph.add_node('d')
large_graph.add_node('e')

large_graph.add_edge('a', 'b', 10)
large_graph.add_edge('a', 'd', 30)
large_graph.add_edge('a', 'e', 100)
large_graph.add_edge('b', 'c', 50)
large_graph.add_edge('c', 'e', 10)
large_graph.add_edge('d', 'c', 20)
large_graph.add_edge('d', 'e', 60)

large_graph.distances

def plot(start, weighted_path, g, routes):
    if weighted_path['path'][-1] == g.end:
        routes.append(weighted_path)

    for edge in g.edges[start]:
        if edge not in weighted_path['path']:
            if g.distances[(start, edge)]:
                newpath = weighted_path['path'] + [edge]
                newweight = weighted_path['weight'] + g.distances[(start, edge)]

                plot(edge, {'path': newpath, 'weight': newweight}, g, routes)

    return routes

def travel(g):
    weighted_path = {'path': [g.start], 'weight': 0}
    return plot(g.start, weighted_path, g, [])

print travel(small_graph)
print travel(large_graph)
