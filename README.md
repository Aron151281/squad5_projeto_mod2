# Pesquisa Digital para Coleta e Armazenamento de Dados 

## Projeto SQUAD 5 Mod 2
![image](https://github.com/Aron151281/squad5_projeto_mod2/assets/132007858/93ab2550-9f13-47d8-8c42-e6953c4e42da)

### Descrição do projeto:
Uma escola de tecnologia nos contratou para desenvolver um aplicativo que avalia o nível de conhecimento dos candidatos em relação à linguagem Python. O objetivo é determinar o grau de conhecimento de cada candidato na linguagem, para que possamos indicar o curso mais adequado de acordo com seu nível de habilidade.

Atendendo a essa solicitação, criamos um questionário com respostas pré-definidas para coletar as informações necessárias. Os dados obtidos serão armazenados em um arquivo CSV para análise e tomada de decisões futuras.

Por meio desse aplicativo, os candidatos poderão responder às perguntas relacionadas à linguagem Python e seu conhecimento sobre ela. Com base nas respostas fornecidas, poderemos avaliar o nível de competência de cada candidato e recomendar o curso mais apropriado para aprimorar suas habilidades em Python.

O aplicativo armazenará as respostas em um arquivo CSV, o que permitirá que a escola de tecnologia analise os dados coletados e tome decisões informadas sobre o encaminhamento dos candidatos aos cursos adequados. Essa abordagem ajudará a garantir que cada candidato seja direcionado para um programa de estudos que corresponda ao seu nível de conhecimento e habilidades em Python.

Dessa forma, o aplicativo que desenvolvemos oferecerá um método eficaz para avaliar o conhecimento dos candidatos em Python e ajudará a escola a fornecer um direcionamento mais personalizado e eficiente para seus cursos.
### Funcionalidade: 
    Primeiro, as bibliotecas necessárias são importadas: csv para trabalhar com arquivos CSV e datetime para obter a data e hora atuais.

    A data e hora atuais são obtidas usando datetime.now(), e formatadas em strings nos formatos desejados para exibição.

    Com base na hora atual, uma saudação apropriada é determinada e armazenada na variável saudacao.

    Em seguida, as informações de data, hora e saudação são impressas na tela.

    O questionário começa, solicitando ao entrevistado que digite sua idade. O loop continuará até que a idade seja digitada como "00".

    Dentro do loop, o entrevistado é solicitado a fornecer seu nome idade e gênero. Em seguida, são feitas perguntas de múltipla escolha sobre Python.

    Após cada pergunta, é dada a opção de respostas pré determinadas: 'Sim', 'Não' e 'Não sei reponder', assim data e hora atuais são exibidas e as respostas são coletadas do entrevistado.

    Após a última pergunta, uma mensagem de agradecimento é exibida e os dados coletados são escritos em um arquivo CSV chamado "respostas.csv". Se o arquivo não existir, um cabeçalho é adicionado antes de escrever as respostas.

    O loop continua para o próximo entrevistado ou é interrompido se a idade digitada for "00".
### Reaproveitamento:
Para aproveitar o código com outras pesquisas, você pode seguir estas etapas:

    1. Analise as necessidades da nova pesquisa: Identifique as perguntas e informações que deseja coletar dos entrevistados.

    2. Modifique as perguntas existentes ou adicione novas perguntas: No código atual, existem cinco perguntas de múltipla escolha. Você pode ajustar ou substituir essas perguntas para se adequarem à sua nova pesquisa. Certifique-se de atualizar a forma como as respostas são exibidas e coletadas.

    3. Personalize o cabeçalho do arquivo CSV: O código atual tem um cabeçalho pré-definido para as colunas do arquivo CSV. Você pode modificar esse cabeçalho para se adequar às suas perguntas e dados específicos da nova pesquisa.

    4. Ajuste as mensagens e saudações: As mensagens de saudação, agradecimento e outras mensagens exibidas durante o questionário podem ser personalizadas para se adequarem à nova pesquisa.

    5. Salve as respostas em um novo arquivo CSV: Se você estiver conduzindo uma nova pesquisa, pode ser útil salvar as respostas em um arquivo CSV separado para cada pesquisa. Você pode modificar o código para criar um novo arquivo CSV com um nome único para cada pesquisa.

    6. Teste e valide o código: Certifique-se de testar o código com as novas perguntas e dados para garantir que tudo funcione corretamente. Verifique se as respostas estão sendo coletadas e salvadas corretamente no arquivo CSV.   
## Tecnologias utilizadas: 
VSCODE , PYTHON , CSV e EXCEL .
## Desenvolvedores e Contatos:
Aron Augusto Bernardo Silva
https://www.linkedin.com/in/aron-bernardo-data-analytics/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BaOogZpm6QwWvOj2DYO%2FCow%3D%3D

Jaqueline dos Santos Pinto da Cunha 
https://www.linkedin.com/in/jaqueline-cunha-01b6a1271/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BaOogZpm6QwWvOj2DYO%2FCow%3D%3D

Rafael César Pinto da Silva Andrade Lima 
https://www.linkedin.com/in/rafael-data-analyst/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BaOogZpm6QwWvOj2DYO%2FCow%3D%3D