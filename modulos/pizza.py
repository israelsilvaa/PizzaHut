import random

class Pizza:

    def __init__(self, tamanhoDoGrid):
        self.numeroVertices = tamanhoDoGrid * tamanhoDoGrid
        self.grid = []
        self.arestas = [[[0, 0, 0] for i in range(self.numeroVertices)]
                        for j in range(self.numeroVertices)]
        self.tamanhoGrid = tamanhoDoGrid
        self.tipoAresta = 3
        if self.tipoAresta == 3:
            self.ajusteEspaco = "              "
            self.ajusteEspacoHorizontal = "  "
            self.ajusteEspacoHorizontal2 = "              "
            self.ajusteEspacoHorizontal3 = "                "
        else:
            self.ajusteEspaco = "                    "
            self.ajusteEspacoHorizontal = "     "
            self.ajusteEspacoHorizontal2 = "                    "

        self.pizza = "\U0001F355"
        self.enderecoPizzaria = "\U0001F3ED"
        self.enderecoCliente = "\U0001F9D1"
        self.entregue = "\U00002705"
        self.inicioCor = "\033[0;31;40m "
        self.fimCor = "\033[m"


    def gerarGrid(self):
        enderecoPizzaHut = random.randint(1, self.numeroVertices - 1)
        entregador = enderecoPizzaHut

        # gerando pedidos aleatorios( != da pizzaria)
        listaDePedidos = []
        endereco = random.randint(1, self.numeroVertices - 1)
        for i in range(3):
            while True:
                endereco = random.randint(1, self.numeroVertices - 1)
                if endereco in listaDePedidos or endereco == enderecoPizzaHut:
                    endereco = random.randint(1, self.numeroVertices - 1)
                else:
                    listaDePedidos.append(endereco)
                    break

        print('\033[0;30;41mQuant Vertices\033[m', self.numeroVertices)
        print("EPIZZAHUT : ", enderecoPizzaHut)
        print("entregador : ", enderecoPizzaHut)
        print("cliente : ", listaDePedidos)
        
        # Criando matriz do GRID e setando endereços de clientes
        c = 1
        for linha in range(0, self.tamanhoGrid):
            valoresLinha = []
            for coluna in range(0, self.tamanhoGrid):
                if c in listaDePedidos:
                    vertice_icone = [c, 3] #mudar pra 3
                else:
                    vertice_icone = [c, 0]
                valoresLinha.append(vertice_icone)
                c += 1
            self.grid.append(valoresLinha)

        # setando endereço PIZZA HUT
        for linha in range(self.tamanhoGrid):
            for coluna in range(self.tamanhoGrid):
                if self.grid[linha][coluna][0] == enderecoPizzaHut:
                    self.grid[linha][coluna][1] = 5 #mudar pra 1

    def adicionarAresta(self, vertice1, vertice2, distancia, tempo):
        self.arestas[vertice1 - 1][vertice2 - 1] = [distancia, tempo, round(tempo/distancia)]
        self.arestas[vertice2 - 1][vertice1 - 1] = [distancia, tempo,  round(tempo/distancia)]

    def mostrarGrid(self):
        """
        0 == imprimir vertice normalmente
        1 ==  icone da pizzaria
        2 ==  pizza
        3 == endereço de entrega
        4 == check -> V (entrega feita)
        5 == pizzaria e entregador
        """
        print("Grid: ")
        for linha in range(0, self.tamanhoGrid):
            for coluna in range(0, self.tamanhoGrid):

                if 0 == self.grid[linha][coluna][1]:
                    if self.numeroVertices > 99 and self.grid[linha][coluna][0] < 10:
                        print("00"+f"{self.grid[linha][coluna][0]} ", self.ajusteEspacoHorizontal, end="")
                        self.printarArestaHorizontal(linha, coluna)
                    elif self.numeroVertices > 9 and self.grid[linha][coluna][0] < 10:
                        print(self.inicioCor+"0"+f"{self.grid[linha][coluna][0]}"+self.fimCor, self.ajusteEspacoHorizontal, end="")
                        # print("X", self.ajusteEspacoHorizontal, end="")
                        self.printarArestaHorizontal(linha, coluna)
                    elif self.numeroVertices > 99 and self.grid[linha][coluna][0] < 100:
                        print("0"+f"{self.grid[linha][coluna][0]} ", self.ajusteEspacoHorizontal, end="")
                        # print("X", self.ajusteEspacoHorizontal, end="")
                        self.printarArestaHorizontal(linha, coluna)
                    else:
                        print(self.inicioCor+f"{self.grid[linha][coluna][0]}"+self.fimCor, self.ajusteEspacoHorizontal, end="")
                        #print(self.inicioCor+"X"+self.fimCor, self.ajusteEspacoHorizontal, end="")
                        self.printarArestaHorizontal(linha, coluna)

                elif 1 == self.grid[linha][coluna][1]:
                    print(self.enderecoPizzaria, self.ajusteEspacoHorizontal, end="")
                    self.printarArestaHorizontal(linha, coluna)
                elif 2 == self.grid[linha][coluna][1]:
                    print(self.pizza, self.ajusteEspacoHorizontal, end="")
                    self.printarArestaHorizontal(linha, coluna)
                elif 3 == self.grid[linha][coluna][1]:
                    print(self.enderecoCliente, self.ajusteEspacoHorizontal, end="")
                    self.printarArestaHorizontal(linha, coluna)
                elif 4 == self.grid[linha][coluna][1]:
                    print(self.entregue, self.ajusteEspacoHorizontal,end="")
                    self.printarArestaHorizontal(linha, coluna)
                elif 5 == self.grid[linha][coluna][1]:
                    print(self.enderecoPizzaria, self.pizza, self.ajusteEspacoHorizontal, end="")
                    self.printarArestaHorizontal(linha, coluna)
            print("\n")

            self.printarArestaVerticais(linha, coluna)
            
    def gerarArestasGrid(self):
        for linha in range(0, self.tamanhoGrid - 1):
            for coluna in range(0, self.tamanhoGrid - 1):

                self.adicionarAresta(self.grid[linha][coluna][0],self.grid[linha + 1][coluna][0],random.randint(1, 4), random.randint(5, 9))
                self.adicionarAresta(self.grid[linha][coluna][0],self.grid[linha][coluna + 1][0],random.randint(1, 4), random.randint(5, 9))
        
        for vertice in range(0, self.tamanhoGrid - 1):
            self.adicionarAresta(self.grid[-1][vertice][0],
                                 self.grid[-1][vertice + 1][0],
                                 random.randint(1, 4), random.randint(5, 9))
            self.adicionarAresta(self.grid[vertice][-1][0],
                                 self.grid[vertice + 1][-1][0],
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
        
    def printarArestaVerticais(self, linha, coluna):
        if self.grid[linha][coluna][0] + self.tamanhoGrid <= self.numeroVertices:
                for i in range(self.tamanhoGrid):
                    if self.tipoAresta == 3:
                        print("|" , self.ajusteEspacoHorizontal3, end="")
                    else:
                        print("|" , self.ajusteEspacoHorizontal2, end="")
                print("\n")
                for coluna in range(self.tamanhoGrid):
                    L_aresta = self.grid[linha][coluna][0]
                    C_aresta = self.grid[linha][coluna][0] + self.tamanhoGrid
                    if self.tipoAresta == 0:
                        print(self.arestas[L_aresta-1][C_aresta-1][self.tipoAresta], self.ajusteEspaco, end="")
                    elif self.tipoAresta == 1:
                        print(self.arestas[L_aresta-1][C_aresta-1][self.tipoAresta], self.ajusteEspaco, end="")
                    elif self.tipoAresta == 2:
                        print(self.arestas[L_aresta-1][C_aresta-1][self.tipoAresta], self.ajusteEspaco, end="")
                    else:
                        print(str(self.arestas[L_aresta-1][C_aresta-1][self.tipoAresta-3])+","+ str(self.arestas[L_aresta-1][C_aresta-1][self.tipoAresta-2]), self.ajusteEspacoHorizontal2, end="")
                print("\n")
                for i in range(self.tamanhoGrid):
                    if self.tipoAresta == 3:
                        print("|" , self.ajusteEspacoHorizontal3, end="")
                    else:
                        print("|" , self.ajusteEspacoHorizontal2, end="")
                print("\n")

    """
        0 == distancia
        1 == tempo
        2 == tempo/distancia
        3 == distantia E tempo    
    """
    def printarArestaHorizontal(self, linha, coluna):
        if coluna+1 <= self.tamanhoGrid - 1:
            L_aresta = self.grid[linha][coluna][0]
            C_aresta = self.grid[linha][coluna+1][0]
            
            if self.tipoAresta == 0:
                print("--", self.arestas[L_aresta-1][C_aresta-1][self.tipoAresta],"--", self.ajusteEspacoHorizontal, end="")
            elif self.tipoAresta == 1:
                print("--", self.arestas[L_aresta-1][C_aresta-1][self.tipoAresta],"--", self.ajusteEspacoHorizontal, end="")
            elif self.tipoAresta == 2:
                print("--", self.arestas[L_aresta-1][C_aresta-1][self.tipoAresta],"--", self.ajusteEspacoHorizontal, end="")
            else:
                print("--", str(self.arestas[L_aresta-1][C_aresta-1][self.tipoAresta-3])+","+str(self.arestas[L_aresta-1][C_aresta-1][self.tipoAresta-2]),"--", self.ajusteEspacoHorizontal, end="")



