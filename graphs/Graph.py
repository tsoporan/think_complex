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

    def remove_edge(self, e):
        """ Takes an edge and removes all references of it from the graph """

        v1, v2 = e

        # Edges are created in both directions, remove both references
        try:
            del self[v1][v2]
            del self[v2][v1]
        except KeyError:
            return None

    def vertices(self):
        """ Return list of graphs verticies """
        return self.keys()

    def edges(self):
        """ Return a list of graphs edges """
        es = []
        for k in self.keys():
            es += self[k].values()
        return es

    def out_vertices(self, v):
        """ Takes a vertex and returns list of adjacent vertices - the ones connected by a given edge"""
        if v in self:
            return self[v].keys()
        return []

    def out_edges(self, v):
        """ Takes a vertex and returns a list of edges connected to vertex """
        if v in self:
            return self[v].values()
        return []

    def add_all_edges(self):
        """ Starts with an edgeless graph and adds edges for all vertices """

        vertices = self.vertices()

        for i, j in enumerate(vertices):
            for k, l in enumerate(vertices):
                if i == k: break
                e = Edge(j, l)
                self.add_edge(e)

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
