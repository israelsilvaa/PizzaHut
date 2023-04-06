from modulos.pizza import Pizza


if __name__ == "__main__":


    # tamanhoGrid = int(input('Qual o tamanho do grid?(NxN):'))
    tamanhoGrid = 3

    peperoni = Pizza(tamanhoGrid)

    peperoni.gerarGrid()
    # peperoni.adicionarAresta(3, 4, 4, 5)

    peperoni.gerarArestasGrid()
    peperoni.mostrarGrid()
    peperoni.getMatrizAdjacencias()
