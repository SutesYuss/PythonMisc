"""Author: Sudi Yussuf
Due: Feb 27, 2022
"""
import collections
from abc import ABC, abstractmethod
class Graph(ABC):
    """Abstract class representing a graph.
    A graph is modeled as a pair of sets (vertices, edges).
    Each element of edges is a tuple (v1, v2) where v1 and v2 are both in vertices.
    """
    @abstractmethod
    def __repr__(self):
        """Returns a string representation of self using the underlying 
representation."""
        return f"{type(self)}:{str(self)}"
    @property
    @abstractmethod
    def vertices(self) -> set:
        """A set of all vertices in self."""
    @property
    @abstractmethod
    def edges(self):
        """A set of all edges in self.
        Each edge is a collection of two vertices.
        """
    @abstractmethod
    def degree(self, vertex) -> int:
        """Returns the degree of vertex.
        Returns the number of edges incident on vertex.
        """
    @abstractmethod
    def adjacent_to(self, vertex):
        """Returns a set of all vertices in self adjacent to vertex."""
    @abstractmethod
    def add_vertex(self, vertex):
        """Adds vertex to self.vertices."""
    @abstractmethod
    def add_edge(self, edge):
        """Adds edge to self.edges.
        Assumes: edge[0] and edge[1] are both in self.vertices.
        """
    @abstractmethod
    def remove_vertex(self, vertex):
        """Removes vertex and all incident edges from self.
        Assumes: vertex in self.vertices.
        """
    @abstractmethod
    def remove_edge(self, edge):
        """Removes edge from self, leaving the endpoints in self.vertices.
        Assumes: edge in self.edges.
        """
    # Non-abstract methods
    def __eq__(self, other):
        """Returns true iff self.vertices is exactly the same as other.vertices and
self.edges is
            exactly the same as other.edges."""
        return self.vertices == other.vertices and self.edges == other.edges
    def __str__(self):
        """Returns a string representation of self as a pair of sets."""
        vertex_set = set(self.vertices)
        edge_set = {tuple(edge) for edge in self.edges}
        return f"({vertex_set}, {edge_set})"
    def __imul__(self, vertex):
        """Adds vertex to self.
        Called by the *= operator.
        """
        self.add_vertex(vertex)
    def __iadd__(self, edge):
        """Adds edge to self.
        Called by the += operator.
        """
        self.add_edge(*edge)
    def __itruediv__(self, vertex):
        """Removes vertex and all incident edges from self.
        Called by the /= operator.
        """
        self.remove_vertex(vertex)
    def __isub__(self, edge):
        """Removes edge from self, leaving the endpoints in self.
        Called by the -= operator.
        """
        self.remove_edge(edge)
    def __iter__(self):
        """Returns an iterator over the vertices of self.
        The implementation provided here does not guarantee any order to the
            vertices seen while iterating.
        """

        return iter(self.vertices)
    def depth_first_search(self, start=None):
      if start is None:
        yield print("invalid input")
      visited = []
      list1 = set()
      list1.add(start)
      while len(list) != 0:
        x = list.pop()
        if x not in visited:
          visited.append(start)
        if x not in self:
          for n in self.vertices:
            list1.add(n)
        yield " ".join(visited)
        raise NotImplementedError
        
    def breadth_first_search(self, start=None):
      visited = []
      q = collections.deque()
      visited[start] = True
      q.append(start)
      while q:
        start = q.popleft()
        print(start, "start")
      for x in self.vertices:
        if not visited[x]:
          visited[x] = True
          yield q.append(x)
      raise NotImplementedError
class EdgelistGraph(Graph):
    """An edge list representation of a Graph.
    A ListGraph has one private instance variable, _edgelist.
    """
    def __init__(self, edgelist=None):
        """Returns an EdgelistGraph generated from edgelist."""
        self._edgelist = edgelist or []
    def __repr__(self):
        return repr(self._edgelist)
    @property
    def vertices(self) -> set:
        self.verticesSet = set()
        for i in self._edgelist:
          for j in i:
            self.verticesSet.add(j)
        return self.verticesSet
        raise NotImplementedError
    @property
    def edges(self) -> set:
        self.edgesSet = set()
        for i in self._edgelist:
            self.edgesSet.add(i)
        return self.edgesSet
        raise NotImplementedError
    def degree(self, vertex) -> int:
        count = 0
        for i in self._edgelist:
          for j in i:
            if j == vertex:
              count += 1
        return count
        raise NotImplementedError
    def adjacent_to(self, vertex) -> set:
        adjSet = set()
        for i in self._edgelist:
          if vertex in i:
            for j in i:
              if j != vertex:
                adjSet.add(j)  
        return adjSet
        raise NotImplementedError
    def add_vertex(self, vertex):
        self._edgelist.append((vertex,None))
        self.verticesSet.add(vertex)
        self.edgesSet.add((vertex,None))
        return self.verticesSet
        raise NotImplementedError
    def add_edge(self, edge): 
        self._edgelist.append(edge)
        self.edgesSet.add(edge)
        return self.edgesSet
        raise NotImplementedError
    def remove_vertex(self, vertex):
        self.verticesSet.remove(vertex)
        for i in self._edgelist:
          for j in i:
            if j == vertex:
              self._edgelist.remove(i)
        self.edgesSet.clear()
        for i in self._edgelist:
            self.edgesSet.add(i)
        return self.verticesSet
        raise NotImplementedError
    def remove_edge(self, edge):
        self.edgesSet.remove(edge)
        self._edgelist.remove(edge)   
        return self.edgesSet
        raise NotImplementedError
class MatrixGraph(Graph):
    """An adjacency-matrix representation of a Graph.
    A MatrixGraph has one private instance variable, _matrix.
    """

    def __init__(self, matrix=None):
        """Produces a MatrixGraph generated from matrix."""
        self._matrix = matrix or []
    def __repr__(self):
        return repr(self._matrix)
    @property
    def vertices(self) -> set:
      self.verticesSet = set()
      for i in self._matrix:
        k = tuple(i)
        self.verticesSet.add(k)
      return self.verticesSet
      raise NotImplementedError
    @property
    def edges(self) -> set:
        self.edgesSet = set()
        count = 1
        for i in self._matrix:
          self.edgesSet.add(count)
          count += 1
        raise NotImplementedError
    def degree(self, vertex) -> int:
        count = 0
        for i in vertex:
          if i == True:
            count += 1
        return count
        raise NotImplementedError
    def adjacent_to(self, vertex) -> set:
        count = 0
        adjSet = set()
        for i in vertex:
          if i == True:
            x = tuple(self._matrix[count])
            adjSet.add(x)
          count +=1
        return adjSet
        raise NotImplementedError
    def add_vertex(self, vertex):
        self._matrix.append(vertex)
        self.verticesSet.add(tuple(vertex))
        return self.verticesSet
        raise NotImplementedError
    def add_edge(self, edge):
        self.edgesSet.add(edge)
        return(self.edgesSet)
        raise NotImplementedError
    def remove_vertex(self, vertex):
        self._matrix.remove(vertex)
        self.verticesSet.remove(tuple(vertex))
        return self.verticesSet
        raise NotImplementedError
    def remove_edge(self, edge):
        self.edgesSet.remove(edge)
        return self.edgesSet
        raise NotImplementedError
  
class DictGraph(Graph):
    """An adjacency-list representation of a Graph.
    A DictGraph has one private instance variable, _dict.
    """
    def __init__(self, dictionary=None):
        """Produces a DictGraph generated from dictionary."""
        self._dict = dictionary or {}
    def __repr__(self):
        return repr(self._dict)
    @property
    def vertices(self) -> set:
      self.verticesSet = set(self._dict.keys())
      return self.verticesSet
      raise NotImplementedError
    @property
    def edges(self) -> set:
      edge = ()
      myList = []
      edgeSet = set()
      for vertice in self.verticesSet:
        myList = self._dict.get(vertice)
        for i in myList:
          edge = (vertice, i)
          edgeSet.add(edge)
      self.edgeSet = edgeSet
      return self.edgeSet
      raise NotImplementedError

    def degree(self, vertex) -> int:
      degreeVal = len(self._dict.get(vertex))
      return degreeVal
      raise NotImplementedError
      
    def adjacent_to(self, vertex) -> set:
      adjSet = set()
      for i in self._dict[vertex]:
        adjSet.add(i)
      return adjSet;
      raise NotImplementedError

    def add_vertex(self, vertex):
      if vertex not in self.verticesSet:
        self._dict.update({vertex: None})
        self.verticesSet.add(vertex)
        return self.verticesSet
        raise NotImplementedError
        
    def add_edge(self, edge):
        self.edgeSet.add(edge)
        return self.edgeSet
        raise NotImplementedError
      
    def remove_vertex(self, vertex):
        self._dict.pop(vertex)
        self.verticesSet.remove(vertex)
        return self.verticesSet
        raise NotImplementedError
      
    def remove_edge(self, edge):
        self.edgeSet.remove(edge)
        return self.edgeSet
        raise NotImplementedError