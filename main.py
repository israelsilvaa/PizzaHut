from modulos.entregador import Entregador
from modulos.grafo import Grafo
from modulos.grid import Grid
from modulos.tela import Tela
from enums.icone import Icone
import random
import time

if __name__ == "__main__":
    tela = Tela()
        
    tamanhoGrid = 7
    tipoCaminho = 0
    enderecoPizzaHut = random.randint(1, tamanhoGrid*tamanhoGrid - 1)
    quantidateEntregas = 8
    velociadeAtualizacao = 0.1
    listaPedidos = []
    compararCaminhos = False

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
            print("\n[0]Distancia | [1]Tempo | [2]Tempo/Distancia | [3]melhor de todos")
            tipoCaminho = int(input("\nTipo de aresta(usada no Dijkstra):"))
            if tipoCaminho == 3:
                tipoCaminho = 0
                compararCaminhos = True
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

            if compararCaminhos: 
                tela.velociadeAtualizacao = 0
                grafo1 = Grafo(tamanhoGrid)
                
                
                grid1 = Grid(grafo1, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
                grid1.gerarGrid()

                grid2 = Grid(grafo1, tamanhoGrid, 1, enderecoPizzaHut, quantidateEntregas, grid1.listaDePedidos)
                grid3 = Grid(grafo1, tamanhoGrid, 2, enderecoPizzaHut, quantidateEntregas, grid1.listaDePedidos)
                grid2.gerarGrid()
                grid3.gerarGrid()
                grid1.gerarArestasGrid()
                grid2.gerarArestasGrid()
                grid3.gerarArestasGrid()

                entregador1 = Entregador(grafo1, grid1, tela)
                entregador1.iniciarEntregas()
                
                entregador2 = Entregador(grafo1, grid2, tela)
                entregador2.iniciarEntregas()
                
                entregador3 = Entregador(grafo1, grid3, tela)
                entregador3.iniciarEntregas()

                tela.limparTela()
                entregador1.painel()
                print("\nAresta tipo: Distancia")
                print("Distancia:", entregador1.custoTotalDaRota," Tempo:", entregador1.tempoMelhorDeTres," soma:", entregador1.dist_tempoMelhorDeTres)
                print("Percurso:", entregador1.percursoTotal)
      
                print("\nAresta tipo: Tempo")
                print("Distancia:", entregador2.distanciaMelhorDeTres," Tempo:", entregador2.custoTotalDaRota," soma:", entregador2.dist_tempoMelhorDeTres)
                print("Percurso:", entregador2.percursoTotal)
             
                print("\nAresta tipo: soma")
                print("Distancia:", entregador3.distanciaMelhorDeTres," Tempo:", entregador3.tempoMelhorDeTres, " soma:", entregador3.custoTotalDaRota)
                print("Percurso:", entregador3.percursoTotal)
           
                print('\n')
                entregador1.grid.mostrarGrid()
            
                print("[0]-Sair",Icone.N_ENTREGUE.value, "     [1]-Repet",Icone.REPETIR.value, "     [2]-Config",Icone.CONFIG.value+" e Repet"+Icone.REPETIR.value , ":")
                # grafo1.getMatrizAdjacencias()
                opc = int(input("\nOpção:"))
                if opc == 0:
                    opc = 10
                if opc == 1:
                    opc = 0
                elif opc == 2:
                    compararCaminhos = False
                    opc = 99
            else:
                tela.velociadeAtualizacao = velociadeAtualizacao

                grafo1 = Grafo(tamanhoGrid)
                
                grid1 = Grid(grafo1, tamanhoGrid, tipoCaminho, enderecoPizzaHut, quantidateEntregas, listaPedidos)
                grid1.gerarGrid()

                grid1.gerarArestasGrid()
          
                entregador1 = Entregador(grafo1, grid1, tela)
                entregador1.iniciarEntregas()
              
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
