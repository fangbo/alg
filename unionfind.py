
"""
This file provides the implementation of union find which is used
to check if a gragh contains cycle or not.

The basic idea about union find is subsets partiton. Each element
is assigned to a subset. Two subsets can be unioned into a new
subset which elements in the two subsets are belonged to.

"""


def find(parent_array, i):
    if parent_array[i] == -1:
        return i

    return find(parent_array, parent_array[i])


def union(parent_array, x, y):
    xset = find(parent_array, x)
    yset = find(parent_array, y)

    parent_array[xset] = yset


class Edge(object):

    """
    src: the src vertice number of the edge

    dest: the dest vertice number of the edge

    """
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


class Graph(object):

    def __init__(self):
        self.edges = []

        self.vertices = []

    def add_edge(self, src, dest):
        self.edges.append(Edge(src, dest))

        if src not in self.vertices:
            self.vertices.append(src)

        if dest not in self.vertices:
            self.vertices.append(dest)

    def total_vertices(self):
        return len(self.vertices)

    def is_contains_cycle(self):

        parent_array = [-1 for x in range(self.total_vertices())]

        contains = False
        for edge in self.edges:
            # find the subset for src and dest
            x = find(parent_array, edge.src)
            y = find(parent_array, edge.dest)

            print "x=%s, y=%s" % (x, y)

            # src and dest are in the same subset
            if x == y:
                contains = True
                break

            # union src and dest
            union(parent_array, edge.src, edge.dest)

        return contains


if __name__ == "__main__":
    g = Graph()

    g.add_edge(0, 1)
    g.add_edge(0, 2)

    if g.is_contains_cycle():
        print "graph contains cycle"
    else:
        print "graph does not contains cycle"

    g = Graph()

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)

    if g.is_contains_cycle():
        print "graph contains cycle"
    else:
        print "graph does not contains cycle"
