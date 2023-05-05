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
         print("[2] - Aresta(usada no DFS): Distancia")
      elif tipoCaminho == 1:
         print("[2] - Aresta(usada no DFS): Tempo")
      elif tipoCaminho == 2:
         print("[2] - Aresta(usada no DFS): Tempo/distancia")
      
      print("[1] - Grid:", tamanhoGrid, "x", tamanhoGrid)
      print("[0] - concluir e iniciar simulação")

        