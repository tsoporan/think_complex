"""
From Think Complexity Lecture 1 - http://greenteapress.com/complexity/

Exercise on Graphs, lightly adapted for Python3
"""

class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """
        Create a new graph
        vs list of verticies
        es list of edges
        """
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """ Add vertex v to graph """
        self[v] = {}

    def add_edge(self, e):
        """
        Add edge e to graph by adding an entry in both directions.
        If there is already an edge connecting these Verticies, the
        new edge replaces it
        """
        v1, v2 = e
        self[v1][v2] = e
        self[v2][v1] = e

    def get_edge(self, v1, v2):
        """Providied two verticies get the edge between them"""

        try:
            return self[v1][v2]
        except KeyError:
            return None

class Vertex(object):
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__

class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__

def main(script, args):
    v = Vertex('v')
    print(v)
    w = Vertex('w')
    print(w)
    e = Edge(v, w)
    print(e)
    g = Graph([v,w], [e])
    print(g)

if __name__ == '__main__':
    import sys
    main(*sys.argv)
