
class Grafo:

    def __init__(self, tamanhoDoGrid):
        self.numeroVertices = tamanhoDoGrid * tamanhoDoGrid
        self.arestas = [[[0, 0, 0] for i in range(self.numeroVertices)]
                        for j in range(self.numeroVertices)]

    def adicionarAresta(self, vertice1, vertice2, distancia, tempo):
        self.arestas[vertice1 - 1][vertice2 -
                                   1] = [distancia, tempo, round(tempo / distancia)]
        self.arestas[vertice2 - 1][vertice1 -
                                   1] = [distancia, tempo, round(tempo / distancia)]

    def getMatrizAdjacencias(self):
        print('\n                Aresta(Peso, Tempo)')
        for linha in range(1, self.numeroVertices + 1):
            print("---", linha, end="---")
        print("")

        for linha in range(0, self.numeroVertices):
            for coluna in range(0, self.numeroVertices):
                if (coluna == 0):
                    if linha < 9:
                        print("0" + str(linha + 1), end="_")
                    else:
                        print(linha + 1, end="_")
                print(f"{self.arestas[linha][coluna]}  ", end="")
            print()