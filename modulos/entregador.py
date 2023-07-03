import time
from modulos.grafo import Grafo
from modulos.tela import Tela
from enums.icone import Icone
from modulos.grid import Grid


class Entregador:

    def __init__(self, grafo: Grafo, grid: Grid, tela: Tela):
        self.grafo = grafo
        self.grid = grid
        self.tela = tela
        self.custo_pi_finali = []
        self.melhorCaminhoDijkstra = []
        self.tipoDeAresta = self.grid.tipoDeAresta
        self.listaEntrega_endStatus = []
        self.custoTotalDaRota = 0
        self.percursoTotal = []
        self.custosPercursoTotal = []

        self.distanciaMelhorDeTres = 0
        self.tempoMelhorDeTres = 0
        self.dist_tempoMelhorDeTres = 0

    # dada a lista de entregas, faz toda a lógica de entregar os pedidos
    # ultilizando as funções mais abaixo
    def iniciarEntregas(self):
        # --------1º rodada partimos da pizzaria--------

        #       clone lista e roda o dijkstra
        self.cloneListaDeEntregas()
        self.dijkstra(self.grid.enderecoPizzaHut)

        #       pega o caminho ate a entrega mais proxima(caminho, custoTotal)
        caminhoCusto = self.pegarMenorCaminhoDaTabela()

        #      salva o custo da rota             (numero, casas depois da virgula)
        self.custoTotalDaRota = round(self.custoTotalDaRota + caminhoCusto[1], 1)

        #       aqui fica todos os caminho de todas as entregas juntas(um percurso a cada pedido)
        self.percursoTotal.append(caminhoCusto[0])

        #       custo de todos as percursos juntos
        self.custosPercursoTotal.append(round(caminhoCusto[1], 1))

        #    move o entregador ponto a ponto pelo caminho q for passado
        self.moverEntregador(caminhoCusto[0])

        # --------continua entregando ate que não tenha mais endereços--------
        while (self.pegarEnderecoMaisPerto() != None):
            self.dijkstra(self.grid.entregador)
            caminhoCusto = self.pegarMenorCaminhoDaTabela()
            self.custoTotalDaRota = round(self.custoTotalDaRota + caminhoCusto[1], 1)
            self.percursoTotal.append(caminhoCusto[0])
            self.custosPercursoTotal.append(round(caminhoCusto[1], 1))
            self.moverEntregador(caminhoCusto[0])

        self.tela.limparTela()
        self.painel()
        self.grid.mostrarGrid()
        self.printTabelaDijkstra()

        #       pega o custo total de todas as entregas(para desitancia, tempo, dist/temp)
        #out: Tres caminhos ao mesmo tempo
        self.pegarDistanciaTempo()
        self.removerRepetidos()

   # faz um clone da lista de endereços de entrega do grid, mas adiciona informação de (entregue ou não)
    def cloneListaDeEntregas(self):
        for i in range(len(self.grid.listaDePedidos)):
            end_status = [self.grid.listaDePedidos[i], 0]
            self.listaEntrega_endStatus.append(end_status)

   # Roda o alg. Dijkstra partindo de um vertice referencia passado no parametro
    def dijkstra(self, vertReferencia):

        # sempre zera variaveis antes de iniciar uma nova rodada
        self.melhorCaminhoDijkstra = []
        self.criaTabelaDijkstra()

        for i in range(self.grafo.numeroVertices):

            # na 1º rodada estamos considerando ir do vertReferencia para todos os outros
            # mas depois temos que pegar o menor custo da tabela Dijkstra(roda teste de mesa Dijkstra pra entender)
            if i > 0:
                vertReferencia = self.buscarMenor(self.custo_pi_finali)
            # ---

            for destino in range(self.grafo.numeroVertices):

                # primeira rodada onde o vertReferencia é o ponto de partida(custo é 0 e anterior é Null)
                if i == 0 and destino == vertReferencia:
                    self.custo_pi_finali[destino][0] = 0

                # SE (aresta de referencia p/ Destino for valida) E (destino ainda não visitado)
                elif self.grafo.arestas[vertReferencia][destino][self.tipoDeAresta] > 0 and self.custo_pi_finali[destino][2] == 0:

                    # se o custo para um vertice for INfinito então coloca o primeiro valor que encontrar
                    if self.custo_pi_finali[destino][0] == "null":

                        # tratamanto para primeira rodada quando, EVITA soma da proxima aresta com custo atual
                        # quando custo atual vale string NULL (da erro se somar INT + STR)
                        if i == 0:
                            self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][self.tipoDeAresta]
                            self.custo_pi_finali[destino][1] = vertReferencia
                        else:
                            #                                               (INTEIRO)                                      +    (INTEIRO)-> na primeira rodada isso pode ser uma string "null"
                            self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][self.tipoDeAresta] + self.custo_pi_finali[vertReferencia][0]
                            self.custo_pi_finali[destino][1] = vertReferencia

                    else:
                        # SE o vertice de destino ja tiver um valor, nos somamos a aresta q vai pra ele mais o custo do Vertice que o descubriu
                        # se for menor então temos um caminho melhor e subistituimos.
                        if self.grafo.arestas[vertReferencia][destino][self.tipoDeAresta] + self.custo_pi_finali[vertReferencia][0] < self.custo_pi_finali[destino][0]:
                            self.custo_pi_finali[destino][0] = self.grafo.arestas[vertReferencia][destino][self.tipoDeAresta] + self.custo_pi_finali[vertReferencia][0]
                            self.custo_pi_finali[destino][1] = vertReferencia

            # finaliza a referencia
            self.custo_pi_finali[vertReferencia][2] = 1

    # retorna o vertice com menor custo da tabela Dijkstra(todo iniciam com custo INFINITO)
    def buscarMenor(self, lista):
        # csuto e seu indice
        menor = [None, None]
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

    # Procura na lista de endereços do entregador e marca o Pedido X como entregue(0 -> 1)
    def finalizaEndereco(self, endereco):
        for i in range(len(self.listaEntrega_endStatus)):
            if endereco == self.listaEntrega_endStatus[i][0]:
                self.listaEntrega_endStatus[i][1] = 1

    # move o entregador ponto a ponto pelo caminho q for passado
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

                        # procura o vertice para atualizar como entregue
                        vertice = self.grid.grid[linha][coluna][0]
                        if vertice == caminho[-1]:
                            self.grid.grid[linha][coluna][1] = 5
                            # aqui atualizamos a tela(esperar > limpar > mostraPainel > mostraGrid)
                            time.sleep(self.tela.velociadeAtualizacao)
                            self.tela.limparTela()
                            self.painel()
                            self.grid.mostrarGrid()

        # apos terminar a rota, o entrgador deve estar no endreço do cliente
        # então marcamos o endereço como Entregue/finalizado
        self.finalizaEndereco(self.pegarEnderecoMaisPerto())

    def painel(self):
        print("    "*5+Icone.LOLOGPIZZAHUT.value)
        print("------------"*4)
        print("Entregas", Icone.CLIENTE.value,
              ":[", self.grid.quantEntregas, "] :        ", end="")
        for i in range(len(self.listaEntrega_endStatus)):
            if self.listaEntrega_endStatus[i][1] == 1:
                print(
                    "("+str(self.listaEntrega_endStatus[i][0])+Icone.CHECK.value, end=")   ")
            else:
                print(
                    "("+str(self.listaEntrega_endStatus[i][0])+Icone.N_ENTREGUE.value, end=")   ")

        print("\nPizzaria:", Icone.PIZZARIA.value,
              ":", self.grid.enderecoPizzaHut)
        print("Entregador", Icone.ENTREGADOR.value, ":", self.grid.entregador)
        if self.pegarEnderecoMaisPerto() != None:
            print("melhor caminho de             ", Icone.COR_VERDE.value +
                  str(self.melhorCaminhoDijkstra[0])+Icone.FIM_COR.value, "->   ", end="")
            for i in range(len(self.melhorCaminhoDijkstra)):
                if self.melhorCaminhoDijkstra[i] == self.grid.entregador:
                    print(Icone.COR_AMARELO.value +
                          str(self.melhorCaminhoDijkstra[i])+Icone.FIM_COR.value, end=" - ")
                else:
                    print(Icone.COR_VERMELHO.value +
                          str(self.melhorCaminhoDijkstra[i])+Icone.FIM_COR.value, end=" - ")

            print("   ->", Icone.COR_VERDE.value +
                  str(self.melhorCaminhoDijkstra[-1])+Icone.FIM_COR.value)
        print(end="")
        if self.tipoDeAresta == 0:
            print("Tipo de aresta:  Distância")
            print("Custo TOTAL caminho:", self.custoTotalDaRota, " metros")
        elif self.tipoDeAresta == 1:
            print("Tipo de Caminho:  Tempo")
            print("Custo TOTAL caminho:", self.custoTotalDaRota, " minutos")
        else:
            print("Tipo de Caminho:  Tempo/distancia")
            print("Custo TOTAL caminho:", self.custoTotalDaRota, " metros/min")

        print("Percurto total:", self.percursoTotal)
        print("Custos:", self.custosPercursoTotal)
        print("Velocidade de atualização:", self.tela.velociadeAtualizacao)
        print("\nGrid: ", self.grid.tamanhoGrid, "x", self.grid.tamanhoGrid)

    # verifica se o pedido do endereço X ja foi entregue
    def verificaStatusEntrega(self, enderecoCliente):
        for i in range(len(self.listaEntrega_endStatus)):
            if self.listaEntrega_endStatus[i][0] == enderecoCliente:
                if self.listaEntrega_endStatus[i][1] == 1:
                    return True
                else:
                    return False

    # depois de rodar o Dijkstra, pega na tabela o endereço com menor custo de deslocamento
    # só retorna endereços que sejam de clientes, se não ouver nemhuma entrega pra ser feita retorna NONE
    def pegarEnderecoMaisPerto(self):

        # pega o custo do primeiro vertice(== end Entrega) que n tenha sido entregue, para comparar com os demais
        menorCustoEndere = None
        for i in range(len(self.listaEntrega_endStatus)):
            if self.listaEntrega_endStatus[i][1] == 0:
                menorCustoEndere = [
                    self.custo_pi_finali[self.listaEntrega_endStatus[i][0]][0], self.listaEntrega_endStatus[i][0]]
                break

        # verifica com os demais, se for um vertice não finalizado é menor que o menor
        for i in range(len(self.listaEntrega_endStatus)):
            if self.listaEntrega_endStatus[i][1] == 0 and self.custo_pi_finali[self.listaEntrega_endStatus[i][0]][0] < menorCustoEndere[0]:
                menorCustoEndere = [
                    self.custo_pi_finali[self.listaEntrega_endStatus[i][0]][0], self.listaEntrega_endStatus[i][0]]

        # se todas as entregas ja tiverem sido feitas, então retornara NONE
        if menorCustoEndere != None:
            return menorCustoEndere[1]
        else:
            return menorCustoEndere

    # ver qual o proximo cliente mais perto na tabela Dijkstra, e com o PI, extrai o caminho ate ele.
    def pegarMenorCaminhoDaTabela(self):
        self.melhorCaminhoDijkstra = []
        custoTotalDoCaminho = 0

        proximo = self.pegarEnderecoMaisPerto()

        self.melhorCaminhoDijkstra.append(proximo)
        custoTotalDoCaminho = self.custo_pi_finali[proximo][0]
        while self.custo_pi_finali[proximo][1] != "null":
            self.melhorCaminhoDijkstra.append(self.custo_pi_finali[proximo][1])
            proximo = self.custo_pi_finali[proximo][1]

        # retorna um caminho e o custo total desse caminho: [[2, 6, 4, 9], [56]]
        self.melhorCaminhoDijkstra.reverse()
        caminho_custo = [self.melhorCaminhoDijkstra, custoTotalDoCaminho]
        return caminho_custo

    # cria a tabela do algoritimo Dijkstra, de acordo com a quantidade de vertices
    # (seta tudo como null) para custos e PI(vertice anterior)
    def criaTabelaDijkstra(self):
        self.custo_pi_finali = []
        for i in range(self.grafo.numeroVertices):
            linha = []
            for x in range(2):
                linha.append("null")
            linha.append(0)
            self.custo_pi_finali.append(linha)

    # apenas imprimi na tela a tabela Dijkstra
    def printTabelaDijkstra(self):
        print("\nDijkstra------ CUSTO    -  PI    -  Finali. ")
        for i in range(self.grafo.numeroVertices):

            # VERTICE X:
            if i in self.grid.listaDePedidos:
                print(Icone.COR_VERMELHO.value+"Vertice" +
                      Icone.FIM_COR.value, i, ":    ", end="")
            else:
                print("Vertice", i, ":    ", end="")

            # CUSTO  -  PI  -  Finali.
            for x in range(3):
                if i == self.pegarEnderecoMaisPerto():
                    print(Icone.COR_VERDE.value +
                          str(self.custo_pi_finali[i][x])+Icone.FIM_COR.value, "       ", end="")
                else:
                    print(str(self.custo_pi_finali[i][x]), "       ", end="")
            print("")

    def pegarDistanciaTempo(self):
        for i in range(len(self.percursoTotal)):
            for x in range(len(self.percursoTotal[i])):
                if x+1 < len(self.percursoTotal[i]):
                    #                         selecionar aresta[linha, coluna]   -->   Aresta[distância, tempo, d/t]
                    #                         selecionar aresta[origem, destino]   -->   Aresta[0, 1, 2]
                    self.distanciaMelhorDeTres += (self.grafo.arestas[self.percursoTotal[i][x]][self.percursoTotal[i][x+1]][0])

                    self.tempoMelhorDeTres += (self.grafo.arestas[self.percursoTotal[i][x]][self.percursoTotal[i][x+1]][1])
                    
                    self.dist_tempoMelhorDeTres += (self.grafo.arestas[self.percursoTotal[i][x]][self.percursoTotal[i][x+1]][2])

    def removerRepetidos(self):
        for i in range(len(self.percursoTotal)):
            if i > 0:
                self.percursoTotal[i].pop(0)
           
