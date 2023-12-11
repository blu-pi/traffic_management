from env.edge import Edge
from util.errors import AmbiguousPathError

class Node:

    def __init__(self, id : str, neighbours : dict = {}) -> None:
        self.id = id
        self.neighbours = neighbours

    def addNeighbour(self, edge: Edge) -> None:
        if edge.dest not in self.neighbours:
            self.neighbours.update({edge.dest : edge})
        else:
            AmbiguousPathError(
                "Edge not added, there already exists an edge connecting {} and {}!".format(edge.orig, edge.dest))
    
    def removeNeighbour(self, edge: Edge) -> None:
        pass