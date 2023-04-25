from modulos.grafo import Grafo
from modulos.grid import Grid
from modulos.tela import Tela

if __name__ == "__main__":

    tela = Tela()
    tela.limparTela()

    tamanhoGrid = 6

    grafo = Grafo(tamanhoGrid)

    grid = Grid(grafo, tamanhoGrid)

    grid.gerarGrid()
    grid.gerarArestasGrid()
    grid.mostrarGrid()
