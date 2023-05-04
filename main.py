import time
from modulos.grafo import Grafo
from modulos.grid import Grid
from modulos.tela import Tela
from modulos.entregador import Entregador

if __name__ == "__main__":
    tela = Tela()
        
    tamanhoGrid = 3
    tipoCaminho = 0
    enderecoPizzaHut = None
    quantidateEntregas = 1
    velociadeAtualizacao = 2
    listaPedidos = []

    opc = 1
    tela.limparTela()
    tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
    while opc != 10:
        
        if opc != 0:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            opc = int(input("\nOpção:"))
        if opc == 6:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            print("\ninforme um vertice negativo para cancelar(ex: -1)")
            NovoPedido = int(input("\nAdicionar pedido:"))
            if NovoPedido != -1:
                listaPedidos.append(NovoPedido)
            while NovoPedido != -1:
                tela.limparTela()
                tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
                print("\ninforme um vertice negativo para cancelar(ex: -1)")
                NovoPedido = int(input("\nAdicionar pedido:"))
                if NovoPedido != -1:
                    listaPedidos.append(NovoPedido)
                    quantidateEntregas = len(listaPedidos)
        if opc == 5:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            velociadeAtualizacao = float(input("\nVelocidade da simulação:"))
        elif opc == 4:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            quantidateEntregas = int(input("\nQuantidade de entregas:"))
        elif opc == 3:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            enderecoPizzaHut = int(input("\nPonto de partida:"))
        elif opc == 2:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            print("\n[0]Distancia | [1]Tempo | [2]Tempo/Distancia")
            tipoCaminho = int(input("\nTipo de aresta(usada no DFS):"))
        elif opc == 1:
            tela.limparTela()
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            tamanhoGrid = int(input("\nTamanho do grid NxN:"))
        elif opc == 0:        
            tela.velociadeAtualizacao = velociadeAtualizacao

            grafo = Grafo(tamanhoGrid)
            grid = Grid(grafo, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
            grid.gerarGrid()
            grid.gerarArestasGrid()
            julinDaCg160 = Entregador(grafo, grid, tela)
            julinDaCg160.iniciarEntregas()

            print("[0] - Sair     [1] - Rodar novamente      [2] - Configurar e rodar novamente:")
            opc = int(input("\nOpção:"))
            if opc == 0:
                opc = 10
            if opc == 1:
                opc = 0
            elif opc == 2:
                opc = 99

    tela.limparTela()
    print("       Obrigado por usar nosso simulador <3")
    time.sleep(3)



    # grafo.getMatrizAdjacencias()
