import random
from enums.icone import Icone
from modulos.grafo import Grafo

class Grid:
    def __init__(self, grafo: Grafo, tamanhoGrid: int):
        self.grid = []
        self.grafo = grafo
        self.tamanhoGrid: int = tamanhoGrid
        random.seed(32)
        self.enderecoPizzaHut = random.randint(1, self.grafo.numeroVertices - 1)
        self.entregador = self.enderecoPizzaHut
        self.tipoAresta = 3
        self.quantEntregas = 2
        self.listaDePedidos = []

    def gerarGrid(self):

        # gerando pedidos aleatorios( != da pizzaria)
        
        # endereço de entregaga aleatorio e 0 == não entregue
        endereco = [random.randint(0, self.grafo.numeroVertices - 1), 0]
        for i in range(self.quantEntregas):
            while True:
                endereco = random.randint(0, self.grafo.numeroVertices - 1)
                if endereco in self.listaDePedidos or endereco == self.enderecoPizzaHut:
                    endereco = random.randint(0, self.grafo.numeroVertices - 1)
                else:
                    self.listaDePedidos.append(endereco)
                    break

        # Criando matriz do GRID e setando endereços de clientes
        c = 0
        for linha in range(0, self.tamanhoGrid):
            valoresLinha = []
            for coluna in range(0, self.tamanhoGrid):

            
                if c in self.listaDePedidos:
                    vertice_icone = [c, 3]  # mudar pra 3(icone cliente)
                else:
                    vertice_icone = [c, 0]
                        
                valoresLinha.append(vertice_icone)
                c += 1
            self.grid.append(valoresLinha)

        # setando endereço PIZZA HUT
        for linha in range(self.tamanhoGrid):
            for coluna in range(self.tamanhoGrid):
                if self.grid[linha][coluna][0] == self.enderecoPizzaHut:
                    self.grid[linha][coluna][1] = 5

    def mostrarGrid(self):
      
        if self.tipoAresta == 3:
            ajusteEspacoHorizontal = "   "
        else:
            ajusteEspacoHorizontal = "     "

        print("\nGrid: ", self.tamanhoGrid,"x", self.tamanhoGrid)
        for linha in range(0, self.tamanhoGrid):
            for coluna in range(0, self.tamanhoGrid):

                if 0 == self.grid[linha][coluna][1]:
                    if self.grafo.numeroVertices > 99 and self.grid[linha][coluna][0] < 10:
                        print(
                            "00" + f"{self.grid[linha][coluna][0]} ", ajusteEspacoHorizontal, end="")
                        self._printarArestaHorizontal(linha, coluna)
                    elif self.grafo.numeroVertices > 9 and self.grid[linha][coluna][0] < 10:
                        print(
                            Icone.COR_VERMELHO.value + "0" +
                            f"{self.grid[linha][coluna][0]}" + Icone.FIM_COR.value,
                            ajusteEspacoHorizontal, end="")
                        
                        self._printarArestaHorizontal(linha, coluna)
                    elif self.grafo.numeroVertices > 99 and self.grid[linha][coluna][0] < 100:
                        print("0" + f"{self.grid[linha][coluna][0]} ",
                            ajusteEspacoHorizontal, end="")
                        self._printarArestaHorizontal(linha, coluna)
                    else:
                        print(Icone.COR_VERMELHO.value + f"{self.grid[linha][coluna][0]}"+
                              Icone.FIM_COR.value, ajusteEspacoHorizontal, end="")
                        self._printarArestaHorizontal(linha, coluna)

                elif 1 == self.grid[linha][coluna][1]:
                    print(Icone.PIZZARIA.value,
                    ajusteEspacoHorizontal, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 2 == self.grid[linha][coluna][1]:
                    print(Icone.ENTREGADOR.value, ajusteEspacoHorizontal, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 3 == self.grid[linha][coluna][1]:
                    print(Icone.CLIENTE.value,
                          ajusteEspacoHorizontal, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 4 == self.grid[linha][coluna][1]:
                    print(Icone.CHECK.value,
                          ajusteEspacoHorizontal, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 5 == self.grid[linha][coluna][1]:
                    print(Icone.PIZZARIA.value, Icone.ENTREGADOR.value,
                          ajusteEspacoHorizontal, end="")
                    self._printarArestaHorizontal(linha, coluna)
            
                    """
                    0 == imprimir vertice normalmente
                    1 ==  icone da pizzaria
                    2 ==  Entregador
                    3 == cliente
                    4 == check -> V (entrega feita)
                    """
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
                    print(self.grafo.arestas[L_aresta][C_aresta]
                          [self.tipoAresta], ajusteEspaco, end="")
                elif self.tipoAresta == 1:
                    print(self.grafo.arestas[L_aresta][C_aresta]
                          [self.tipoAresta], ajusteEspaco, end="")
                elif self.tipoAresta == 2:
                    print(self.grafo.arestas[L_aresta][C_aresta]
                          [self.tipoAresta], ajusteEspaco, end="")
                else:
                    print(str(self.grafo.arestas[L_aresta][C_aresta][self.tipoAresta - 3]) + "," + str(
                        self.grafo.arestas[L_aresta][C_aresta][self.tipoAresta - 2]), ajusteEspacoHorizontal2,
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
                print("--", self.grafo.arestas[L_aresta][C_aresta]
                        [self.tipoAresta], "--", ajusteEspacoHorizontal, end="")
            elif self.tipoAresta == 1:
                print("--", self.grafo.arestas[L_aresta][C_aresta]
                        [self.tipoAresta], "--", ajusteEspacoHorizontal, end="")
            elif self.tipoAresta == 2:
                print("--", self.grafo.arestas[L_aresta][C_aresta]
                        [self.tipoAresta], "--", ajusteEspacoHorizontal, end="")
            else:
                print("--", str(self.grafo.arestas[L_aresta][C_aresta][self.tipoAresta - 3]) + "," + str(
                    self.grafo.arestas[L_aresta][C_aresta][self.tipoAresta - 2]), "--", ajusteEspacoHorizontal,
                    end="")
                
    