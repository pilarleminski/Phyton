"""
PILAR LEMINSKI VEIGA
Crie um vetor de tamanho x, sendo que x será informado pelo usuário (o valor de x deve estar entre 5 e 20).
Faça tratamento de exceção para este valor. Preencha este vetor com números inteiros aleatórios gerados
automaticamente pelo programa na faixa de 1 a 10. Mostre o vetor gerado. Escreva uma função que informe
quantas vezes cada número diferente armazenado no vetor se repetiu.
"""
from random import randint
"""
CONTA QUANTAS VEZES CADA NÚMERO SE REPETE NO VETOR
"""
def repetido():
    for i in range(1, 11):
        cont = vet.count(i)
        if cont != 0:
            print(f'{i} --> {cont} vezes')

"""
CRIA VETOR DO TAMANHO INFORMADO PELO USUÁRIO, ENTRE 5 E 20.
"""
while 1:
    x = 0
    vet = []
    try:
        x = int(input('Digite um valor entre 5 e 20: '))
        if x < 5 or x > 20:
            print('O valor deve estar entre 5 e 20')
        else:
            vet = [0] * x
            break
    except ValueError:
        print('O valor deve ser númerico')

"""
PREENCHE VETOR COM VALORES ALEATÓRIOS DE 1 A 10
"""
for c in range(x):
    vet.insert(c, randint(1, 10))
    vet.pop(c + 1)
print(vet)
repetido()
