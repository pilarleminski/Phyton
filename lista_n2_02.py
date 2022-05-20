"""
PILAR LEMINSKI VEIGA
2)	Crie um programa que leia o nome, idade e salário de diversas pessoas,
guardando os dados de cada pessoa em um dicionário, e todos os dicionários em uma lista.
Quando o nome for repetido, descarte e quando for vazio, encerre o programa.
Ao encerrar o programa mostre.
a.	Os dados das pessoas cadastradas (formatados)
b.	Quantas pessoas foram cadastradas
c.	A média de idade do grupo
d.	Uma lista de todas as pessoas com idade acima da média de idades
e.	A soma de todos os salários
"""
cont = 0
x = 0
lista = []
lista_nomes = []
lista_idade = []
pessoas = dict()
media_idade = 0
soma_salario = 0

"""
CRIA DICIONÁRIO PARA CADA ENTRADA DE DADOS COMPLETOS, 
INCREMENTA O CONTADOR cont PARA CADA ENTRADA E 
CRIA LISTA COM OS DICIONÁRIOS DE CADA ENTRADA COMPLETA
"""
while 1:
    nome = input('NOME: ')
    if nome in lista_nomes:
        print('Pessoa já cadastrada')
        continue
    else:
        lista_nomes.append(nome)
    if nome == '':
        for nome, dados in pessoas.items():
            print(f'{dados["nome"]}\t |\t {dados["idade"]} anos\t |\t Salário: R${dados["salario"]}')
        break
    else:
        cont += 1
    idade = int(input('IDADE: '))
    lista_idade.append(idade)
    media_idade += idade
    salario = float(input('SALÁRIO: R$ '))
    soma_salario += salario
    dicPessoas = {'nome': nome, 'idade': idade, 'salario': salario} #Cria um dicionário temporário
    pessoas[nome] = dicPessoas
    lista.append(dicPessoas)  #Armazena o dicionário temporário em uma lista
print(f'O total de pessoas cadastradas foi {cont}')
print('A média de idade do grupo é {:.2f}'.format(media_idade/cont))
print('A soma dos salario é R$ {:.2f}'.format(soma_salario))
print('As pessoas com idade acima da média são:')
while x < len(lista_nomes) - 1:
    if lista_idade[x] > media_idade/cont:
        print(f'{lista_nomes[x]}')
        x += 1
    else:
        x += 1

