class DisjoinSet:

    """
    Nombre: Conjunto Disjunto
    Funciones: make_set,
    find,union
    """

    def __init__(self):
        self.parent = []
        self.rank = []

    def make_set(self, i):
        """
        Hace un conjunto
        con los valores
        que se ingrese.
        Argumentos: i
        """
        if len(self.parent) - 1 < i:
            for k in range(len(self.parent), i+1):
                self.parent.append(k)
                self.rank.append(0)

    def find(self, i):
        """
        Busca un elemento
        dentro de un conjunto.
        Argumentos: i
        """
        if i >= len(self.parent):
            return -1
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """
        Une a dos conjuntos
        Argumentos: i,j
        """
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1



