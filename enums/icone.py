from enum import Enum


class Icone(Enum):
    # Icones
    ENTREGADOR = "\U0001F6F5"
    PIZZARIA = "\U0001F3ED"
    PIZZA = "\U0001F355"
    CLIENTE = "\U0001F9D1"
    CHECK = "\U00002705"
    N_ENTREGUE = "\U0000274C"

    # Cores
    COR_VERMELHO = "\033[31m" #VERMELHO
    COR_VERDE = "\033[32m" #VERDE
    COR_AMARELO = "\033[33m" #AMARELO
    COR_ROXO = "\033[35m" #ROXO
    FIM_COR = "\033[m"

    # Logo
    LOLOGPIZZAHUT = "PIZZ"+"\U0001F355"+"HUT"