from enum import Enum


class Icone(Enum):
    PIZZA = "\U0001F355"
    PIZZARIA = "\U0001F3ED"
    RESIDENCIA = "\U0001F9D1"
    ENTREGUE = "\U00002705"
    # INICIO = "\033[0;31;40m" #VERMELHOR
    # INICIO = "\033[0;32;40m" #VERDE
    # INICIO = "\033[0;33;40m" #AMARELO
    INICIO = "\033[0;34;40m" #ROXO
    FIM = "\033[m"
