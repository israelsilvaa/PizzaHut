import random
import time
from enums.icone import Icone
from modulos.grafo import Grafo

class Grid:
    def __init__(self, grafo: Grafo, tamanhoGrid: int, tipoDeAresta=0, enderecoPizzaHut=None, quantEntregas=1, listaPedidos=[]):
        self.grid = []
        self.grafo = grafo
        
        self.tamanhoGrid: int = tamanhoGrid
        if enderecoPizzaHut == None:
            self.enderecoPizzaHut = random.randint(1, self.grafo.numeroVertices - 1)
        else:
            self.enderecoPizzaHut = enderecoPizzaHut

        self.entregador = self.enderecoPizzaHut
        
        if len(listaPedidos) == 0:
            self.listaDePedidos = []
            self.criarListapedidosAleatorios = True
        else:
            self.listaDePedidos = listaPedidos.copy()
            self.criarListapedidosAleatorios = False

        self.quantEntregas = quantEntregas
        self.tipoDeAresta = tipoDeAresta

    def gerarGrid(self):

        # gerando pedidos aleatorios( != da pizzaria)
        
        # endereço de entregaga aleatorio e 0 == não entregue
        if self.criarListapedidosAleatorios:
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
                    self.grid[linha][coluna][1] = 6

    def mostrarGrid(self):
        for linha in range(0, self.tamanhoGrid):
            for coluna in range(0, self.tamanhoGrid):

                if 0 == self.grid[linha][coluna][1]:
                    if self.grafo.numeroVertices > 99 and self.grid[linha][coluna][0] < 10:
                        print(
                            "00" + f"{self.grid[linha][coluna][0]} ", end="")
                        self._printarArestaHorizontal(linha, coluna)
                    elif self.grafo.numeroVertices > 9 and self.grid[linha][coluna][0] < 10:
                        print(
                            Icone.COR_VERMELHO.value + "0" +
                            f"{self.grid[linha][coluna][0]}" + Icone.FIM_COR.value, end="")
                        
                        self._printarArestaHorizontal(linha, coluna)
                    elif self.grafo.numeroVertices > 99 and self.grid[linha][coluna][0] < 100:
                        print("0" + f"{self.grid[linha][coluna][0]} ", end="")
                        self._printarArestaHorizontal(linha, coluna)
                    else:
                        print(Icone.COR_VERMELHO.value + f"{self.grid[linha][coluna][0]}"+
                              Icone.FIM_COR.value, end="")
                        self._printarArestaHorizontal(linha, coluna)

                elif 1 == self.grid[linha][coluna][1]:
                    print(Icone.PIZZARIA.value, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 2 == self.grid[linha][coluna][1]:
                    print(Icone.ENTREGADOR.value, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 3 == self.grid[linha][coluna][1]:
                    print(Icone.PIZZA.value, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 4 == self.grid[linha][coluna][1]:
                    print(Icone.CHECK.value, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 5 == self.grid[linha][coluna][1]:
                    print(Icone.CHECK.value,Icone.ENTREGADOR.value, end="")
                    self._printarArestaHorizontal(linha, coluna)
                elif 6 == self.grid[linha][coluna][1]:
                    print(Icone.PIZZARIA.value, Icone.ENTREGADOR.value, end="")
                    self._printarArestaHorizontal(linha, coluna)
                    """
                    0 == imprimir vertice normalmente
                    1 ==  icone da pizzaria
                    2 ==  Entregador
                    3 == cliente
                    4 == check -> V (entrega feita)
                    5 == check e entregador
                    6 == Pizzaria e entregador
                    """
            print("\n")
            self._printarArestaVerticais(linha, coluna)

    def gerarArestasGrid(self):
        for linha in range(0, self.tamanhoGrid - 1):
            for coluna in range(0, self.tamanhoGrid - 1):
                self.grafo.adicionarAresta(self.grid[linha][coluna][0], self.grid[linha + 1]
                                           [coluna][0], random.randint(1, 9), random.randint(1, 9))
                self.grafo.adicionarAresta(self.grid[linha][coluna][0], self.grid[linha]
                                           [coluna + 1][0], random.randint(1, 9), random.randint(1, 9))

        for vertice in range(0, self.tamanhoGrid - 1):
            self.grafo.adicionarAresta(self.grid[-1][vertice][0],
                                       self.grid[-1][vertice + 1][0],
                                       random.randint(1, 9), random.randint(1, 9))
            self.grafo.adicionarAresta(self.grid[vertice][-1][0],
                                       self.grid[vertice + 1][-1][0],
                                       random.randint(1, 9), random.randint(1, 9))

    def _printarArestaVerticais(self, linha, coluna):
        if self.tipoDeAresta == 2:
            ajusteEspacoHorizontal = "                      "    
            ajusteEspacoHorizontal2 = "                   "     
        else:
            ajusteEspacoHorizontal = "                    "    

        # verifica se vai se é a ultima linha do grid
        # se não for signica que todo o grid ja foi printado, e não executa
        if self.grid[linha][coluna][0] + self.tamanhoGrid <= self.grafo.numeroVertices:

            for i in range(self.tamanhoGrid):
                print("|", ajusteEspacoHorizontal, end="")
            print(end="\n")

            for coluna in range(self.tamanhoGrid):
                L_aresta = self.grid[linha][coluna][0]
                C_aresta = self.grid[linha][coluna][0] + self.tamanhoGrid
                if self.tipoDeAresta == 2:
                    print(self.grafo.arestas[L_aresta][C_aresta][self.tipoDeAresta], ajusteEspacoHorizontal2, end="")    
                else:
                    print(self.grafo.arestas[L_aresta][C_aresta][self.tipoDeAresta], ajusteEspacoHorizontal, end="")    
            print(end="\n")

            for i in range(self.tamanhoGrid):
                print("|", ajusteEspacoHorizontal, end="")
            print("\n")

    def _printarArestaHorizontal(self, linha, coluna):
        ajusteEspacoHorizontal = "     "

        if coluna + 1 <= self.tamanhoGrid - 1:
            L_aresta = self.grid[linha][coluna][0]
            C_aresta = self.grid[linha][coluna + 1][0]
            print(ajusteEspacoHorizontal,"--", str(self.grafo.arestas[L_aresta][C_aresta][self.tipoDeAresta])," --", ajusteEspacoHorizontal,end="")
                
    