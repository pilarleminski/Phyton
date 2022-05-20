from random import choice

print("*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************")

lista = ['banana', 'morango', 'abacaxi', 'caqui', 'pera', 'uva']
palavra_secreta = choice(lista).upper().strip()
resp='s'
chances=6
while resp=='s':
    letras_acertadas = ['' for letra in palavra_secreta]
    print(letras_acertadas)

    #Cria uma varíavel reposta pois a palavra secreta será transformada em lista
    resposta = palavra_secreta
    palavra_secreta = list(palavra_secreta)

    #Cria um lista com as letras digitadas
    letras_digitadas = []

    while chances > 0:
        letra = input('Digite uma letra:').upper()
        for i in palavra_secreta:
            if i == letra:
                #pega o index da letra em palavra secreta
                index = palavra_secreta.index(letra)
                letras_acertadas[index] = letra #coloca a letra no mesmo índice indicado em letras_acertadas
            else:
                chances -= 1
        print(letras_acertadas)

        #Avisa que a letra já foi digitada
        if letra in letras_digitadas:
            print("Esta letra já foi digitada!")

        #Verifica se a palavra já foi completada
        palavra_valida = ''
        for i in letras_acertadas:
            palavra_valida+=i

        #Para o loop
        if resposta == palavra_valida:
            break
