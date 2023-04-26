import random

from enums.icone import Icone
from modulos.grafo import Grafo


class Grid:
    def __init__(self, grafo: Grafo, tamanhoGrid: int):
        self.grid = []
        self.grafo = grafo
        self.tamanhoGrid: int = tamanhoGrid
        self.tipoAresta = 3
        self.quantEntregas = 2

    def gerarGrid(self):
        enderecoPizzaHut = random.randint(1, self.grafo.numeroVertices - 1)

        # gerando pedidos aleatorios( != da pizzaria)
        listaDePedidos = []
        endereco = random.randint(1, self.grafo.numeroVertices - 1)
        for i in range(self.quantEntregas):
            while True:
                endereco = random.randint(1, self.grafo.numeroVertices - 1)
                if endereco in listaDePedidos or endereco == enderecoPizzaHut:
                    endereco = random.randint(1, self.grafo.numeroVertices - 1)
                else:
                    listaDePedidos.append(endereco)
                    break

        print('\033[0;30;41mQuant Vertices\033[m', self.grafo.numeroVertices)
        print("EPIZZAHUT : ", enderecoPizzaHut)
        print("entregador : ", enderecoPizzaHut)
        print("cliente : ", listaDePedidos)

        # Criando matriz do GRID e setando endereços de clientes
        c = 1
        for linha in range(0, self.tamanhoGrid):
            valoresLinha = []
            for coluna in range(0, self.tamanhoGrid):
                if c in listaDePedidos:
                    vertice_icone = [c, 3]  # mudar pra 3
                else:
                    vertice_icone = [c, 0]
                valoresLinha.append(vertice_icone)
                c += 1
            self.grid.append(valoresLinha)

        # setando endereço PIZZA HUT
        for linha in range(self.tamanhoGrid):
            for coluna in range(self.tamanhoGrid):
                if self.grid[linha][coluna][0] == enderecoPizzaHut:
                    self.grid[linha][coluna][1] = 5

    def mostrarGrid(self):
        """
        0 == imprimir vertice normalmente
        1 ==  icone da pizzaria
        2 ==  pizza
        3 == endereço de entrega
        4 == check -> V (entrega feita)
        5 == pizzaria e entregador
        """
        if self.tipoAresta == 3:
            ajusteEspacoHorizontal = "  "
        else:
            ajusteEspacoHorizontal = "     "

        print("Grid: ")
        for linha in range(0, self.tamanhoGrid):
            for coluna in range(0, self.tamanhoGrid):

                if 0 == self.grid[linha][coluna][1]:
                    if self.grafo.numeroVertices > 99 and self.grid[linha][coluna][0] < 10:
                        print(
                            "00" + f"{self.grid[linha][coluna][0]} ", ajusteEspacoHorizontal, end="")
                        self._printarArestaHorizontal(linha, coluna)
                    elif self.grafo.numeroVertices > 9 and self.grid[linha][coluna][0] < 10:
                        print(
                            Icone.INICIO.value + "0" +
                            f"{self.grid[linha][coluna][0]}" + Icone.FIM.value,
                            ajusteEspacoHorizontal, end="")
                        
                        self._printarArestaHorizontal(linha, coluna)
                    elif self.grafo.numeroVertices > 99 and self.grid[linha][coluna][0] < 100:
                        print("0" + f"{self.grid[linha][coluna][0]} ",
                            ajusteEspacoHorizontal, end="")
                        self._printarArestaHorizontal(linha, coluna)
                    else:
                        print(Icone.INICIO.value + f"{self.grid[linha][coluna][0]}" +
                              Icone.FIM.value, ajusteEspacoHorizontal, end="")
                        self._printarArestaHorizontal(linha, coluna)

                elif 1 == self.grid[linha][coluna][1]:
                    print(Icone.PIZZARIA.value,
                    ajusteEspacoHorizontal, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 2 == self.grid[linha][coluna][1]:
                    print(Icone.PIZZA.value, ajusteEspacoHorizontal, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 3 == self.grid[linha][coluna][1]:
                    print(Icone.RESIDENCIA.value,
                          ajusteEspacoHorizontal, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 4 == self.grid[linha][coluna][1]:
                    print(Icone.ENTREGUE.value,
                          ajusteEspacoHorizontal, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 5 == self.grid[linha][coluna][1]:
                    print(Icone.PIZZARIA.value, Icone.PIZZA.value,
                          ajusteEspacoHorizontal, end="")
                    self._printarArestaHorizontal(linha, coluna)

            print("\n")
            self._printarArestaVerticais(linha, coluna)

    def gerarArestasGrid(self):
        for linha in range(0, self.tamanhoGrid - 1):
            for coluna in range(0, self.tamanhoGrid - 1):
                self.grafo.adicionarAresta(self.grid[linha][coluna][0], self.grid[linha + 1]
                                           [coluna][0], random.randint(1, 4), random.randint(5, 9))
                self.grafo.adicionarAresta(self.grid[linha][coluna][0], self.grid[linha]
                                           [coluna + 1][0], random.randint(1, 4), random.randint(5, 9))

        for vertice in range(0, self.tamanhoGrid - 1):
            self.grafo.adicionarAresta(self.grid[-1][vertice][0],
                                       self.grid[-1][vertice + 1][0],
                                       random.randint(1, 4), random.randint(5, 9))
            self.grafo.adicionarAresta(self.grid[vertice][-1][0],
                                       self.grid[vertice + 1][-1][0],
                                       random.randint(1, 4), random.randint(5, 9))

    def _printarArestaVerticais(self, linha, coluna):
        if self.tipoAresta == 3:
            ajusteEspaco = "              "
            ajusteEspacoHorizontal2 = "              "
            ajusteEspacoHorizontal3 = "                "
        else:
            ajusteEspaco = "                    "
            ajusteEspacoHorizontal2 = "                    "

        if self.grid[linha][coluna][0] + self.tamanhoGrid <= self.grafo.numeroVertices:
            for i in range(self.tamanhoGrid):
                if self.tipoAresta == 3:
                    print("|", ajusteEspacoHorizontal3, end="")
                else:
                    print("|", ajusteEspacoHorizontal2, end="")
            print("\n")
            for coluna in range(self.tamanhoGrid):
                L_aresta = self.grid[linha][coluna][0]
                C_aresta = self.grid[linha][coluna][0] + self.tamanhoGrid
                if self.tipoAresta == 0:
                    print(self.grafo.arestas[L_aresta - 1][C_aresta - 1]
                          [self.tipoAresta], ajusteEspaco, end="")
                elif self.tipoAresta == 1:
                    print(self.grafo.arestas[L_aresta - 1][C_aresta - 1]
                          [self.tipoAresta], ajusteEspaco, end="")
                elif self.tipoAresta == 2:
                    print(self.grafo.arestas[L_aresta - 1][C_aresta - 1]
                          [self.tipoAresta], ajusteEspaco, end="")
                else:
                    print(str(self.grafo.arestas[L_aresta - 1][C_aresta - 1][self.tipoAresta - 3]) + "," + str(
                        self.grafo.arestas[L_aresta - 1][C_aresta - 1][self.tipoAresta - 2]), ajusteEspacoHorizontal2,
                        end="")
            print("\n")
            for i in range(self.tamanhoGrid):
                if self.tipoAresta == 3:
                    print("|", ajusteEspacoHorizontal3, end="")
                else:
                    print("|", ajusteEspacoHorizontal2, end="")
            print("\n")

    def _printarArestaHorizontal(self, linha, coluna):
        if self.tipoAresta == 3:
            ajusteEspacoHorizontal = "  "
        else:
            ajusteEspacoHorizontal = "     "

        if coluna + 1 <= self.tamanhoGrid - 1:
            L_aresta = self.grid[linha][coluna][0]
            C_aresta = self.grid[linha][coluna + 1][0]

            if self.tipoAresta == 0:
                print("--", self.grafo.arestas[L_aresta - 1][C_aresta - 1]
                        [self.tipoAresta], "--", ajusteEspacoHorizontal, end="")
            elif self.tipoAresta == 1:
                print("--", self.grafo.arestas[L_aresta - 1][C_aresta - 1]
                        [self.tipoAresta], "--", ajusteEspacoHorizontal, end="")
            elif self.tipoAresta == 2:
                print("--", self.grafo.arestas[L_aresta - 1][C_aresta - 1]
                        [self.tipoAresta], "--", ajusteEspacoHorizontal, end="")
            else:
                print("--", str(self.grafo.arestas[L_aresta - 1][C_aresta - 1][self.tipoAresta - 3]) + "," + str(
                    self.grafo.arestas[L_aresta - 1][C_aresta - 1][self.tipoAresta - 2]), "--", ajusteEspacoHorizontal,
                    end="")
