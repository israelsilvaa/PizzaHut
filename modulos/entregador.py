from modulos.grafo import Grafo
from modulos.grid import Grid
class Entregador:

    def __init__(self, grafo: Grafo, grid: Grid):
        self.teste = "testando"
        self.grafo = grafo
        self.grid = grid
        self.custo_pi = []
        self.melhorCaminhoDFS = []
        self.parametro = 0

        #pegar o endereço da pizzaria para inciar o DFS
        self.vertice_inicial_entrega = 0

    
    def melhorCaminho(self):
        self.criaTabelaDFS()
        self.printTabelaDFS()
        self.dfs()

        print("\nmelhor caminho de ", self.grid.enderecoPizzaHut, " -> ", self.grid.listaDePedidos[0])
        
        print(self.melhorCaminhoDFS)

        self.printTabelaDFS()

    def criaTabelaDFS(self):
        for i in range(self.grafo.numeroVertices):
            linha = []
            for x in range(2):
                linha.append("null")
            self.custo_pi.append(linha)
        print("variavel teste: ", self.grafo.arestas[0][1][0])

    def printTabelaDFS(self):
        print("\nDFS-------- -  CUSTO  -  PI ")
        for i in range(self.grafo.numeroVertices):
            print("Vertice", i, ":    ", end="")
            for x in range(2):
                print(str(self.custo_pi[i][x]) , "    ", end="")
            print("")

    def dfs(self):        
        vertice_inicial = self.grid.enderecoPizzaHut
        vertice_final = self.grafo.numeroVertices

        self.dfs_visit(vertice_inicial, vertice_final)

        if vertice_inicial > 0:
            vertice_inicial = 0
            vertice_final = self.grid.enderecoPizzaHut
            self.dfs_visit(vertice_inicial, vertice_final)


    def dfs_visit(self, vertice_inicial, vertice_final):
        for saidaVerticeX_linha in range(vertice_inicial ,vertice_final):
            for destinoVerticeX_coluna in range(vertice_final):

                if saidaVerticeX_linha == self.grid.enderecoPizzaHut:
                    self.custo_pi[vertice_inicial][0] = 0

                # se a aresta existir(peso > 0)
                elif self.grafo.arestas[saidaVerticeX_linha][destinoVerticeX_coluna][self.parametro] > 0:

                    # se o custo for menor que o infinito
                    custoDaAresta = self.grafo.arestas[saidaVerticeX_linha][destinoVerticeX_coluna][self.parametro] 
                
                    if self.custo_pi[destinoVerticeX_coluna][0] == "null":
                        self.custo_pi[destinoVerticeX_coluna][0] = custoDaAresta
                        self.custo_pi[destinoVerticeX_coluna][1] = saidaVerticeX_linha
                    
                    elif(custoDaAresta + self.custo_pi[destinoVerticeX_coluna][0] < self.custo_pi[destinoVerticeX_coluna][0]):
                        self.custo_pi[destinoVerticeX_coluna][0] = custoDaAresta + self.custo_pi[destinoVerticeX_coluna][0]    
                        self.custo_pi[destinoVerticeX_coluna][1] = saidaVerticeX_linha
        

        





    