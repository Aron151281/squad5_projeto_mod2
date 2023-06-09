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
    saudacao = 'Olá, bom dia entrevistado(a)!'

    # se a hora for maior ou igual a 12 e menor que 18 , dizer boa tarde:
elif 12 <= hora < 18 :
    saudacao ='Olá, boa tarde entrevistado(a)!'

    # senao dizer boa noite:
else:
    saudacao = 'Olá, boa noite entrevistado(a)!'

#exibe a data, hora e saudação
print('='*30,'\n')
print('Data:', dia_atual,'Hora', hora_atual)
print()
print(saudacao)

# questionario de multliplas escolhas que irá mostrar data e hora da resposta.
print('Seja bem vindo(a) ao questionário sobre a linguagem Python!')
print()

# pegar a primeira linha do .csv
primeiraLinha = open('respostas.csv')
reader = csv.reader(primeiraLinha)
row1 = next(reader)
primeiraLinha.close()

#salva as respostas em um arquivo csv

with open('respostas.csv','a', newline='') as file:
    
    # cria um cabeçalho se não tiver
    writer = csv.writer(file)
    
    if row1 != ['Nome', 'Idade', 'Gênero', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Resposta 5', 'Data', 'Hora']:
        writer.writerow(['Nome', 'Idade', 'Gênero', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Resposta 5', 'Data', 'Hora'])
    
    # cria um loop baseado na idade que para ao inserir a idade '00'
    idade_entrevistado = ''
    
    while idade_entrevistado != '00':
        
        idade_entrevistado = str(input('Digite sua idade : '))
        if idade_entrevistado == '00':
            break
        
        dia_atual = agora.strftime('%d/%m/%y')
        hora_atual = agora.strftime('%H:%M:%S')
        print('Data:', dia_atual,'Hora', hora_atual)       
        print('='*30,'\n')       
        
        nome_entrevistado = str(input('Digite seu nome : '))
        dia_atual = agora.strftime('%d/%m/%y')
        hora_atual = agora.strftime('%H:%M:%S')             
        print('Data:', dia_atual,'Hora', hora_atual)
        print('='*30,'\n')

        genero_entrevistado = str(input('Digite como você se identifica (gênero): '))     
        dia_atual = agora.strftime('%d/%m/%y')  
        hora_atual = agora.strftime('%H:%M:%S')
        print('Data:', dia_atual,'Hora', hora_atual)
        print('='*30,'\n')

        resposta_1 = str(input('Você sabe o que seria Python?'
                            '\n1 - Sim'
                            '\n2 - Não'
                            '\n3 - Não sei responder'
                            '\nR:  '))
        
        dia_atual = agora.strftime('%d/%m/%y')
        hora_atual = agora.strftime('%H:%M:%S')             
        print('Data:', dia_atual,'Hora', hora_atual)
        print('='*30,'\n')
                            
        resposta_2 = str(input('Você sabe utilizar alguma biblioteca do Python? Como Pandas, Numpy etc?' 
                            '\n1 - Sim'
                            '\n2 - Não'
                            '\n3 - Não sei responder'
                            '\nR:  '))
               
        dia_atual = agora.strftime('%d/%m/%y')
        hora_atual = agora.strftime('%H:%M:%S')
        print('Data:', dia_atual,'Hora', hora_atual)
        print('='*30,'\n')                                   

        resposta_3 = str(input('Você sabe oque é um arquivo .csv? '
                            '\n1 - Sim'
                            '\n2 - Não'
                            '\n3 - Não sei responder'
                            '\nR:  '))
                            
        dia_atual = agora.strftime('%d/%m/%y')  
        hora_atual = agora.strftime('%H:%M:%S')
        print('Data:', dia_atual,'Hora', hora_atual)
        print('='*30,'\n')
                                           
        resposta_4 = str(input('Você conseguiria criar um aplicativo mobile do zero?'
                            '\n1 - Sim'
                            '\n2 - Não'
                            '\n3 - Não sei responder'
                            '\nR:  '))
                            
        dia_atual = agora.strftime('%d/%m/%y')
        hora_atual = agora.strftime('%H:%M:%S')
        print('Data:', dia_atual,'Hora', hora_atual)
        print('='*30,'\n')
                                                   
        resposta_5 = str(input('Você é sabe o que são decoradores em Python e como eles podem ser usados?'
                            '\n1 - Sim'
                            '\n2 - Não'
                            '\n3 - Não sei responder'
                            '\nR:  '))
                            
        dia_atual = agora.strftime('%d/%m/%y')                      
        hora_atual = agora.strftime('%H:%M:%S')             
        print('Data:', dia_atual,'Hora', hora_atual)
        print()
        print('Muito obrigado(a) por participar da pesquisa!')
        print('='*45,'\n')
        print('\nPróximo entrevistado! Ou digite 00 na idade para parar!\n')
       
        
        writer.writerow([nome_entrevistado, idade_entrevistado, genero_entrevistado, resposta_1, resposta_2, resposta_3, resposta_4, resposta_5, dia_atual,hora_atual])
