from modulos.grafo import Grafo
from modulos.grid import Grid
from modulos.tela import Tela
from modulos.entregador import Entregador

if __name__ == "__main__":

    tela = Tela()

    tamanhoGrid = 3


    # tela.velociadeAtualizacao = 2
    # grid.tipoCaminho = 0
    # grid.enderecoPizzaHut = 0
    # grid.quantEntregas = 3
        
    tamanhoGrid = 3
    tipoCaminho = 0
    enderecoPizzaHut = None
    quantidateEntregas = 1
    velociadeAtualizacao = 2

    opc = 1
    tela.limparTela()
    tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas, velociadeAtualizacao)
    while opc != 0:
        
        tela.limparTela()
        tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao)
        opc = int(input("\nOpção:"))
        if opc == 1:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao)
            tamanhoGrid = int(input("\nTamanho do grid NxN:"))
        if opc == 2:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao)
            tipoCaminho = int(input("\nTipo de aresta(usada no DFS):"))
        if opc == 3:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao)
            enderecoPizzaHut = int(input("\n Ponto de partida(0 a 25 :"))
        if opc == 4:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao)
            quantidateEntregas = int(input("\nQuantidade de entregas:"))
        if opc == 5:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao)
            velociadeAtualizacao = float(input("\nVelocidade da simulação:"))


    grafo = Grafo(tamanhoGrid)
    grid = Grid(grafo, tamanhoGrid)

    grid.gerarGrid()

    grid.gerarArestasGrid()

    julinDaCg160 = Entregador(grafo, grid, tela)

    julinDaCg160.iniciarEntregas()


    # grafo.getMatrizAdjacencias()
