import random


class Pizza:

    def __init__(self, tamanhoDoGrid):
        self.numeroVertices = tamanhoDoGrid * tamanhoDoGrid
        self.grid = []
        self.arestas = [[[0, 0] for i in range(self.numeroVertices)]
                        for j in range(self.numeroVertices)]
        self.tamanhoGrid = tamanhoDoGrid

    def gerarGrid(self):
        c = 1
        for linha in range(0, self.tamanhoGrid):
            valoresLinha = []
            for coluna in range(0, self.tamanhoGrid):

                valoresLinha.append(c)
                c += 1

            self.grid.append(valoresLinha)

    def adicionarAresta(self, linha, coluna, distancia, tempo):
        self.arestas[linha - 1][coluna - 1] = [distancia, tempo]
        self.arestas[coluna - 1][linha - 1] = [distancia, tempo]


    def mostrarGrid(self):

        print("Grid: ")
        for linha in range(0, self.tamanhoGrid):

            for coluna in range(0, self.tamanhoGrid):
                print(f"{ self.grid[linha][coluna]} ", end="")
            print()

    def gerarArestasGrid(self):
        for linha in range(0, self.tamanhoGrid - 1):
            for coluna in range(0, self.tamanhoGrid - 1):
                self.adicionarAresta(self.grid[linha][coluna],
                                     self.grid[linha + 1][coluna],
                                     random.randint(1, self.tamanhoGrid), random.randint(1, self.tamanhoGrid))
                self.adicionarAresta(self.grid[linha][coluna],
                                     self.grid[linha][coluna + 1],
                                     random.randint(1, self.tamanhoGrid), random.randint(1, self.tamanhoGrid))
        for vertice in range(0, self.tamanhoGrid - 1):
            self.adicionarAresta(self.grid[-1][vertice],
                                 self.grid[-1][vertice + 1],
                                 random.randint(1, self.tamanhoGrid), random.randint(1, self.tamanhoGrid))
            self.adicionarAresta(self.grid[vertice][-1],
                                 self.grid[vertice + 1][-1],
                                 random.randint(1, self.tamanhoGrid), random.randint(1, self.tamanhoGrid))

    def getMatrizAdjacencias(self):
        print('\n                Aresta(Peso, Tempo)')
        for linha in range(1, self.numeroVertices + 1):
            print("---", linha, end="---")
        print("")
        for linha in range(0, self.numeroVertices):
            for coluna in range(0, self.numeroVertices):
                if (coluna == 0):
                    print(linha + 1, end="_")
                print(f"{self.arestas[linha][coluna]}  ", end="")
            print()


