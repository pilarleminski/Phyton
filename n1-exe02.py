'''
Elabore um programa que leia uma data como uma string no formato dd/mm/aaaa, e informe se esta data é válida ou não! Use fatiamento (slices) para separar as partes da data. Caso a data seja válida, escreva a mesma com o mês por extenso.
No caso de a data ser recusada, informe o motivo: dia inválido, mês inválido, ano não bissexto.
O programa deve ter tratamento de exceção e só aceitar datas no formato acima mencionado.
Prever repetição.
Ex: 15/09/2020 -> 15 de setembro de 2020.
31/04/2020 -> dia inválido
29/02/2021 -> ano não bissexto
13/13/2021-> mês inválido
'''
dia=0
mes=0
mes_texto=''
ano=0
while True:
    data=input('Digite uma data (DD/MM/AAAA) ou "F" para encerrar o programa: ').strip().lower()
    if (data=='f'):
        print('==========PROGRAMA ENCERRADO==========')
        break
    dia=data[0]+data[1]
    dia=int(dia)
    mes=data[3]+data[4]
    mes=int(mes)
    ano=data[6]+data[7]+data[8]+data[9]
    ano=int(ano)
    if (mes<=0 or mes>=13):
        print('Mês inválido')
        print('==========PROGRAMA ENCERRADO==========')
    else:
        if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
            if (dia<=0 or dia>=32):
                print('Dia inválido')
            else:
                if (mes==1):
                    mes_texto='janeiro'
                elif (mes==3):
                    mes_texto='março'
                elif (mes==5):
                    mes_texto='maio'
                elif (mes==7):
                    mes_texto='julho'
                elif (mes==8):
                    mes_texto='agosto'
                elif (mes==10):
                    mes_texto='outubro'
                elif (mes==12):
                    mes_texto='dezembro'
        if (mes==4 or mes==6 or mes==9 or mes==11):
            if (dia<=0 or dia>=31):
                print('Dia inválido')
            else:
                if (mes==4):
                    mes_texto='abril'
                elif (mes==6):
                    mes_texto='junho'
                elif (mes==9):
                    mes_texto='setembro'
                elif (mes==11):
                    mes_texto='novembro'
        if (mes==2):
            if (dia<=0 or dia>=30):
                print('Dia inválido')
            if (dia==29):
                if(ano%4==0 and ano%100!=0) or ano%400==0:
                    mes_texto='fevereiro'
                else:
                    print('Ano não é bissexto')
    print('{}/{}/{}.'.format(dia, mes_texto, ano))

