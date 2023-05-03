import os
from enums.icone import Icone

class Tela():

   def __init__(self):
      self.velociadeAtualizacao = 0.5

   def limparTela(self):
      os.system('cls')
   
   def painelConfigRapida(self, tamanhoGrid,tipoCaminho,enderecoPizzaHut,quantidateEntregas, velociadeAtualizacao):
      print("    "*5+Icone.LOLOGPIZZAHUT.value)
      print("------------"*4)
      print("              Configurações rapidas\n")
      print("[0] - concluir e iniciar simulação")
      print("[1] - Tamanho do grid:", tamanhoGrid, "x", tamanhoGrid)
      if tipoCaminho == 0:
         print("[2] - Tipo de aresta(usada no DFS): Distancia")
      elif tipoCaminho == 1:
         print("[2] - Tipo de aresta(usada no DFS): Tempo")
      elif tipoCaminho == 2:
         print("[2] - Tipo de aresta(usada no DFS): Tempo/distancia")

      if enderecoPizzaHut == None:
         print("[3] - Ponto de partida(0 a",tamanhoGrid*tamanhoGrid,"): Aleatorio")
      else:
         print("[3] - Ponto de partida(0 a",tamanhoGrid*tamanhoGrid,"):", enderecoPizzaHut)
      print("[4] - Quantidade de entregas:", quantidateEntregas)
      print("[5] - Velocidade da simulação:", velociadeAtualizacao)

        