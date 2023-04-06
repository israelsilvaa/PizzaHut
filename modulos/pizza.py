import os
import random

class Pizza:
    grid = []
    arestas = []
    tamanhoGrid = None
    
    def __init__(self, tamanhoDoGrid):
        self.tamanhoGrid = tamanhoDoGrid
        
    def criarGrid(self):
        global grid
        global arestas
        global tamanhoGrid
        
        numero = 1
        for i in range(1, self.tamanhoGrid+1):
            linha = ["x"]
            for x in range(1, self.tamanhoGrid+1):
                linha.append(numero)
                numero = numero + 1
                # linha.append(".")
            self.grid.append(linha)
            

    def criarArestas(self):
        global grid
        global arestas
        global tamanhoGrid
        self.tamanhoGrid = self.tamanhoGrid * self.tamanhoGrid
        
        for i in range(1, self.tamanhoGrid+1):
            # indice 0 é adicionado, mas não vamos usar
            linha = [['', '']]
            for x in range(1, self.tamanhoGrid+1):
                pesoTempo = [0, 0]
                if i != x and i != 1 and i + 1 >= x and i+x != 10:
                    pesoTempo[0] = random.randint(1, 4)
                    pesoTempo[1] = random.randint(5, 9)
                linha.append(pesoTempo)
            self.arestas.append(linha)

    def gridAtual(self):
        global grid
        global arestas
        global tamanhoGrid
        
        for linha in range(1, self.tamanhoGrid+1):
            for coluna in range(1, self.tamanhoGrid+1):
                if linha == 3 and coluna == 5:
                    self.grid[linha][coluna] = '0'
                print(self.grid[linha-1][coluna], ' ', end='')
            print(' \n')

        print("\n")
    
    def listaArestas(self):
        global grid
        global arestas
        global tamanhoGrid
    
        print('\n                Aresta(Peso, Tempo)')
        for linha in range(1, self.tamanhoGrid+1):
            print("---",linha, end="---")    
        print("")

        for linha in range(1, self.tamanhoGrid+1):
            for coluna in range(1, self.tamanhoGrid+1):
                if (coluna == 1):
                    print(linha, end="_")
                print(self.arestas[linha-1][coluna], ' ', end='')
            print('')
        print("\nCoordenada da aresta (Linha, coluna)\n")
        print("Exemplo: uma aresta ligando o Vertice 8 ao 9")
        print("teriamos um PESO e um TEMPO gravados nas coordenadas: Linha 8 e Coluna 9\n")
        print("Ou seja: (8,9)\n")
        print("\n")
        
        print("\n")

   
