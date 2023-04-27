from modulos.grafo import Grafo
class Entregador:

    def __init__(self, grafo: Grafo):
        self.teste = "testando"
        self.grafo = grafo
        self.tempo = None
        self.inicio_fim_pi_cor = []

        #pegar o endereço da pizzaria para inciar o DFS
        self.vertice_inicial_entrega = 0

    
    def melhorCaminho(self):
        for i in range(self.grafo.numeroVertices):
            linha = []
            for x in range(4):
                linha.append("null")
            self.inicio_fim_pi_cor.append(linha)
        print("variavel teste: ", self.grafo.arestas[0][1][0])

        # Seta todos os vertices para a cor branca
        for i in range(self.grafo.numeroVertices):
            self.inicio_fim_pi_cor[i][3] = 'branco'
        
        print("DFS-------- T_inicio  - T_fim  - PI   -  COR ")
        for i in range(self.grafo.numeroVertices):
            print("Vertice", i, ":    ", end="")
            for x in range(4):
                print(self.inicio_fim_pi_cor[i][x], "    ", end="")
            print("")