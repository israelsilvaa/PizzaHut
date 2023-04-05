from modulos.pizza import Pizza
from modulos.tela import Tela

tela = Tela()
tela.limparTela()

tamanhoGrid = int(input('Qual o tamanho do grid?(NxN):'))

peperoni = Pizza(tamanhoGrid)
#v = 2


peperoni.criarGrid()
peperoni.gridAtual()

peperoni.criarArestas()
peperoni.listaArestas()
