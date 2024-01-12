
from typing import TYPE_CHECKING

from util.path_errors import AmbiguousPathError
#the fact that I even havce to do this is a joke. Thanks pylance. 
if TYPE_CHECKING:
    from edge import Edge
    from graph import Intersection
    

class Node:

    def __init__(self, graph : 'Intersection', neighbours : dict = {}) -> None:
        self.neighbours = neighbours
        graph.registerNode(self)

    def addNeighbour(self, edge: 'Edge') -> None:
        if edge.dest not in self.neighbours:
            self.neighbours.update({edge.dest : edge})
        else:
            AmbiguousPathError(
                "Edge not added, there already exists an edge connecting {} and {}!".format(edge.orig, edge.dest))
    
    def removeNeighbour(self, edge: 'Edge') -> None:
        pass