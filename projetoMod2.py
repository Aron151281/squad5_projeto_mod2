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
nome_entrevistado = str(input('Digite seu nome : '))
dia_atual = agora.strftime('%d/%m/%y')
hora_atual = agora.strftime('%H:%M:%S')
print('data:', dia_atual)
print('hora', hora_atual)

idade_entrevistado = str(input('Digite sua idade : '))
dia_atual = agora.strftime('%d/%m/%y')
hora_atual = agora.strftime('%H:%M:%S')
print('data:', dia_atual)
print('hora', hora_atual)

pronome_entrevistado = str(input('Digite como você se identifica (gênero): '))
dia_atual = agora.strftime('%d/%m/%y')
hora_atual = agora.strftime('%H:%M:%S')
print('data:', dia_atual)
print('hora', hora_atual)

resposta_1 = str(input('Você sabe o que seria Python?'
                       '\n[1-Sim]'
                       '\n[2-Não]'
                       '\n[3-Não sei responder]'
                       '\nR: '))
dia_atual = agora.strftime('%d/%m/%y')
hora_atual = agora.strftime('%H:%M:%S')
print('data:', dia_atual)
print('hora', hora_atual)

resposta_2 = str(input('Você sabe utilizar alguma biblioteca do Python? Como Pandas, Numpy etc?'
                       '\n[1-Sim]'
                       '\n[2-Não]'
                       '\n[3-Não sei responder]'
                       '\nR: '))
dia_atual = agora.strftime('%d/%m/%y')
hora_atual = agora.strftime('%H:%M:%S')
print('data:', dia_atual)
print('hora', hora_atual)

resposta_3 = str(input('Você sabe oque é um arquivo .csv? '
                       '\n[1-Sim]'
                       '\n[2-Não]'
                       '\n[3-Não sei responder]'
                       '\nR: '))
dia_atual = agora.strftime('%d/%m/%y')
hora_atual = agora.strftime('%H:%M:%S')
print('data:', dia_atual)
print('hora', hora_atual)

resposta_4 = str(input('Você conseguiria criar um aplicativo mobile do zero?'
                       '\n[1-Sim]'
                       '\n[2-Não]'
                       '\n[3-Não sei responder]'
                       '\nR: '))
dia_atual = agora.strftime('%d/%m/%y')
hora_atual = agora.strftime('%H:%M:%S')
print('data:', dia_atual)
print('hora', hora_atual)

resposta_5 = str(input('Você é bom no que faz?'
                       '\n[1-Sim]'
                       '\n[2-Não]'
                       '\n[3-Não sei responder]'
                       '\nR: '))

dia_atual = agora.strftime('%d/%m/%y')
hora_atual = agora.strftime('%H:%M:%S')
print('data:', dia_atual)
print('hora', hora_atual)

#salva as respostas em um arquivo csv
with open('respostas.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Data', 'Hora', 'Nome', 'Idade', 'Pronome', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Resposta 5'])
    writer.writerow([dia_atual, hora_atual, nome_entrevistado, idade_entrevistado, pronome_entrevistado, resposta_1, resposta_2, resposta_3, resposta_4, resposta_5])