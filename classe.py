import datetime as dt


class Saudacao():
    agora = dt.datetime.now()

    #obtem o dia atual, com formato de saida especificado:
    dia_atual = agora.strftime('%d/%m/%y')
    
    #obtem a hora atual, com formato de saida especificado:
    hora_atual = agora.strftime('%H:%M:%S')
    def bemvindo(self):
        agora = dt.datetime.now()
        hora = agora.hour
        # se a hora for maior ou igual  a 6 e menor que 12 , dizer bom dia :
        if 6 <= hora < 12:
            saudacao = 'Olá, bom dia entrevistado(a)!'
            # se a hora for maior ou igual a 12 e menor que 18 , dizer boa tarde:
        elif 12 <= hora < 18 :
            saudacao ='Olá, boa tarde entrevistado(a)!'
            # senao dizer boa noite:
        else:
            saudacao = 'Olá, boa noite entrevistado(a)!'

        return saudacao
msg_de_boasvindas = Saudacao()
print(msg_de_boasvindas.bemvindo())
