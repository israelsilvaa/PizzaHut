import random


class Pizza:

    def __init__(self, tamanhoDoGrid):
        self.numeroVertices = tamanhoDoGrid * tamanhoDoGrid
        self.grid = []
        self.arestas = [[[0, 0, 0] for i in range(self.numeroVertices)]
                        for j in range(self.numeroVertices)]
        self.tamanhoGrid = tamanhoDoGrid
        self.pizza = "\U0001F355"
        self.enderecoPizzaria = "\U0001F3ED"
        self.enderecoCliente = "\U0001F9D1"

    def gerarGrid(self):
        c = 1
        for linha in range(0, self.tamanhoGrid):
            valoresLinha = []
            for coluna in range(0, self.tamanhoGrid):
                valoresLinha.append(c)
                c += 1

            self.grid.append(valoresLinha)

    def adicionarAresta(self, vertice1, vertice2, distancia, tempo):
        self.arestas[vertice1 - 1][vertice2 - 1] = [distancia, tempo, round(tempo/distancia)]
        self.arestas[vertice2 - 1][vertice1 - 1] = [distancia, tempo,  round(tempo/distancia)]


    def mostrarGrid(self):

        enderecoPizzaHut = random.randint(1, self.numeroVertices - 1)

        print("EPIZZAHUT END: ", enderecoPizzaHut)
        print("Grid: ")
        for linha in range(0, self.tamanhoGrid):

            for coluna in range(0, self.tamanhoGrid):
                if enderecoPizzaHut == self.grid[linha][coluna]:
                    print(self.enderecoPizzaria, end="    ")
                elif self.numeroVertices > 99 and self.grid[linha][coluna] < 10:
                    print("00"+f"{self.grid[linha][coluna]} ", end="    ")
                elif self.numeroVertices > 9 and self.grid[linha][coluna] < 10:
                    print("0"+f"{self.grid[linha][coluna]} ", end="    ")
                elif self.numeroVertices > 99 and self.grid[linha][coluna] < 100:
                    print("0"+f"{self.grid[linha][coluna]} ", end="    ")
                else:
                    print(f"{ self.grid[linha][coluna]} ", end="    ")
            print("\n\n")

    def gerarArestasGrid(self):
        for linha in range(0, self.tamanhoGrid - 1):
            for coluna in range(0, self.tamanhoGrid - 1):
                self.adicionarAresta(self.grid[linha][coluna],
                                     self.grid[linha + 1][coluna],
                                     random.randint(1, 4), random.randint(5, 9))
                self.adicionarAresta(self.grid[linha][coluna],
                                     self.grid[linha][coluna + 1],
                                     random.randint(1, 4), random.randint(5, 9))
        
        for vertice in range(0, self.tamanhoGrid - 1):
            self.adicionarAresta(self.grid[-1][vertice],
                                 self.grid[-1][vertice + 1],
                                 random.randint(1, 4), random.randint(5, 9))
            self.adicionarAresta(self.grid[vertice][-1],
                                 self.grid[vertice + 1][-1],
                                 random.randint(1, 4), random.randint(5, 9))

    def getMatrizAdjacencias(self):
        print('\n                Aresta(Peso, Tempo)')
        for linha in range(1, self.numeroVertices + 1):
            print("---", linha, end="---")
        print("")

        for linha in range(0, self.numeroVertices):
            for coluna in range(0, self.numeroVertices):
                if (coluna == 0):
                    if linha < 9:
                        print("0"+ str(linha+1), end="_")
                    else:
                        print(linha + 1, end="_")
                print(f"{self.arestas[linha][coluna]}  ", end="")
            print()


