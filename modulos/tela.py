import os
from enums.icone import Icone

class Tela():

   def __init__(self):
      self.velociadeAtualizacao = 0.5

   def limparTela(self):
      os.system('cls')
   
   def painelConfigRapida(self, tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas, velociadeAtualizacao, listaPedidos):
      print("    "*5+Icone.LOLOGPIZZAHUT.value)
      print("------------"*4)
      print("              Configurações rapidas\n")
      print("[10] - Sair")
      if len(listaPedidos) == 0:
         print("[6] - Lista de Pedidos: 1 pedido aleatorio(default)")
      else:
         print("[6] - Lista de Pedidos:", listaPedidos)
      print("[5] - Velocidade da simulação:", velociadeAtualizacao)
      print("[4] - Quantidade de entregas:", quantidateEntregas)

      if enderecoPizzaHut == None:
         print("[3] - Ponto de partida(0 a",tamanhoGrid*tamanhoGrid,"): Aleatorio")
      else:
         print("[3] - Ponto de partida(0 a",tamanhoGrid*tamanhoGrid,"):", enderecoPizzaHut)
      
      if tipoCaminho == 0:
         print("[2] - Tipo de aresta(usada no DFS): Distancia")
      elif tipoCaminho == 1:
         print("[2] - Tipo de aresta(usada no DFS): Tempo")
      elif tipoCaminho == 2:
         print("[2] - Tipo de aresta(usada no DFS): Tempo/distancia")
      
      print("[1] - Tamanho do grid:", tamanhoGrid, "x", tamanhoGrid)
      print("[0] - concluir e iniciar simulação")

        