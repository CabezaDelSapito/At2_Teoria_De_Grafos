class Grafo:
    def __init__(self, num_vertices, eh_direcionado):
        self.num_vertices = num_vertices
        self.tempo = 0
        self.lista_adj = [[] for _ in range(num_vertices)]
        self.pre = [0]*num_vertices
        self.pos = [0]*num_vertices
        self.eh_direcionado = eh_direcionado

    def adiciona_aresta(self, origem, destino):
        self.lista_adj[origem].append(destino)
        if not self.eh_direcionado:
            self.lista_adj[destino].append(origem)

    def dfs(self, vertice, visitado):
        visitado[vertice] = True
        self.tempo += 1
        self.pre[vertice] = self.tempo
        
        for vizinho in self.lista_adj[vertice]:
            if not visitado[vizinho]:
                self.dfs(vizinho, visitado)
        
        self.tempo += 1
        self.pos[vertice] = self.tempo
        
    def exibe(self):
        for i, adj in enumerate(self.lista_adj):
            print(f"{i}: {' -> '.join(map(str, adj))}")

    def exibe_pre_pos(self):
        print("\nTempo de visita da pré e pós-ordem:")
        for i in range(self.num_vertices):
            print(f"Vértice {i} ({self.pre[i]}/{self.pos[i]})")

# Teste
num_vertices = 4
eh_direcionado = False
grafo = Grafo(num_vertices, eh_direcionado)
grafo.adiciona_aresta(0, 1)
grafo.adiciona_aresta(0, 2)
grafo.adiciona_aresta(1, 3)
grafo.adiciona_aresta(2, 3)
visitado = [False]*grafo.num_vertices
print("Lista de adjacência do grafo:")
grafo.exibe()
print("\nBusca DFS no grafo:")
grafo.dfs(0, visitado)
grafo.exibe_pre_pos()