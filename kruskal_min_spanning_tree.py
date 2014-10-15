
"""

This is the implementation of Kruskal Minimum Spanning Tree.

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
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest

        self.weight = weight


class Graph(object):

    def __init__(self):
        self.edges = []

        self.vertices = []

    def add_edge(self, src, dest, weight):
        self.edges.append(Edge(src, dest, weight))

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

    def kruskal_span_tree(self):

        span_tree = Graph()

        # sort the edges order by weights
        self.edges.sort(key=lambda item: item.weight)

        i = 0
        total_vertices = self.total_vertices()

        for each_edge in self.edges:
            parent_array = [-1 for x in range(total_vertices)]

            # check if span_tree contains cycle or not.
            cycle = False
            edges = [x for x in span_tree.edges]
            edges.append(each_edge)

            for edge in edges:
                # find the subset for src and dest
                x = find(parent_array, edge.src)
                y = find(parent_array, edge.dest)

                # src and dest are in the same subset
                if x == y:
                    cycle = True
                    break

                # union src and dest
                union(parent_array, edge.src, edge.dest)

            if not cycle:
                span_tree.edges.append(each_edge)

            if i == total_vertices:
                break

            i += 1

        return span_tree

if __name__ == "__main__":
    g = Graph()

    g.add_edge(0, 1, 3)
    g.add_edge(0, 2, 1)

    if g.is_contains_cycle():
        print "graph contains cycle"
    else:
        print "graph does not contains cycle"

    g = Graph()

    g.add_edge(0, 1, 3)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 0)
    g.add_edge(2, 3, 1)

    if g.is_contains_cycle():
        print "graph contains cycle"
    else:
        print "graph does not contains cycle"

    print [(edge.src, edge.dest) for edge in g.kruskal_span_tree().edges]
