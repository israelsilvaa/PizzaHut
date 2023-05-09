from modulos.entregador import Entregador
from modulos.grafo import Grafo
from modulos.grid import Grid
from modulos.tela import Tela
from enums.icone import Icone
import random
import time

if __name__ == "__main__":
    tela = Tela()
        
    tamanhoGrid = 3
    tipoCaminho = 2
    enderecoPizzaHut = random.randint(1, tamanhoGrid*tamanhoGrid - 1)
    quantidateEntregas = 1
    velociadeAtualizacao = 0.5
    listaPedidos = []

    grafoPreview = Grafo(tamanhoGrid)
    gridPreview = Grid(grafoPreview, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
    gridPreview.gerarGrid()
    gridPreview.gerarArestasGrid()
    gridPreview.mostrarGrid()

    opc = 1
    tela.limparTela()
    # tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
    while opc != 10:
        
        # perguntar qual a proxima opc, 
        if opc != 0:
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            grafoPreview = Grafo(tamanhoGrid)
            gridPreview = Grid(grafoPreview, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
            gridPreview.gerarGrid()
            gridPreview.gerarArestasGrid()
            gridPreview.mostrarGrid()
            # grafoPreview.getMatrizAdjacencias()
            opc = int(input("\nOpção:"))

        if opc == 7:
            tela.sobre()
            sair = str(input())

        elif opc == 6:
            NovoPedido = 99
            while NovoPedido != -1:
               
                tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
                gridPreview = Grid(grafoPreview, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
                gridPreview.gerarGrid()
                gridPreview.gerarArestasGrid()
                gridPreview.mostrarGrid()
                print("\n[-1]cancelar   [-2]Remover ultimo:")
                NovoPedido = int(input("\nAdicionar pedido:"))
                if NovoPedido >= 0 and not(NovoPedido in listaPedidos) and NovoPedido != enderecoPizzaHut and NovoPedido <= tamanhoGrid * tamanhoGrid - 1:
                    listaPedidos.append(NovoPedido)
                    quantidateEntregas = len(listaPedidos)
                elif NovoPedido == -2 and len(listaPedidos) >= 1:
                    listaPedidos.pop()
                    quantidateEntregas = len(listaPedidos)
                    if quantidateEntregas == 0:
                        quantidateEntregas = 1

        elif opc == 5:
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            gridPreview = Grid(grafoPreview, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
            gridPreview.gerarGrid()
            gridPreview.gerarArestasGrid()
            gridPreview.mostrarGrid()
            velociadeAtualizacao = float(input("\nVelocidade da simulação:"))
        elif opc == 4:
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            gridPreview = Grid(grafoPreview, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
            gridPreview.gerarGrid()
            gridPreview.gerarArestasGrid()
            gridPreview.mostrarGrid()
            quantidateEntregas = int(input("\nQuantidade de entregas:"))
        elif opc == 3:
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            gridPreview = Grid(grafoPreview, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
            gridPreview.gerarGrid()
            gridPreview.gerarArestasGrid()
            gridPreview.mostrarGrid()
            novoPontoPartida = int(input("\nPizzaria:"))
            if not(novoPontoPartida in listaPedidos):
                enderecoPizzaHut = novoPontoPartida
        elif opc == 2:
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            gridPreview = Grid(grafoPreview, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
            gridPreview.gerarGrid()
            gridPreview.gerarArestasGrid()
            gridPreview.mostrarGrid()
            print("\n[0]Distancia | [1]Tempo | [2]Tempo/Distancia")
            tipoCaminho = int(input("\nTipo de aresta(usada no Dijkstra):"))
        elif opc == 1:
            tela.painelConfigRapida(tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas,velociadeAtualizacao, listaPedidos)
            gridPreview = Grid(grafoPreview, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
            gridPreview.gerarGrid()
            gridPreview.gerarArestasGrid()
            gridPreview.mostrarGrid()
            tamanhoGrid = int(input("\nTamanho do grid NxN:"))
            while True:
                valor = random.randint(1, tamanhoGrid*tamanhoGrid - 1)
                if valor in listaPedidos:
                    valor = random.randint(1, tamanhoGrid*tamanhoGrid - 1)
                else:
                    enderecoPizzaHut = valor
                    break

        elif opc == 0:        
            tela.velociadeAtualizacao = velociadeAtualizacao

            grafo = Grafo(tamanhoGrid)
            grid = Grid(grafo, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
            grid.gerarGrid()
            grid.gerarArestasGrid()
            julinDaCg160 = Entregador(grafo, grid, tela)
            julinDaCg160.iniciarEntregas()

            print("[0]-Sair",Icone.N_ENTREGUE.value, "     [1]-Repet",Icone.REPETIR.value, "     [2]-Config",Icone.CONFIG.value+" e Repet"+Icone.REPETIR.value , ":")
            opc = int(input("\nOpção:"))
            if opc == 0:
                opc = 10
            if opc == 1:
                opc = 0
            elif opc == 2:
                opc = 99

    tela.limparTela()
    print("\n\n\n\n\n\n                  ", Icone.LOLOGPIZZAHUT.value)
    print("       Obrigado por usar nosso simulador <3\n\n\n\n\n\n")
    time.sleep(3)



    # grafo.getMatrizAdjacencias()
