"""
Graph testing.
"""

import unittest
from Graph import Graph, Vertex, Edge

class TestGraph(unittest.TestCase):

    def test_empty_graph(self):
        g = Graph()
        self.assertEqual(g, {})

    def test_add_vertex(self):
        v1 = Vertex('1')
        v2 = Vertex('2')
        v3 = Vertex('3')

        g = Graph(vs=[v1, v2])
        self.assertTrue(v1 in g)
        self.assertTrue(v2 in g)

        g.add_vertex(v3)

        self.assertTrue(v3 in g)

    def test_add_edge(self):
        v1 = Vertex('1')
        v2 = Vertex('2')
        e1 = Edge(v1, v2)

        v3 = Vertex('3')
        v4 = Vertex('4')
        e2 = Edge(v3, v4)

        e3 = Edge(v1, v4)

        g = Graph(vs=[v1,v2,v3,v4], es=[e1,e2])

        # Ensure that each vertex has the correct edge
        self.assertTrue(e1 in g[v1].values())
        self.assertTrue(e1 in g[v2].values())
        self.assertTrue(e2 in g[v3].values())
        self.assertTrue(e2 in g[v4].values())

        g.add_edge(e3)

        self.assertTrue(e3 in g[v1].values())
        self.assertTrue(e3 in g[v4].values())


    def test_get_edge(self):

        v = Vertex(1)
        v2 = Vertex(2)
        e = Edge(v, v2)

        g = Graph(vs=[v,v2], es=[e])

        self.assertEqual(g.get_edge(v, v), None)
        self.assertEqual(g.get_edge(v, v2), e)

    def test_remove_edge(self):

        v = Vertex(1)
        v2 = Vertex(2)
        e = Edge(v, v2)

        g = Graph(vs=[v, v2], es=[e])

        g.remove_edge(e)

        self.assertEqual(g[v], {})
        self.assertEqual(g[v2], {})


    def test_list_vertices(self):

        v = Vertex(1)
        v2 = Vertex(2)
        v3 = Vertex(3)

        g = Graph(vs=[v, v2, v3], es=[])

        vertices = g.vertices()

        self.assertTrue(v in vertices)
        self.assertTrue(v2 in vertices)
        self.assertTrue(v3 in vertices)

    def test_list_edges(self):
        v = Vertex(1)
        v2 = Vertex(2)
        v3 = Vertex(3)

        e = Edge(v, v2)
        e2 = Edge(v2, v3)
        e3 = Edge(v3, v)

        g = Graph(vs=[v, v2, v3], es=[e, e2, e3])

        edges = g.edges()
        self.assertTrue(e in edges)
        self.assertTrue(e2 in edges)
        self.assertTrue(e3 in edges)

    def test_list_adjacent_vertices(self):

        v = Vertex(1)
        v2 = Vertex(2)
        v3 = Vertex(3)


        e = Edge(v, v2)
        e2 = Edge(v2, v3)
        e3 = Edge(v3, v)

        g = Graph([v, v2, v3], [e, e2, e3])
        adjacent = g.out_vertices(v)

        # Vertex v is connected to v2 and v3
        self.assertTrue(v2 in adjacent)
        self.assertTrue(v3 in adjacent)
        self.assertTrue(len(adjacent), 2)

    def test_list_connected_edges(self):

        v = Vertex(1)
        v2 = Vertex(2)
        v3 = Vertex(3)

        e = Edge(v, v2)
        e2 = Edge(v2, v3)
        e3 = Edge(v3, v)

        g = Graph([v, v2, v3], [e, e2, e3])
        connected_edges = g.out_edges(v)

        # Vertex v is connected by edges e and e3
        self.assertTrue(e in connected_edges)
        self.assertTrue(e3 in connected_edges)
        self.assertTrue(len(connected_edges), 2)


    def test_add_all_edges(self):

        v = Vertex(1)
        v2 = Vertex(2)

        g = Graph([v, v2])

        self.assertEqual(g.edges(), [])

        g.add_all_edges()

        self.assertEqual(g[v][v2], Edge(v2, v))
        self.assertEqual(g[v2][v], Edge(v2, v))

if __name__ == '__main__':
    unittest.main()
