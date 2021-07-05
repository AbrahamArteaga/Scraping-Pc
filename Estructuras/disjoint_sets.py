class DisjoinSet:

    def __init__(self):
        self.parent = []
        self.rank = []

    def make_set(self, i):
        if len(self.parent) - 1 < i:
            for k in range(len(self.parent), i+1):
                self.parent.append(k)
                self.rank.append(0)

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
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


conjunto = DisjoinSet()
conjunto.make_set(1)
conjunto.make_set(2)
conjunto.make_set(6)
conjunto.union(2, 4)
conjunto.union(5, 2)
conjunto.union(3, 1)
conjunto.union(2, 3)
print()
