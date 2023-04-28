from modulos.grafo import Grafo
from modulos.grid import Grid
from modulos.tela import Tela
from modulos.entregador import Entregador

if __name__ == "__main__":

    tela = Tela()
    tela.limparTela()

    tamanhoGrid = 5

    grafo = Grafo(tamanhoGrid)

    grid = Grid(grafo, tamanhoGrid)

    grid.gerarGrid()
    grid.gerarArestasGrid()

    
    julinDaCg160 = Entregador(grafo, grid)

    grid.mostrarGrid()

    julinDaCg160.melhorCaminho()

    julinDaCg160.printTabelaDFS()

    print(grafo.arestas[0][8])

    # grafo.getMatrizAdjacencias()
