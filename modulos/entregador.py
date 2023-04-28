from modulos.grafo import Grafo
from modulos.grid import Grid
class Entregador:

    def __init__(self, grafo: Grafo, grid: Grid):
        self.teste = "testando"
        self.grafo = grafo
        self.grid = grid
        self.custo_pi_finali = []
        self.melhorCaminhoDFS = []
        self.parametro = 0

        #pegar o endereço da pizzaria para inciar o DFS
        self.vertice_inicial_entrega = 0
    
    def melhorCaminho(self):
        self.criaTabelaDFS()
        self.dfs()

        proximo = self.grid.listaDePedidos[0]
        self.melhorCaminhoDFS.append(proximo)
        ct = 0
        while self.custo_pi_finali[proximo][1] != "null":
            self.melhorCaminhoDFS.append(self.custo_pi_finali[proximo][1])
            ct = ct + self.custo_pi_finali[proximo][0]
            proximo = self.custo_pi_finali[proximo][1]

        print("\nmelhor caminho de ", self.grid.enderecoPizzaHut, " -> ", self.grid.listaDePedidos[0] )
        self.melhorCaminhoDFS.reverse()
        print(self.melhorCaminhoDFS)
        print("CUSTO TOTAL: ",ct)
      

    def criaTabelaDFS(self):
        for i in range(self.grafo.numeroVertices):
            linha = []
            for x in range(2):
                linha.append("null")
            linha.append(0)
            self.custo_pi_finali.append(linha)

    def printTabelaDFS(self):
        print("\nDFS-------- -  CUSTO  -  PI  -  Finali. ")
        for i in range(self.grafo.numeroVertices):
            print("Vertice", i, ":    ", end="")
            for x in range(3):
                print(str(self.custo_pi_finali[i][x]) , "       ", end="")
            print("")

    def dfs(self):        

        vertReferencia = self.grid.enderecoPizzaHut
        for i in range(self.grafo.numeroVertices):
            if i > 0:
                vertReferencia = self.buscarMenor(self.custo_pi_finali)

            for destino in range(self.grafo.numeroVertices):    
                if i == 0 and destino == vertReferencia:
                        self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][0]
                elif self.grafo.arestas[vertReferencia][destino][0] > 0 and self.custo_pi_finali[destino][2] == 0:# aresta E nFinalizado

                    if self.custo_pi_finali[destino][0] == "null":
                        self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][0]
                        self.custo_pi_finali[destino][1] = vertReferencia
                    else:
                        if self.grafo.arestas[vertReferencia][destino][0] + self.custo_pi_finali[vertReferencia][0] < self.custo_pi_finali[destino][0]:
                            self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][0] + self.custo_pi_finali[vertReferencia][0]
                            self.custo_pi_finali[destino][1] = vertReferencia
            self.custo_pi_finali[vertReferencia][2] = 1 # finaliza a referencia
            
    def buscarMenor(self, lista):
        # csuto e seu indice
        menor = [None ,None]
        primeiroValorMenor = 0

        for i in range(len(lista)):
            if lista[i][0] != "null" and lista[i][2] != 1 and primeiroValorMenor == 0:
                menor[0] = lista[i][0]
                menor[1] = i
                primeiroValorMenor = 1
        
        for i in range(len(lista)):
            if lista[i][0] != "null" and lista[i][2] != 1:
                if lista[i][0] < menor[0]:
                    menor[0] = lista[i][0]
                    menor[1] = i

        return menor[1]
        

        





    