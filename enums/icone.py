from enum import Enum


class Icone(Enum):
    PIZZA = "\U0001F6F5"
    PIZZARIA = "\U0001F3ED"
    RESIDENCIA = "\U0001F9D1"
    ENTREGUE = "\U00002705"
    INICIO = "\033[31m" #VERMELHO
    # INICIO = "\033[32m" #VERDE
    # INICIO = "\033[33m" #AMARELO
    # INICIO = "\033[35m" #ROXO
    FIM = "\033[m"