class GrafoRutas:
    def __init__(self, nodos):
        self.nodos = nodos
        self.adyacencia = {n: {} for n in nodos}
    
    def agregar_arista(self, origen, destino, peso):
        self.adyacencia[origen][destino] = peso
    
    def dijkstra(self, origen):
        distancias = {n: float('inf') for n in self.nodos}
        distancias[origen] = 0
        no_visitados = set(self.nodos)
        while no_visitados:
            actual = min(no_visitados, key=lambda n: distancias[n])
            no_visitados.remove(actual)
            for vecino, peso in self.adyacencia[actual].items():
                nueva_dist = distancias[actual] + peso
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
        return distancias
    
    def floyd_warshall(self):
        n = len(self.nodos)
        idx = {nodo: i for i, nodo in enumerate(self.nodos)}
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for origen in self.nodos:
            for destino, peso in self.adyacencia[origen].items():
                dist[idx[origen]][idx[destino]] = peso
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist