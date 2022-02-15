# Breadth-first search for finding shortest paths from a source in
# Graph or Digraph.
#
# Jesper Larsson, Malmö University, 2018-2020

import collections

class BFS:
    def __init__(self, G, s):
        self.__s = s
        self.__edge_to = [-1] * G.V
        self.__dist_to = [-1] * G.V

        q = collections.deque()
        q.append(s)
        self.__dist_to[s] = 0
        while q:                            # while q not empty
            v = q.popleft()
            for w in G.adj(v):
                if self.__dist_to[w] < 0:   # if w not visited
                    q.append(w)
                    self.__edge_to[w] = v
                    self.__dist_to[w] = self.__dist_to[v] + 1

    def has_path_to(self, v):
        return self.__dist_to[v] >= 0

    def dist_to(self, v):
        return self.__dist_to[v]

    def path_to(self, v):
        if self.__dist_to[v] < 0:
            return None
        p = [v]
        while v != self.__s:
            v = self.__edge_to[v]
            p.append(v)
        p.reverse()
        return p
