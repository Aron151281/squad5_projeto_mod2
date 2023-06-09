import csv
import datetime as dt
from classe import Saudacao 

msg_de_boasvindas = Saudacao()

#obtem a data e hora atual
agora = dt.datetime.now()

#obtem o dia atual, com formato de saida especificado:
dia_atual = msg_de_boasvindas.dia_atual

#obtem a hora atual, com formato de saida especificado:
hora_atual = msg_de_boasvindas.hora_atual

#exibe a data, hora e saudação
print('='*30,'\n')
print('Data:', dia_atual,'Hora', hora_atual)
print()

msg_de_boasvindas = Saudacao()
print(msg_de_boasvindas.bemvindo())


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
    
    if row1 != ['Nome', 'Idade', 'Genero', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Resposta 5', 'Data', 'Hora']:
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
