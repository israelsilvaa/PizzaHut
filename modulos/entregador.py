import time
from modulos.grafo import Grafo
from modulos.tela import Tela
from enums.icone import Icone
from modulos.grid import Grid
class Entregador:

    def __init__(self, grafo: Grafo, grid: Grid, tela:Tela):
        self.grafo = grafo
        self.grid = grid
        self.tela = tela
        self.custo_pi_finali = []
        self.melhorCaminhoDFS = []
        self.tipoCaminho = self.grid.tipoCaminho
        self.listaEntrega_endStatus = []
        self.custoTotalDaRota = 0

    def iniciarEntregas(self):

        self.cloneListaDeEntregas()
        self.dfs(self.grid.enderecoPizzaHut)
        caminhoCusto = self.pegarMenorCaminhoDaTabela()
        self.custoTotalDaRota = self.custoTotalDaRota + caminhoCusto[1]
        self.moverEntregador(caminhoCusto[0])
        
        while(self.pegarEnderecoMaisPerto() != None):
            self.dfs(self.grid.entregador)
            caminhoCusto = self.pegarMenorCaminhoDaTabela()
            self.custoTotalDaRota = self.custoTotalDaRota + caminhoCusto[1]
            self.moverEntregador(caminhoCusto[0])

        self.tela.limparTela()
        self.painel()
        self.grid.mostrarGrid()

    #Procura na lista de endereços do entregador e marca o Pedido X como entregue(0 -> 1)
    def finalizaEndereco(self, endereco):
        for i in range(len(self.listaEntrega_endStatus)):
            if endereco == self.listaEntrega_endStatus[i][0]:
                self.listaEntrega_endStatus[i][1] = 1

    #move o entregador ponto a ponto do caminho q for passado
    def moverEntregador(self, caminho):    
        """
        0 == imprimir vertice normalmente
        1 ==  icone da pizzaria
        2 ==  Entregador
        3 == cliente
        4 == check -> V (entrega feita)
        5 == check e entregador
        6 == Pizzaria e entregador
        """
        for i in range(len(caminho)):

            # primeiro apagamos o entregador da tela, e escrevemos o icone do vertice
            # se for Vertice == EndPizzaria, então escrevemos icone da pizzaria
            # se vertice estiver na lista de clientes(escrevemos icone de cliente)
            #       - Se for um cliente não atendido(escreve incone de cliente não atendido)
            #       - Se for um cliente atendido(escreve incone CHECK -> antrega feita!)
            # senão ele é apenas um vertive qualquer(sem icone, escerver numero do vertice) 
            for linha in range(0, self.grid.tamanhoGrid):
                for coluna in range(0, self.grid.tamanhoGrid):

                    vertice = self.grid.grid[linha][coluna][0]
                    icone = self.grid.grid[linha][coluna][1]

                    if vertice == self.grid.entregador:
                        
                        if vertice in self.grid.listaDePedidos:
                            # out icone check
                            if self.verificaStatusEntrega(vertice):
                                self.grid.grid[linha][coluna][1] = 4
                            else:
                                self.grid.grid[linha][coluna][1] = 3
                        elif vertice == self.grid.enderecoPizzaHut:
                            self.grid.grid[linha][coluna][1] = 1
                        else:
                            self.grid.grid[linha][coluna][1] = 0
            
            # depois de tirar o enretregador do mapa, temos que escrever ele no proximo vertice do caminho 
            for linha in range(0, self.grid.tamanhoGrid):
                for coluna in range(0, self.grid.tamanhoGrid):

                    vertice = self.grid.grid[linha][coluna][0]
                    if vertice == caminho[i] and vertice == self.grid.enderecoPizzaHut:
                        self.grid.grid[linha][coluna][1] = 6
                        self.grid.entregador = caminho[i]
                    elif vertice == caminho[i]:
                        self.grid.grid[linha][coluna][1] = 2
                        self.grid.entregador = caminho[i]

            # aqui atualizamos a tela(esperar > limpar > mostraPainel > mostraGrid)
            time.sleep(self.tela.velociadeAtualizacao)
            self.tela.limparTela()
            self.painel()
            self.grid.mostrarGrid()


            if caminho[-1] == self.grid.entregador:
                
                for linha in range(0, self.grid.tamanhoGrid):
                    for coluna in range(0, self.grid.tamanhoGrid):

                        vertice = self.grid.grid[linha][coluna][0]
                        if vertice == caminho[-1]:
                            self.grid.grid[linha][coluna][1] = 5
        
        #apos terminar a rota, o entrgador deve estar no endreço do cliente
        #então marcamos o endereço como Entregue/finalizado
        self.finalizaEndereco(self.pegarEnderecoMaisPerto()) 

    def painel(self):
        print("Lista de entregas[", self.grid.quantEntregas, "] :        ", end="")
        for i in range(len(self.listaEntrega_endStatus)):
            if self.listaEntrega_endStatus[i][1] == 1:
                print("("+str(self.listaEntrega_endStatus[i][0])+Icone.CHECK.value, end=")   ")
            else:
                print("("+str(self.listaEntrega_endStatus[i][0])+Icone.N_ENTREGUE.value, end=")   ")

        print("\nEPIZZAHUT : ", self.grid.enderecoPizzaHut)
        print("entregador : ", self.grid.entregador)
        if self.pegarEnderecoMaisPerto() != None:
            print("melhor caminho de             ", Icone.COR_VERDE.value + str(self.grid.entregador)+Icone.FIM_COR.value,"->   ", end="") 
            for i in range(len(self.melhorCaminhoDFS)):
                if self.melhorCaminhoDFS[i] == self.grid.entregador:
                    print(Icone.COR_AMARELO.value + str(self.melhorCaminhoDFS[i])+Icone.FIM_COR.value, end=" - ")
                else:
                    print(Icone.COR_VERMELHO.value + str(self.melhorCaminhoDFS[i])+Icone.FIM_COR.value, end=" - ")
    
            print("   ->",Icone.COR_VERDE.value + str(self.pegarEnderecoMaisPerto())+Icone.FIM_COR.value)
        print(end="")
        if self.tipoCaminho == 0:
            print("Tipo de Caminho:  Distância")
            print("Custo TOTAL caminho:", self.custoTotalDaRota, " metros")
        elif self.tipoCaminho == 1:
            print("Tipo de Caminho:  Tempo")
            print("Custo TOTAL caminho:", self.custoTotalDaRota, " minutos")
        else:
            print("Tipo de Caminho:  Distância/Tempo")
            print("Custo TOTAL caminho:", self.custoTotalDaRota, " metros/min")
    
        print("Velocidade de atualização:", self.tela.velociadeAtualizacao)
        print("Percurto total:  ((TODOS OS VERTICES POR ONDE PASSOU EM SEQUENCIA))")
        print("\nGrid: ", self.grid.tamanhoGrid,"x", self.grid.tamanhoGrid)
       
        

    # verifica se o pedido do endereço X ja foi entregue
    def verificaStatusEntrega(self, enderecoCliente):
        for i in range(len(self.listaEntrega_endStatus)):
            if self.listaEntrega_endStatus[i][0] == enderecoCliente:
                if self.listaEntrega_endStatus[i][1] == 1:
                    return True
                else:
                    return False
    
    # faz um clone da lista de endereços de entrega do grid, mas adiciona informação de (entregue ou não)
    def cloneListaDeEntregas(self):
        for i in range(len(self.grid.listaDePedidos)):
            end_status = [self.grid.listaDePedidos[i], 0]
            self.listaEntrega_endStatus.append(end_status)

    # depois de rodar o DFS pega na tabela o endereço com custo menor de deslocamento
    # so retorna endereços que sejam de clientes, se não ouver nemhuma entrega pra ser feita retorna NONE
    def pegarEnderecoMaisPerto(self):
        
        #pega o custo do primeiro vertice que n tenha sido entregue, para comparar com os demais 
        menorCustoEndere = None
        for i in range(len(self.listaEntrega_endStatus)):
            if self.listaEntrega_endStatus[i][1] == 0:
                menorCustoEndere = [self.custo_pi_finali[self.listaEntrega_endStatus[i][0]][0], self.listaEntrega_endStatus[i][0]]
                break
    
        # verifica com os demais, se for um vertice não finalizado e menor que o menor
        for i in range(len(self.listaEntrega_endStatus)):
            if self.listaEntrega_endStatus[i][1] == 0 and self.custo_pi_finali[self.listaEntrega_endStatus[i][0]][0] < menorCustoEndere[0]:
                menorCustoEndere = [self.custo_pi_finali[self.listaEntrega_endStatus[i][0]][0], self.listaEntrega_endStatus[i][0]]
        
        # se todas as entregas ja tivem sido feitas, então retornara NONE
        if menorCustoEndere != None:
            return menorCustoEndere[1]
        else:
            return None

    # ver qual o proximo cliente mais perto na tabela DFS, e com o PI, extrai o caminho ate ele.
    def pegarMenorCaminhoDaTabela(self):
        self.melhorCaminhoDFS = []
        custoTotalDoCaminho = 0

        proximo = self.pegarEnderecoMaisPerto()

        self.melhorCaminhoDFS.append(proximo)
        custoTotalDoCaminho = self.custo_pi_finali[proximo][0]
        while self.custo_pi_finali[proximo][1] != "null":
            self.melhorCaminhoDFS.append(self.custo_pi_finali[proximo][1])
            proximo = self.custo_pi_finali[proximo][1]
        
        self.melhorCaminhoDFS.reverse()
        caminho_custo = [self.melhorCaminhoDFS, custoTotalDoCaminho]
        return caminho_custo

    # cria a tabela do algoritimo DFS, de acordo com a quantidade de vertices
    # (seta tudo como null) para custos e PI(vertice anterior)
    def criaTabelaDFS(self):
        self.custo_pi_finali = []
        for i in range(self.grafo.numeroVertices):
            linha = []
            for x in range(2):
                linha.append("null")
            linha.append(0)
            self.custo_pi_finali.append(linha)

    # apenas imprimi na tela a tabela DFS
    def printTabelaDFS(self):

        print("\nDFS-------- -  CUSTO  -  PI  -  Finali. ")
        for i in range(self.grafo.numeroVertices):

            # VERTICE X: 
            if i in self.grid.listaDePedidos:
                print(Icone.COR_VERMELHO.value+"Vertice"+Icone.FIM_COR.value, i, ":    ", end="")
            else:
                print("Vertice", i, ":    ", end="")

            # CUSTO  -  PI  -  Finali.
            for x in range(3):
                if i == self.pegarEnderecoMaisPerto():
                    print(Icone.COR_VERDE.value+str(self.custo_pi_finali[i][x])+Icone.FIM_COR.value , "       ", end="")
                else:
                    print(str(self.custo_pi_finali[i][x]) , "       ", end="")
            print("")

    # Roda o alg. DFS partindo de um vertice referencia passado no parametro
    def dfs(self, vertReferencia):     

        # sempre zera variaveis antes de iniciar uma nova rodada 
        self.melhorCaminhoDFS = []
        self.criaTabelaDFS()

        for i in range(self.grafo.numeroVertices):

            # na 1º rodada estamos considerando ir do vertReferencia para todos os outros
            # mas depois temos que pegar o menor custo da tabela DFS(roda teste de mesa DFS pra entender) 
            if i > 0:
                vertReferencia = self.buscarMenor(self.custo_pi_finali)
            # ---

            for destino in range(self.grafo.numeroVertices):    

                # primeira rodada onde o vertReferencia é o ponto de partida(custo é 0 e anterior é Null)
                if i == 0 and destino == vertReferencia:
                        self.custo_pi_finali[destino][0] = 0

                # SE (aresta de referencia p/ Destino for valida) E (destino ainda não visitado)
                elif self.grafo.arestas[vertReferencia][destino][self.tipoCaminho] > 0 and self.custo_pi_finali[destino][2] == 0:

                    # se o custo para um vertice for INfinito então coloca o primeiro valor que encontrar
                    if self.custo_pi_finali[destino][0] == "null":

                        # tratamanto para primeira rodada quando, EVITA soma da proxima aresta com custo atual
                        # quando custo atual vale string NULL (da erro se somar INT + STR) 
                        if i == 0:
                            self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][self.tipoCaminho]
                            self.custo_pi_finali[destino][1] = vertReferencia
                        else:
                            #                                               (INTEIRO)                                      +    (INTEIRO)-> na primeira rodada isso pode ser uma string "null"
                            self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][self.tipoCaminho] + self.custo_pi_finali[vertReferencia][0]
                            self.custo_pi_finali[destino][1] = vertReferencia

                    else:
                        #SE o vertice de destino ja tiver um valor, nos somamos a aresta q vai pra ele mais o custo do Vertice que o descubriu
                        # se for menor então temos um caminho melhor e subistituimos.
                        if self.grafo.arestas[vertReferencia][destino][self.tipoCaminho] + self.custo_pi_finali[vertReferencia][0] < self.custo_pi_finali[destino][0]:
                            self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][self.tipoCaminho] + self.custo_pi_finali[vertReferencia][0]
                            self.custo_pi_finali[destino][1] = vertReferencia
            
            self.custo_pi_finali[vertReferencia][2] = 1 # finaliza a referencia

    # retorna o vertice com menor custo da tabela DFS(todo iniciam com custo INFINITO)
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

                    # no caso ele pega [Custo, vertice]
                    # pego o custo para debug(pode ser removido, como essa função ja esta funcionando)
                    menor[0] = lista[i][0]
                    menor[1] = i

        # mas retorno somento o vertice
        return menor[1]
        
   