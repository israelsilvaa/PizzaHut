
Classes e suas funções

class Tela:
    - limparTela(self): [OK !!!]
        limpa a tela com o comando "clear" nativo do terminal so S.O.

class pizza:
    __init__(): [OK !!!]
        inicia algumas variavies do objeto, para que quando usar metodos, n tenha necessidade de passar por parametro, so acessamos elas com "self.variavel"

    criarGrid(self): [OK !!!]
        -gerar um mapa(gird) NxN

    criarArestas(self): [OK !!!]
        -gera uma matriz com todos as arestas possiveis para o grid NxN, e nas arestas que compoe o grid adiciona pesos e tempo aleatórios

    enderecoPizza(self, x, y): [não feito!!!!!!]
        -gerar end. da pizzaria no grid
    
    criarEndEntrega(self, x,y): [não feito!!!!!!]
        -selecionar endereços para fazer entrega

class entregador:
    __init__(): [não feito!!!!!!]
        inicializa variaves para serem usadas nos metodos

    -calcularRotas(self, endereco1, endereco2, endereco3):[não feito!]
        melhor caminho entre os 3 endereços
    
    -movimentação(self, endereco): [não feito!!!!!!]
        ir do ponto atual para o endereço X


#https://python.igraph.org/en/stable/