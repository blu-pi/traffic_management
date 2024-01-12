
class PathException(Exception):

    def __init__(self, message : str = "A PathException occured") -> None:
        self.message = message
        super().__init__(self.message)


class GraphLoopError(PathException):
    
    def __init__(self, message : str = "A GraphLoopError occured") -> None:
        self.message = message
        super().__init__(self.message)


class AmbiguousPathError(PathException):
    """When 2 or more paths connect the same 2 Nodes"""
    def __init__(self, message : str = "A AmbiguousPathError occured") -> None:
        self.message = message
        super().__init__(self.message)