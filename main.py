from modulos.pizza import Pizza
from modulos.tela import Tela

tela = Tela()
tela.limparTela()

#tamanhoGrid = int(input('Qual o tamanho do grid?(NxN):'))
tamanhoGrid = 3

peperoni = Pizza(tamanhoGrid)


peperoni.criarGrid()
peperoni.gridAtual()

peperoni.criarArestas()
peperoni.listaArestas()
