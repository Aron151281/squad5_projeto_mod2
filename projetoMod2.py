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
    saudacao = 'bom dia entrevistado(a)!'

    # se a hora for maior ou igual a 12 e menor que 18 , dizer boa tarde:
elif 12 <= hora < 18 :
    saudacao ='boa tarde entrevistado(a) !'

    # senao dizer boa noite:
else:
    saudacao = 'boa noite entrevistado(a)!'
    
    #exibe a data, hora e saudacao 
print('data:', dia_atual)
print('hora', hora_atual)
print(saudacao)

# questionario de multliplss escolhas.
print(' Seja bem vindo(a) ao questionário Sobre Python ! ')
nome_entrevistado = str(input('Digite seu nome :'))
idade_entrevistado = str(input('Digite sua idade :'))
pronome_entrevistado = str(input('Digite como voçê se identifica (gênero):'))
resposta_1 = str(input('voçê sabe o que seria Python? [1-sim]  [2-não]  [3-não sei responder] ='))


