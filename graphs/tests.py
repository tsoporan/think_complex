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
        pass

    def test_list_verticies(self):
        pass

    def test_list_edges(self):
        pass

    def test_list_adjacent_vertices(self):
        pass

    def test_list_connected_edges(self):
        pass

    def test_add_all_edges(self):
        pass


if __name__ == '__main__':
    unittest.main()
