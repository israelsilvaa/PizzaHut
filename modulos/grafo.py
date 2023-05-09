from enums.icone import Icone
class Grafo:

    def __init__(self, tamanhoDoGrid):
        self.numeroVertices = tamanhoDoGrid * tamanhoDoGrid
        self.arestas = [[[0, 0, 0] for i in range(self.numeroVertices)]for j in range(self.numeroVertices)]

    def adicionarAresta(self, vertice1, vertice2, distancia, tempo):
        self.arestas[vertice1][vertice2] = [distancia, tempo, round((distancia/tempo)/2, 1)]
        self.arestas[vertice2][vertice1] = [distancia, tempo, round((distancia/tempo)/2, 1)]

    def getMatrizAdjacencias(self):
        print('\n                Aresta(Peso, Tempo)')
        print(end="       ")
        for linha in range(self.numeroVertices):
            print(linha, end="          ")
        print("")

        for linha in range(0, self.numeroVertices):
            for coluna in range(0, self.numeroVertices):
                if (coluna == 0):
                    if linha < 9:
                        print("0" + str(linha), end="_")
                    else:
                        print(linha + 1, end="_")
                if self.arestas[linha][coluna][0] == 0:
                    print(f"{self.arestas[linha][coluna]}  ", end="")
                else:
                    print(Icone.COR_VERMELHO.value +f"{self.arestas[linha][coluna]}  "+ Icone.FIM_COR.value, end="")
            print()