import random

#v = int(input('Qual a quantidade de vertices?:'))
v = 10
end  = ""



print("\n")
matriz = []
numero = 1
for i in range(1, v+1):
    linha = ["x"]
    for x in range(1, v+1):
        linha.append(numero)
        numero = numero + 1
        #linha.append(".")
    matriz.append(linha)
    
for linha in range(1, v+1):
    for coluna in range(1, v+1):
        if coluna == 1:
            print(  end="- ")
        if linha == 73 and coluna == 5:
            matriz[linha][coluna] = '0'
        print( matriz[linha-1][coluna], ' ', end='')
        
    print(' \n')

print('Coordenadas(inicio, destino)\n\n\n')
v = v*v
teste = []
for i in range(1, v+1):
    #indice 0 é adicionado, mas não vamos usar
    linha = [['','']]
    for x in range(1, v+1):
        pesoTempo = [0, 0]
        if i != x and i != 1 and i + 1 >= x and i+x != 10:
            pesoTempo[0] = random.randint(1, 4)
            pesoTempo[1] = random.randint(5, 9)

        linha.append(pesoTempo)
    teste.append(linha)

if 0:
    for linha in range(1, v+1):
        for coluna in range(1, v+1):
            if (coluna == 1):
                print(linha, end="_")
            print(teste[linha-1][coluna], ' ', end='')
        print('')
        
    for linha in range(1, v+1):
        print("---",linha, end="---")    
    print('\nAresta(Peso, Tempo)')
'''
for linha in range(1, v+1):
    for coluna in range(1, v+1):
        print(matriz[linha-1][coluna], '', end='')

        if(coluna <= v-1 and linha == 2):
            print('- ', end='')
        elif(coluna == 2):
            print('| ', end='')
        else:
            print('  ', end='')
    print('')
'''

#https://python.igraph.org/en/stable/