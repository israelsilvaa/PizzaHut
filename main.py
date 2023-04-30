from modulos.grafo import Grafo
from modulos.grid import Grid
from modulos.tela import Tela
from modulos.entregador import Entregador

if __name__ == "__main__":

    tela = Tela()
    tela.limparTela()

    tamanhoGrid = 4

    grafo = Grafo(tamanhoGrid)

    grid = Grid(grafo, tamanhoGrid)

    grid.gerarGrid()
    grid.gerarArestasGrid()

    
    julinDaCg160 = Entregador(grafo, grid)

    julinDaCg160.iniciarEntregas()


    # grafo.getMatrizAdjacencias()
