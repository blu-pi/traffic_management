import networkx as nx

from env.edge import Edge
from env.node import Node

class Intersection:

    nodes = {}
    nxgraph = nx.DiGraph()
    paths = {}

    def __init__(self, io_connection: int = 2) -> None:
        assert(io_connection >= 2)
        self.in_nodes = {}
        self.out_nodes = {}

        for x in range(io_connection):
            in_node = Node(self)
            out_node = Node(self)
    
    def registerNode(self, node : Node) -> None:
        ident = self.getNextNodeId()
        self.nodes[ident] = self
        self.nxgraph.add_node(ident)

    def getNextNodeId(self) -> int:
        if len(self.nodes) > 0:
            return max(self.nodes) + 1
        return 1
