from modulos.grafo import Grafo
from modulos.grid import Grid
from modulos.tela import Tela
from modulos.entregador import Entregador

if __name__ == "__main__":

    tela = Tela()

    tamanhoGrid = 5

    grafo = Grafo(tamanhoGrid)
    grid = Grid(grafo, tamanhoGrid)

    tela.velociadeAtualizacao = 0.5
    grid.tipoCaminho = 0
    grid.enderecoPizzaHut = 0
    grid.quantEntregas = 6

    grid.gerarGrid()

    grid.gerarArestasGrid()

    julinDaCg160 = Entregador(grafo, grid, tela)

    julinDaCg160.iniciarEntregas()


    # grafo.getMatrizAdjacencias()
