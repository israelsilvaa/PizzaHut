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

    def criarArestas(self):

        self.tamanhoGrid = self.tamanhoGrid * self.tamanhoGrid

        for i in range(1, self.tamanhoGrid+1):
            # indice 0 é adicionado, mas não vamos usar
            linha = [['', '']]
            for x in range(1, self.tamanhoGrid+1):
                pesoTempo = [0, 0]
                if i != x and i != 1 and i + 1 >= x and i+x != 10:
                    pesoTempo[0] = random.randint(1, 4)
                    pesoTempo[1] = random.randint(5, 9)
                linha.append(pesoTempo)
            self.arestas.append(linha)

    def gridAtual(self):

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

    def listaArestas(self):

        print('\n                Aresta(Peso, Tempo)')
        for linha in range(1, self.numeroVertices + 1):
            print("---", linha, end="---")
        print("")

        for linha in range(1, self.numeroVertices + 1):
            for coluna in range(1, self.numeroVertices + 1):
                if (coluna == 1):
                    print(linha, end="_")
                print(self.arestas[linha - 1][coluna], ' ', end='')
            print('')
        print("\nCoordenada da aresta (Linha, coluna)\n")
        print("Exemplo: uma aresta ligando o Vertice 8 ao 9")
        print("teriamos um PESO e um TEMPO gravados nas coordenadas: Linha 8 e Coluna 9\n")
        print("Ou seja: (8,9)\n")
        print("\n")

        print("\n")
