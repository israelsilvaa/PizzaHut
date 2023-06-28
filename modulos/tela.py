import os
from enums.icone import Icone

class Tela():

   def __init__(self):
      self.velociadeAtualizacao = 0.5

   def limparTela(self):
      os.system('cls')
   
   def painelConfigRapida(self, tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas, velociadeAtualizacao, listaPedidos):
      self.limparTela()
      print("    "*5+Icone.LOLOGPIZZAHUT.value)
      print("------------"*4)
      print("              Configurações rapidas\n")
      print("[10] - Sair")
      print("[7] - SOBRE",Icone.EXCLAMACAO.value)
      if len(listaPedidos) == 0:
         print("[6] - Pedidos: ",quantidateEntregas," aleatorio(default)")
      else:
         print("[6] - Pedidos:", listaPedidos)
      print("[5] - Velocidade:",float(velociadeAtualizacao), "'s")
      print("[4] - Quant. de entregas:", quantidateEntregas)

      if enderecoPizzaHut == None:
         print("[3] - Pizzaria(0 a",tamanhoGrid*tamanhoGrid - 1,"): Aleatorio")
      else:
         print("[3] - Pizzaria(0 a",tamanhoGrid*tamanhoGrid - 1,"):", enderecoPizzaHut)
      
      if tipoCaminho == 0:
         print("[2] - Aresta(usada no Dijkstra): Distancia")
      elif tipoCaminho == 1:
         print("[2] - Aresta(usada no Dijkstra): Tempo")
      elif tipoCaminho == 2:
         print("[2] - Aresta(usada no Dijkstra): Tempo/distancia")
      
      print("[1] - Grid:", tamanhoGrid, "x", tamanhoGrid)
      print("[0] - concluir e iniciar simulação")

   def sobre(self):
      self.limparTela()
      print(Icone.COR_VERDE.value,"             SISTEMAS DE INFORMAÇÃO\n\n", Icone.FIM_COR.value)
      print(Icone.COR_AMARELO.value,"Disciplina: ",Icone.FIM_COR.value ,"Estruturas de dados II")
      print(Icone.COR_AMARELO.value,"Docente:",Icone.FIM_COR.value ,"Prof. Dr. Carlos Gustavo Resques Dos Santos")
      print(Icone.COR_AMARELO.value,"Discentes:",Icone.FIM_COR.value ," Israel Pinheiro da Silva")
      print("              Mateus Vinicius Santiago Melo ")
      print("              Weslei Marcelo Amorin Dos Santos")
      print("              Adriano Silva Portal Marinho\n\n")
      print(Icone.COR_AMARELO.value,"             Tema do Projeto:",Icone.FIM_COR.value ," Entregador de Pizza\n")
      print(Icone.COR_AMARELO.value,"Descrição:",Icone.FIM_COR.value ," programa que faça simulação de entregas de pizza em uma ""mapa"" NxN")
      print(Icone.COR_AMARELO.value,"Objetivos:",Icone.FIM_COR.value, Icone.COR_VERMELHO.value," 1 -",Icone.FIM_COR.value,"Gerar um mapa em grid de tamanho NxN")
      print(Icone.COR_VERMELHO.value,"\n               2 -",Icone.FIM_COR.value,"Considere que cada caminho desse grid possui um tempo de")
      print("                     passagem e uma distância (ambos aleatórios).")
      print(Icone.COR_VERMELHO.value,"\n               3 -",Icone.FIM_COR.value,"Para 1 entregador de pizza ache os três melhores caminhos para 1 destino considerando:")
      print("                     •Tempo \n                     •Menorcaminho \n                     •Ambosaomesmotempo")
      print(Icone.COR_VERMELHO.value,"\n               4 -",Icone.FIM_COR.value,"Faça o mesmo para D destinos consecutivos.")
      print(Icone.COR_VERMELHO.value,"\n               5 -",Icone.FIM_COR.value,"Realize várias simulações e mostre elas rodando na aplicação dando a opção de trocar") 
      print("                    de parâmetros.\n\n\n")
      print(Icone.COR_AMARELO.value,"Principal Algoritmo Utilizado:",Icone.FIM_COR.value ,Icone.COR_VERMELHO.value,"O Algoritmo de Dijkstra (E.W. Dijkstra)", Icone.FIM_COR.value, "é um dos algoritmos que calcula")
      print("               o caminho de custo mínimo entre vértices de um grafo. Escolhido um vértice como raiz da busca,")
      print("               este algoritmo calcula o custo mínimo deste vértice para todos os demais vértices do grafo.Ele")
      print("               é bastante simples e com um bom nível de performance.")

      print(Icone.COR_VERDE.value,"\n\n\n                Pressione ENTER para sair. '-'", Icone.FIM_COR.value)