from modulos.grafo import Grafo
from modulos.grid import Grid
class Entregador:

    def __init__(self, grafo: Grafo, grid: Grid):
        self.teste = "testando"
        self.grafo = grafo
        self.grid = grid
        self.tempo = None
        self.inicio_fim_pi_cor = []
        self.melhorCaminhoDFS = []

        #pegar o endereço da pizzaria para inciar o DFS
        self.vertice_inicial_entrega = 0

    
    def melhorCaminho(self):
        self.criaTabelaDFS()

        self.printTabelaDFS()
        self.dfs()


        pi = self.inicio_fim_pi_cor[self.grid.listaDePedidos[0]][2]
        while pi != "null":
            self.melhorCaminhoDFS.append(pi)
            pi = self.inicio_fim_pi_cor[pi][2]
        
        print("\nmelhor caminho de ", self.grid.enderecoPizzaHut-1, " -> ", self.grid.listaDePedidos[0]-1)
        
        print(self.melhorCaminhoDFS)
        self.printTabelaDFS()

    def criaTabelaDFS(self):
        for i in range(self.grafo.numeroVertices):
            linha = []
            for x in range(4):
                linha.append("null")
            self.inicio_fim_pi_cor.append(linha)
        print("variavel teste: ", self.grafo.arestas[0][1][0])

    def printTabelaDFS(self):
        print("\nDFS-------- T_inicio  - T_fim  - PI   -  COR ")
        for i in range(self.grafo.numeroVertices):
            print("Vertice", i, ":    ", end="")
            for x in range(4):
                print(self.inicio_fim_pi_cor[i][x], "    ", end="")
            print("")

    def dfs(self):        
        self.tempo = 0
        vertice_inicial = self.grid.enderecoPizzaHut - 1
      
        # Seta todos os vertices para a cor branca
        for i in range(self.grafo.numeroVertices):
            self.inicio_fim_pi_cor[i][3] = 'branco'

        self.dfs_visit(vertice_inicial)

        # Verifica vertices do grafo a partir do vertice escoliho
        for i in range(self.grafo.numeroVertices):
            if (self.inicio_fim_pi_cor[vertice_inicial][3] == 'branco'):
                self.dfs_visit(vertice_inicial)

        

    def dfs_visit(self, vertice_inicial):
        self.tempo = self.tempo + 1

        self.inicio_fim_pi_cor[vertice_inicial][0] = self.tempo
        self.inicio_fim_pi_cor[vertice_inicial][3] = 'cinza'

        # Verifica os adjacentes a V
        for i in range(self.grafo.numeroVertices):
            # IF (a distancia da aresta for valida E o vertice ainda náo foi visitado)
            if (self.grafo.arestas[vertice_inicial][i][0] > 0 and self.inicio_fim_pi_cor[i][3] == 'branco'):
                # o vertice adjacente recebe como PI o vertice q achou ele.
                self.inicio_fim_pi_cor[i][2] = vertice_inicial
                self.dfs_visit(i)
        
        self.inicio_fim_pi_cor[vertice_inicial][3] = 'preto'
        self.tempo = self.tempo + 1
        self.inicio_fim_pi_cor[vertice_inicial][1] = self.tempo





    