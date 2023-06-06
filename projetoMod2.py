import csv
import datetime as dt

#obtem a data e hora atual
agora = dt.datetime.now()

#obtem o dia atual, com formato de saida especificado:
dia_atual = agora.strftime('%d/%m/%y')

#obtem a hora atual, com formato de saida especificado:
hora_atual = agora.strftime('%H:%M:%S')

#verifica o horario para determinar a saudação:
saudacao = ''
hora = agora.hour
''
# se a hora for maior ou igual  a 6 e menor que 12 , dizer bom dia :
if 6 <= hora < 12:
    saudacao = 'Bom dia entrevistado(a)!'

    # se a hora for maior ou igual a 12 e menor que 18 , dizer boa tarde:
elif 12 <= hora < 18 :
    saudacao ='Boa tarde entrevistado(a) !'

    # senao dizer boa noite:
else:
    saudacao = 'Boa noite entrevistado(a)!'

#exibe a data, hora e saudação
print('data:', dia_atual)
print('hora', hora_atual)
print(saudacao)

# questionario de multliplas escolhas que irá mostrar data e hora da resposta.
print(' Seja bem vindo(a) ao questionário Sobre Python ! ')

#salva as respostas em um arquivo csv
with open('respostas.csv', newline='') as file:
    reader = csv.reader(file)
    row1 = next(reader)
    if row1 == ['Data', 'Hora', 'Nome', 'Idade', 'Pronome', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Resposta 5']:
        print('engual')
    exit()
    writer = csv.writer(file)
    writer.writerow(['Data', 'Hora', 'Nome', 'Idade', 'Pronome', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Resposta 5'])
    idade_entrevistado = ''
    while idade_entrevistado != '00':
        idade_entrevistado = str(input('Digite sua idade : '))
        if idade_entrevistado == '00':
            break

        nome_entrevistado = str(input('Digite seu nome : '))

        pronome_entrevistado = str(input('Digite como você se identifica (gênero): '))


        resposta_1 = str(input('Você sabe o que seria Python?'
                            '\n[1-Sim]'
                            '\n[2-Não]'
                            '\n[3-Não sei responder]'
                            '\nR: '))

        resposta_2 = str(input('Você sabe utilizar alguma biblioteca do Python? Como Pandas, Numpy etc?'
                            '\n[1-Sim]'
                            '\n[2-Não]'
                            '\n[3-Não sei responder]'
                            '\nR: '))

        resposta_3 = str(input('Você sabe oque é um arquivo .csv? '
                            '\n[1-Sim]'
                            '\n[2-Não]'
                            '\n[3-Não sei responder]'
                            '\nR: '))

        resposta_4 = str(input('Você conseguiria criar um aplicativo mobile do zero?'
                            '\n[1-Sim]'
                            '\n[2-Não]'
                            '\n[3-Não sei responder]'
                            '\nR: '))

        resposta_5 = str(input('Você é bom no que faz?'
                            '\n[1-Sim]'
                            '\n[2-Não]'
                            '\n[3-Não sei responder]'
                            '\nR: '))

        print('\nPróximo entrevistado! digite 00 na idade para parar!\n')
        writer.writerow([idade_entrevistado, nome_entrevistado, pronome_entrevistado, resposta_1, resposta_2, resposta_3, resposta_4, resposta_5, dia_atual, hora_atual])


# Data,Hora,Nome,Idade,Pronome,Resposta 1,Resposta 2,Resposta 3,Resposta 4,Resposta 5
# 25,Rafael,M,1,1,1,2,1,06/06/23,16:24:40
# 33,Jesus,M,2,2,2,2,1,06/06/23,16:24:40
# 22,Bianca,F,1,2,1,2,1,06/06/23,16:24:40
# Babu,Babu,Babu,3,3,3,3,3,06/06/23,16:24:40
