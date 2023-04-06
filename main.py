from modulos.pizza import Pizza
from modulos.tela import Tela

if __name__ == "__main__":

    tela = Tela()
    tela.limparTela()
    # tamanhoGrid = int(input('Qual o tamanho do grid?(NxN):'))
    tamanhoGrid = 8


    peperoni = Pizza(tamanhoGrid)

    peperoni.gerarGrid()
    # peperoni.adicionarAresta(3, 4, 4, 5)

    peperoni.gerarArestasGrid()
    peperoni.mostrarGrid()
    #peperoni.getMatrizAdjacencias()
