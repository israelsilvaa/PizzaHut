from modulos.grafo import Grafo
from modulos.tela import Tela
from enums.icone import Icone
from modulos.grid import Grid
class Entregador:

    def __init__(self, grafo: Grafo, grid: Grid):
        self.teste = "testando"
        self.grafo = grafo
        self.grid = grid
        self.custo_pi_finali = []
        self.melhorCaminhoDFS = []
        self.parametro = 0
        self.listaEntrega_endStatus = []

    def iniciarEntregas(self):

        self.cloneListaDeEntregas()
        self.dfs(self.grid.enderecoPizzaHut)
        caminhoCusto = self.pegarMenorCaminhoDaTabela()

        print("lista de entregas : ",  self.listaEntrega_endStatus)
        print("EPIZZAHUT : ", self.grid.enderecoPizzaHut)
        print("\nDISTANCIA:")
        print("melhor caminho de ",Icone.COR_VERDE.value + str(self.grid.enderecoPizzaHut)+Icone.FIM_COR.value,
               "->"+Icone.COR_VERMELHO.value + str(caminhoCusto[0])+Icone.FIM_COR.value+"->",
                 Icone.COR_VERDE.value + str(self.pegarEnderecoMaisPerto())+Icone.FIM_COR.value)
        print("CUSTO TOTAL: ",Icone.COR_AMARELO.value +str(caminhoCusto[1])+Icone.FIM_COR.value)
 
        #self.moverEntregador(caminhoCusto[0])
        
    
    def moverEntregador(self, caminho):
        """
        0 == imprimir vertice normalmente
        1 ==  icone da pizzaria
        2 ==  Entregador
        3 == cliente
        4 == check -> V (entrega feita)
        5 == pizzaria e entregador
        """
        print("\ncaminho-----------", caminho)

    def cloneListaDeEntregas(self):
        for i in range(len(self.grid.listaDePedidos)):
            end_status = [self.grid.listaDePedidos[i], 0]
            self.listaEntrega_endStatus.append(end_status)

    def pegarEnderecoMaisPerto(self):

        for i in range(len(self.listaEntrega_endStatus)):
            if self.listaEntrega_endStatus[i][1] == 0:
                menorCustoEndere = [self.custo_pi_finali[self.listaEntrega_endStatus[i][0]][0], self.listaEntrega_endStatus[i][0]]
                break
    
        for i in range(len(self.listaEntrega_endStatus)):
            if self.listaEntrega_endStatus[i][1] == 0 and self.custo_pi_finali[self.listaEntrega_endStatus[i][0]][0] < menorCustoEndere[0]:
                menorCustoEndere = [self.custo_pi_finali[self.listaEntrega_endStatus[i][0]][0], self.listaEntrega_endStatus[i][0]]
                

                """
                essa linha marca um endereço como ENTREGUE, mas deve ser feito apos o entregador chegar lá
                self.listaEntrega_endStatus[i][1] = 1
                
                """

        return menorCustoEndere[1]
            

    def pegarMenorCaminhoDaTabela(self):

        proximo = self.pegarEnderecoMaisPerto()

        self.melhorCaminhoDFS.append(proximo)
        custoTotalDoCaminho = self.custo_pi_finali[proximo][0]
        while self.custo_pi_finali[proximo][1] != "null":
            self.melhorCaminhoDFS.append(self.custo_pi_finali[proximo][1])
            proximo = self.custo_pi_finali[proximo][1]
        
        self.melhorCaminhoDFS.reverse()
        caminho_custo = [self.melhorCaminhoDFS, custoTotalDoCaminho]
        return caminho_custo

    def criaTabelaDFS(self):
        
        self.custo_pi_finali = []
        for i in range(self.grafo.numeroVertices):
            linha = []
            for x in range(2):
                linha.append("null")
            linha.append(0)
            self.custo_pi_finali.append(linha)

    def printTabelaDFS(self):

        print("\nDFS-------- -  CUSTO  -  PI  -  Finali. ")
        for i in range(self.grafo.numeroVertices):
            if i in self.grid.listaDePedidos:
                print(Icone.COR_VERMELHO.value+"Vertice"+Icone.FIM_COR.value, i, ":    ", end="")
            else:
                print("Vertice", i, ":    ", end="")
            for x in range(3):
                if i == self.pegarEnderecoMaisPerto():
                    print(Icone.COR_VERDE.value+str(self.custo_pi_finali[i][x])+Icone.FIM_COR.value , "       ", end="")
                else:
                    print(str(self.custo_pi_finali[i][x]) , "       ", end="")
            print("")

    def dfs(self, vertReferencia):      
        self.melhorCaminhoDFS = []
        self.criaTabelaDFS()

        for i in range(self.grafo.numeroVertices):

            if i > 0:
                vertReferencia = self.buscarMenor(self.custo_pi_finali)
            
            for destino in range(self.grafo.numeroVertices):    

                # primeira rodada onde o vertReferencia é o ponto de partida(custo é 0 e anterior é Null)
                if i == 0 and destino == vertReferencia:
                        self.custo_pi_finali[destino][0] = 0

                # SE (aresta de referencia p/ Destino for valida) E (destino ainda não visitado)
                elif self.grafo.arestas[vertReferencia][destino][self.parametro] > 0 and self.custo_pi_finali[destino][2] == 0:

                    # se o custo para um vertice for INfinito então coloca o primeiro valor que encontrar
                    if self.custo_pi_finali[destino][0] == "null":

                        # tratamanto para primeira rodada quando, EVITA soma da proxima aresta com custo atual
                        # quando custo atual vale string NULL (da erro se somar INT + STR) 
                        if i == 0:
                            self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][self.parametro]
                            self.custo_pi_finali[destino][1] = vertReferencia
                        else:
                            #                                               (INTEIRO)                                      +    (INTEIRO)-> na primeira rodada isso pode ser uma string "null"
                            self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][self.parametro] + self.custo_pi_finali[vertReferencia][0]
                            self.custo_pi_finali[destino][1] = vertReferencia

                    else:
                        #SE o vertice de destino ja tiver um valor, nos somamos a aresta q vai pra ele mais o custo do Vertice que o descubriu
                        # se for menor então temos um caminho melhor e subistituimos.
                        if self.grafo.arestas[vertReferencia][destino][self.parametro] + self.custo_pi_finali[vertReferencia][0] < self.custo_pi_finali[destino][0]:
                            self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][self.parametro] + self.custo_pi_finali[vertReferencia][0]
                            self.custo_pi_finali[destino][1] = vertReferencia
            
            self.custo_pi_finali[vertReferencia][2] = 1 # finaliza a referencia

                
    def buscarMenor(self, lista):
        # csuto e seu indice
        menor = [None ,None]
        primeiroValorMenor = 0

        # pega o menor valor da lista(valores com custo != INFINITO(null))
        for i in range(len(lista)):
            if lista[i][0] != "null" and lista[i][2] != 1 and primeiroValorMenor == 0:
                menor[0] = lista[i][0]
                menor[1] = i
                primeiroValorMenor = 1
                
        # dentre os valores menores que INFINITO(null) e não visitados, retorna o menor deles e seu Vertice
        for i in range(len(lista)):
            if lista[i][0] != "null" and lista[i][2] != 1:
                if lista[i][0] < menor[0]:
                    menor[0] = lista[i][0]
                    menor[1] = i
        return menor[1]
        
   