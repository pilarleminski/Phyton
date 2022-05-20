'''
Elabore um programa que efetue a leitura de valores positivos reais até que 0 ou um valor negativo seja fornecido. Aplique o tratamento de exceção para recusar dados inválidos. Ao final devem ser apresentados: o maior e o menor valores informados pelo usuário, a quantidade de valores aceitos pelo programa, a soma e a média dos números lidos.
'''

count=0
maior=0
menor=999999999999999999999
soma=0
n=1
while n > 0:
    while True:
        try:
            n=float(input('Digite um número positivo diferente de zero: '))
            if (n > 0):
                count=count+1
                soma=soma+n
                if n > maior:
                    maior=n
                if n < menor:
                    menor=n
                break
            else:
                print('Valor <= 0, programa encerrado')
                print('aceitos {} | maior {} | menor {} | soma {} | media {}'.format(count, maior, menor, soma, soma/count))
                break
        except ValueError:
            print('Digite um valor numérico.')
   
    
    

    
