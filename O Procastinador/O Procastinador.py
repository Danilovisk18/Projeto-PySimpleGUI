#projeto mini game
import PySimpleGUI as sg
#Importando random para tirar a sorte num "dado"
import random
def Ato01():
    #variáveis de hora e localização
    horas = 17
    minutos = 0
    loc = 'Portão'
    tempo_de_espera = 0
    tempo_de_espera_total_do_pagamento_via_pix_no_RU = 0
    #Cara ou coroa(teste de sorte)
    numero_da_sorte = 5
    #Dinheiro físico
    dinheiro = 2.00
    #Placar do pedra, papel e tesoura
    Arthur_placar = 0
    Pc_placar = 0
    #A "escolha" do pc no pedra papel e tesoura
    Pc_escolha = 0
    #Lista que contém as respostas
    lista_de_respostas = ['Questão 01:??????','Questão 02:??????','Questão 03:??????','Questão 04:??????','Questão 05:??????']
    #Variáveis das respostas começam falsas, mas quando se torna verdadeira o gabarito recebe um update para exibir a resposta
    Sabe_resposta1 = False
    Sabe_resposta2 = False
    Sabe_resposta3 = False
    Sabe_resposta4 = False
    Sabe_resposta5 = False
    #Variáveis para verificar se uma ação já foi feita
    Comprou_resposta = False
    Vasculhou_ao_redor_RU = False
    Falou_com_pessoa_RU = False
    Jantou_no_RU = False
    Achou_papel_amassado = False
    Falou_pela_primeira_vez = True
    Falou_pela_primeira_vez_bilioteca = True
    Falou_pela_primeira_vez_pavilhao = True
    Leu_livro = False
    Livro_util = False
    Ajudou_pessoa_na_biblioteca = False
    Questoes_certas = 0
    #Variável para contar quantas questões foram acertadas na prova
    Pontos_prova = 0
    #Janela do Game over
    Game_over1 = [
         [sg.Text('GAME OVER',font=('Comic Sans MS',30),key='-TEXTO_EM_DESTAQUE-')],
         [sg.Text('',visible=False,key='-TEXTO_FINAL-',font=('Comic Sans MS',15))],
         [sg.Image(filename=r'',key='-IMAGEM-')],
         [sg.Button('Sair',key='-GAME_OVER-')]
    ]
    #Mapa/Pausa
    Mapa = [
        [sg.Column([[sg.Text(f'Relógio: {horas}:0{minutos}',key='-HORAS-',font=('Comic Sans MS',15)),
                     sg.Text(f'Dinheiro: {dinheiro:.2f}R$',font=('Comic Sans MS',15),key='-DINHEIRO-')]],justification='Left'),
        sg.Button('Fechar',key='-FECHAR-')],
    [
        sg.Column([
            [sg.Image(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\mapa.png', key='-MAPA_PORTAO-', visible=True, size=(845, 468))],
            [sg.Image(filename=r'',visible=False)]
        ], element_justification='center'),
    #Lista de resposta que podemos clicar no menu de pausa
        sg.Column([
            [sg.Button(item,font=('Comic Sans MS',15),key=str(i))] for i, item in enumerate(lista_de_respostas)
        ], justification='left')]
    ]
    #As respostas são exibidas em um menu diferente dependendo de qual opção foi clicada ela será atualizada para a tal
    Respostas = [
        [sg.Button('Voltar',key='-FECHAR_PAUSA_QUANDO_NÃO_SOUBER_A_RESPOSTA-')],
        #Respostas serão atualizadas quando as variáveis Saber_resposta forem verdadeiras
        [sg.Image(filename=r'',key='-ARTHUR_NÃO_SABE_A_1-')],
        [sg.Text('Arthur',key='-ARTHUR_NOME-',font=('Helvetica',17))],
        [sg.Text('',key='-TEXTO_QUANDO_NÃO_SABE_A_RESPOSTA-',font=('Arial',13))],
    ]
    #Mini game pedra, papel e tesoura
    Pedra_papel_tesoura = [
         [sg.Text('',key='-TITULO_DO_PEDRA_PAPEL_TESOURA-',font=('Comic Sans MS',24))],
         [sg.Text('',key='-RESULTADO_DA_JOGADA-',font=('Comic Sans MS',18))],
         [sg.Text('',key='-PLACAR_ARTHUR-',font=('Comic Sans MS',18)),sg.Text('',key='-PLACAR_PC-',font=('Comic Sans MS',18))],
         [sg.Image(filename=r'',key='-ESCOLHA_DO_ARTHUR-'),sg.Image(filename=r'',key='-PC-')],
         [sg.Button('Pedra',key='-PEDRA-'),sg.Button('Papel',key='-PAPEL-'),sg.Button('Tesoura',key='-TESOURA-'),sg.Button('Finalizar',key='-VITORIA-',visible=False),sg.Button('Finalizar',key='-DERROTA-',visible=False)]
    ]    
    #Jogo completo em uma janela fixa, os valores vão se alterando com o método Update
    jogo_completo = [
        #Relógio e botão para abrir o mapa
        [sg.Column([[sg.Text(f'Relógio: {horas}:0{minutos}',key='-HORAS-',font=('Comic Sans MS',15),visible=False)]],justification='Left')],
        [sg.Column([[sg.Button('Abrir mapa',visible=False,font=('Comic Sans MS',15),pad=(0, 20),key='-ABRIR_MAPA_NO_RU1-'),
                     sg.Button('Resposta',visible=False,font=('Comic Sans MS',15),pad=(0, 20),key='-RESPOSTA_DO_LIVRO-'),]],justification='right')],

        #A imagem dos personagens ou da situação
        [sg.Column([[sg.Image(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur1.PNG',key='-ARTHUR1-',visible=False),
        sg.Image(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\ato1iIntro.png',key='-INTRO-'),
        sg.Image(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\esperandobage.png',key='-IMAGEM-',visible=False)]],justification='center',element_justification='center'),
        ],

        #Escolhas no mapa enquanto está no portão
        [sg.Column([[sg.Button('Ir para o RU(pegar o Bagé)',key='-ESCOLHER_RU_DO_PORTAO-',font=('Comic Sans MS',10),visible=False),sg.Button('Ir para o RU(pegar o Bagé)',key='-ESCOLHER_RU_DO_PORTAO2-',font=('Comic Sans MS',10),visible=False),sg.Button('Caminhar até o Pavilhão',key='-ESCOLHER_PAVILHAO_DO_PORTAO-',font=('Comic Sans MS',10),visible=False),sg.Button('Ir para a Biblioteca(Pegar o bagé)',key='-ESCOLHER_BIBLIOTECA_DO_PORTAO-',font=('Comic Sans MS',10),visible=False)]],justification='center',element_justification='center')],

        #Mapa da Ufra (muda conforme a localização)
        [sg.Image(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\mapa.png',key='-MAPA_PORTAO-',visible=False,size=(845,468))],

        #O nome dos personagens
        [sg.Column([[sg.Text('Arthur',key='-ARTHUR_NOME-',font=('Helvetica',17),visible=False),
        sg.Text('Narrador',key='-NARRADOR-',font=('Comic Sans MS',17),visible=False),
        sg.Text('Atendente',visible=False,key='-ATENDENTE(RU)-',font=('Helvetica',17)),
        sg.Text('Kayla',visible=False,key='-Kayla-',font=('Impact',17),text_color='#800080'),
        sg.Text('Aluno 01',key='-ALUNO_RU1-',font=('Helvetica',17),visible=False),
        sg.Text('Aluno 02',key='-ALUNO_RU2-',font=('Helvetica',17),visible=False),
        sg.Text('Aluno 03',key='-ALUNO_BIBLIOTECA-',font=('Helvetica',17),visible=False),
        sg.Text('Aluno',key='-ALUNO_PAVILHAO-',font=('Helvetica',17),visible=False),]],justification='center',element_justification='center')],


        #O texto falado pelos personagens
        [sg.Column([[sg.Text('Consegui chegar cedo dessa vez, parece que não há muito movimento por aqui',key='-CAIXA_DE_TEXTO1-',font=('Arial',13),visible=False)]]
        ,justification='center',element_justification='center')],

        #Os botões que vão permitir os eventos, eles estão abaixo do nome e da caixa de texto
        #Botões iniciais quando está no portão
        [sg.Button('Prosseguir',font=('Courier'),key='-PROSSEGUIR-'),
        sg.Column([[sg.Button('Prosseguir >>',key='-PROSSEGUIR1-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Prosseguir >>',key='-PROSSEGUIR2-',font=('Comic Sans MS',10),visible=False),

        #Botões quando se escolhe pavilhão
        sg.Button('Andar para o pavilhão',key='-ESCOLHER_PAVILHAO_DO_PORTAO-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Prossegui>>',key='-PAVILHAO-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Prossegui>>',key='-PAVILHAO2-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Conversar com pessoa',key='-FALAR_COM_PESSOA_PAVILHAO-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Prosseguir>>',key='-FALAR_COM_PESSOA_PAVILHAO2-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Começar a prova',key='-INICIAR_PROVA-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Pegar bagé',key='-PEGAR_BAGE_NO_PAVILHAO-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Negócio fechado',key='-COMPRAR_RESPOSTA-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Nada feito',key='-NAO_COMPRAR_RESPOSTA-',font=('Comic Sans MS',10),visible=False),
        #Prova leva para o fim do jogo e dependendo do resultado o jogador vence ou perde
        sg.Button('Confirmar',key='-CONFIRMAR_PROVA-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Prosseguir',key='-CONFIRMAR_PROVA2-',font=('Comic Sans MS',10),visible=False),
        #Questões da prova
        #Questão 01
        sg.Button('a)',key='-PROVA_1_A-',font=('Comic Sans MS',10),visible=False),
        sg.Button('b)',key='-PROVA_1_B-',font=('Comic Sans MS',10),visible=False),
        sg.Button('c)',key='-PROVA_1_C-',font=('Comic Sans MS',10),visible=False),
        sg.Button('d)',key='-PROVA_1_D-',font=('Comic Sans MS',10),visible=False),
        #Questão 02
        sg.Button('a) Byte',key='-PROVA_2_A-',font=('Comic Sans MS',10),visible=False),
        sg.Button('b) Bit',key='-PROVA_2_B-',font=('Comic Sans MS',10),visible=False),
        sg.Button('c) Palavra',key='-PROVA_2_C-',font=('Comic Sans MS',10),visible=False),
        sg.Button('d) Célula de memória',key='-PROVA_2_D-',font=('Comic Sans MS',10),visible=False),
        #Questão 03
        sg.Button('a) 48.384',key='-PROVA_3_A-',font=('Comic Sans MS',10),visible=False),
        sg.Button('b) 56.004',key='-PROVA_3_B-',font=('Comic Sans MS',10),visible=False),
        sg.Button('c) 56.480',key='-PROVA_3_C-',font=('Comic Sans MS',10),visible=False),
        sg.Button('d) 56.064',key='-PROVA_3_D-',font=('Comic Sans MS',10),visible=False),
        #Questão 04
        sg.Button('a) 355',key='-PROVA_4_A-',font=('Comic Sans MS',10),visible=False),
        sg.Button('b) 300',key='-PROVA_4_B-',font=('Comic Sans MS',10),visible=False),
        sg.Button('c) 454',key='-PROVA_4_C-',font=('Comic Sans MS',10),visible=False),
        sg.Button('d) 104',key='-PROVA_4_D-',font=('Comic Sans MS',10),visible=False),
        #Questão 05
        sg.Button('a) 33 bits',key='-PROVA_5_A-',font=('Comic Sans MS',10),visible=False),
        sg.Button('b) 32 bits',key='-PROVA_5_B-',font=('Comic Sans MS',10),visible=False),
        sg.Button('c) 64 bits',key='-PROVA_5_C-',font=('Comic Sans MS',10),visible=False),
        sg.Button('d) 128 bits',key='-PROVA_5_D-',font=('Comic Sans MS',10),visible=False),
        #Botão para finalizar prova e mostrar resultado
        sg.Button('Resultado',key='-FINALIZAR-',font=('Comic Sans MS',10),visible=False),
        #Botões quando se escolhe ir para a biblioteca a partir do portão e demais ações da biblioteca
        sg.Button('Continuar para a biblioteca',key='-CONFIRMAR_IDA_PARA_A_BIBLIOTECA-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Continuar para a biblioteca',key='-ESPERAR_NO_PORTAO_BIBLIOTECA-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Confirmar(teste sua sorte)',key='-CONFIRMAR_IDA_PARA_A_BIBLIOTECA-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Continuar para a biblioteca',key='-VIAJAR_PARA_A_BIBLIOTECA-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Ir para o RU',key='-CAMINHAR_DA_BIBLIOTECA_PARA_RU-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Pegar bagé',key='-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Sair',key='-SAIR_DA_BIBLIOTECA-',font=('Comic Sans MS',10),visible=False),  
        sg.Button('Fala com uma pessoa',key='-FALAR_COM_PESSOA-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Prosseguir>>',key='-FALAR_COM_PESSOA2-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Prosseguir>>',key='-FALAR_COM_PESSOA3-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Ler um livro(testar sorte)',key='-LER_LIVRO-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Prosseguir>>',key='-AJUDAR2-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Prosseguir>>',key='-AJUDAR3-',font=('Comic Sans MS',10),visible=False),
        #Questões quando o livro é lido com sucesso
        sg.Button('c) 56.064',key='-QUESTAO_1_C1-',font=('Comic Sans MS',10),visible=False),
        sg.Button('a) 32 bits',key='-QUESTAO_2_A1-',font=('Comic Sans MS',10),visible=False),
        sg.Button('c) 7',key='-QUESTAO_3_C1-',font=('Comic Sans MS',10),visible=False),
        sg.Button('d) 9 e 31',key='-QUESTAO_4_D1-',font=('Comic Sans MS',10),visible=False),
        sg.Button('a) 3C',key='-QUESTAO_5_A1-',font=('Comic Sans MS',10),visible=False),
        #Questão 1 da pessoa da biblioteca
        sg.Button('a) 56.004',key='-QUESTAO_1_A-',font=('Comic Sans MS',10),visible=False),
        sg.Button('b) 48.384',key='-QUESTAO_1_B-',font=('Comic Sans MS',10),visible=False),
        sg.Button('c) 56.064',key='-QUESTAO_1_C-',font=('Comic Sans MS',10),visible=False),
        sg.Button('d) 52.480',key='-QUESTAO_1_D-',font=('Comic Sans MS',10),visible=False),
        #Questão 2 da pessoa da biblioteca
        sg.Button('a) 32 bits',key='-QUESTAO_2_A-',font=('Comic Sans MS',10),visible=False),
        sg.Button('b) 64 bits',key='-QUESTAO_2_B-',font=('Comic Sans MS',10),visible=False),
        sg.Button('c) 128 bits',key='-QUESTAO_2_C-',font=('Comic Sans MS',10),visible=False),
        sg.Button('d) 256 bits',key='-QUESTAO_2_D-',font=('Comic Sans MS',10),visible=False),
        #Questão 3 da pessoa da biblioteca
        sg.Button('a) 1',key='-QUESTAO_3_A-',font=('Comic Sans MS',10),visible=False),
        sg.Button('b) 9',key='-QUESTAO_3_B-',font=('Comic Sans MS',10),visible=False),
        sg.Button('c) 7',key='-QUESTAO_3_C-',font=('Comic Sans MS',10),visible=False),
        sg.Button('d) 7.3',key='-QUESTAO_3_D-',font=('Comic Sans MS',10),visible=False),
        #Questão 4 da pessoa da biblioteca
        sg.Button('a) 31 e 9',key='-QUESTAO_4_A-',font=('Comic Sans MS',10),visible=False),
        sg.Button('b) 6 e 26',key='-QUESTAO_4_B-',font=('Comic Sans MS',10),visible=False),
        sg.Button('c) 6 e 31',key='-QUESTAO_4_C-',font=('Comic Sans MS',10),visible=False),
        sg.Button('d) 9 e 31',key='-QUESTAO_4_D-',font=('Comic Sans MS',10),visible=False),
        #Questão 4 da pessoa da biblioteca
        sg.Button('a) 3C',key='-QUESTAO_5_A-',font=('Comic Sans MS',10),visible=False),
        sg.Button('b) DB00',key='-QUESTAO_5_B-',font=('Comic Sans MS',10),visible=False),
        sg.Button('c) 3F',key='-QUESTAO_5_C-',font=('Comic Sans MS',10),visible=False),
        sg.Button('d) A1',key='-QUESTAO_5_D-',font=('Comic Sans MS',10),visible=False),
        #Botão quando Arthur respondeu corretamente na biblioteca
        sg.Button('Prosseguir>>',key='-SUCESSO-',font=('Comic Sans MS',10),visible=False),
        #Arthur falhou o quiz
        sg.Button('Prosseguir>>',key='-FALHA-',font=('Comic Sans MS',10),visible=False),

        #Botões quando se escolhe o RU em ordem cronológica
        sg.Button('Cancelar',key='-CANCELAR_DO_PORTAO_PRO_RU-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Prosseguir para o RU',key='-CONFIRMAR_IDA_PRO_RU-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Esperar Bagé(teste sua sorte)',key='-ESPERAR_NO_PORTAO-',font=('Comic Sans MS',10),visible=False),
        sg.Button('Viajar até o Ru',visible=False,key='-VIAJAR_NO_BAGÉ_DO_PORTAO_PARA_O_RU-'),
        sg.Button('Prossegui>>',key='-PROXIMA_ACAO_DO_PORTAO_PARA_RU-',visible=False),
        sg.Button('Prossegui>>',key='-PROXIMA_ACAO_DO_PORTAO_PARA_RU2-',visible=False),
        sg.Button('Prossegui>>',key='-PROXIMA_ACAO_DO_PORTAO_PARA_RU3-',visible=False),
        sg.Button('Prossegui>>',key='-PROXIMA_ACAO_DO_PORTAO_PARA_RU4-',visible=False),
        sg.Button('Prossegui>>',key='-PROXIMA_ACAO_DO_PORTAO_PARA_RU5-',visible=False),
        sg.Button('Conversar com uma pessoa',key='-ABORDAR_PESSOA_NA_PARADA-',visible=False),
        sg.Button('Prossegui>>',key='-ABORDAR_PESSOA_NA_PARADA2-',visible=False),
        sg.Button('Prossegui>>',key='-ABORDAR_PESSOA_NA_PARADA3-',visible=False),
        sg.Button('Prossegui>>',key='-ABORDAR_PESSOA_NA_PARADA4-',visible=False),
        sg.Button('Prossegui>>',key='-ABORDAR_PESSOA_NA_PARADA5-',visible=False),
        sg.Button('Prossegui>>',key='-ABORDAR_PESSOA_NA_PARADA6-',visible=False),
        sg.Button('Pagar janta',key='-PAGAR_A_JANTA_DA_KAYLA-',visible=False),
        sg.Button('Não tenho dinheiro',key='-NAO_PAGAR_JANTA_DA_KAYLA-',visible=False),
        sg.Button('Comprar janta',key='-COMPRAR_JANTA-',visible=False),
        sg.Button('Procurar resposta ao redor',key='-VASCULHAR_AO_REDOR-',visible=False),
        sg.Button('Voltar',key='-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-',visible=False),
        sg.Button('Voltar',key='-VOLTAR_SEM_VASCULHAR_AO_REDOR-',visible=False),
        sg.Button('Prosseguir>>',key='-COMPRAR_JANTA2-',visible=False),
        sg.Button('Cancelar',key='-CANCELAR_JANTA2-',visible=False),
        sg.Button('Esperar na fila(teste sua sorte)',key='-COMPRAR_JANTA3-',visible=False),
        sg.Button('Prosseguir>>',key='-COMPRAR_JANTA4-',visible=False),
        sg.Button('Prosseguir>>',key='-COMPRAR_JANTA5-',visible=False),
        sg.Button('Prosseguir>>',key='-COMPRAR_JANTA6-',visible=False),
        sg.Button('Prosseguir>>',key='-COMPRAR_JANTA7-',visible=False),
        sg.Button('Prosseguir>>',key='-COMPRAR_JANTA8-',visible=False),
        sg.Button('Prosseguir>>',key='-COMPRAR_JANTA9-',visible=False),
        sg.Button('Prosseguir>>',key='-COMPRAR_JANTA10-',visible=False),
        sg.Button('Prosseguir>>',key='-COMPRAR_JANTA11-',visible=False),
        sg.Button('Prosseguir>>',key='-COMPRAR_JANTA12-',visible=False),
        sg.Button('Mostra papel amassado',key='-MOSTRAR_PAPEL_AMASSADO_RU-',visible=False),
        sg.Button('Jogar pedra papel e tesoura no RU',key='-JOGAR_PEDRA_PAPEL_TESOURA_CONTRA_PESSOA_NO_RU-',visible=False),
        sg.Button('Começar',key='-COMEÇAR_PEDRA_PAPEL_TESOURA-',visible=False),
        sg.Button('Prosseguir>>',key='-GANHOU_PEDRA_PAPEL_TESOURA-',visible=False),
        sg.Button('Prosseguir>>',key='-GANHOU_PEDRA_PAPEL_TESOURA2-',visible=False),
        sg.Button('Prosseguir>>',key='-PERDEU_PEDRA_PAPEL_TESOURA-',visible=False),
        sg.Button('Prosseguir>>',key='-PERDEU_PEDRA_PAPEL_TESOURA2-',visible=False),
        sg.Button('Pedir respostas',key='-PEDIR_RESPOSTA_PARA_PESSOAS_NO_RU-',visible=False),
        sg.Button('Próximo>>',key='-MOSTRAR_PAPEL_RU2-',visible=False),
        sg.Button('Próximo>>',key='-MOSTRAR_PAPEL_RU3-',visible=False),
        sg.Button('Próximo>>',key='-PEDIR_RESPOSTA_PARA_PESSOAS_NO_RU2-',visible=False),
        sg.Button('Pagar no pix(teste sua sorte)',key='-PAGAR_JANTA_NO_PIX-',visible=False),
        sg.Button('Pagar janta no dinheiro',key='-PAGAR_JANTA_NO_DINHEIRO-',visible=False),
        sg.Button('Ir embora',key='-IR_EMBORA_DO_PAGAMENTO_DA_JANTA-',visible=False),
        sg.Button('Falar com os alunos',key='-FALAR_COM_ALUNOS_RU-',visible=False),
        sg.Button('Terminar a janta(não falar com eles)',key='-NAO_FALAR_COM_ALUNOS_RU-',visible=False),
        #Usuário decide ir para o pavilhão da biblioteca ou do RU
        sg.Button('Ir para o pavilhão',key='-VIAJAR_DO_RU_OU_BIBLIOTECA-',visible=False),]],justification='center',element_justification='center'),
        

        ],
        [sg.Column([[sg.Button('Ir para a biblioteca',key='-IR_PARA_BIBLIOTECA_DO_RU-',visible=False),
         sg.Button('Pegar o bagé',key='-PEGAR_O_BAGÉ_DO_RU-',visible=False),
         #Botões da biblioteca
         sg.Button('Entrar na biblioteca',key='-ENTRAR_NA_BIBLIOTECA-',visible=False),
         sg.Button('Ajudar',key='-AJUDAR-',font=('Comic Sans MS',10),visible=False),]]
        ,justification='center',element_justification='center')],

    ]
    jogo = sg.Window('O procastinador',jogo_completo,location=(400,0),finalize=True)
    Pausa = sg.Window('Mapinha',Mapa,finalize=True)
    Ver_respostas = sg.Window('Gabarito',Respostas,finalize=True,element_justification='center',location=(400,0))
    Game_over = sg.Window('Game over',Game_over1,finalize=True,element_justification='center',location=(400,0))
    Pedra_papel_tesoura_completo = sg.Window('Pedra, papel e tesoura',Pedra_papel_tesoura,finalize=True,element_justification='center',location=(400,0))
    Pedra_papel_tesoura_completo.hide()
    Game_over.hide()
    Pausa.hide()
    Ver_respostas.hide()
    while True:
        evento,valor = jogo.read(timeout=100)
        pausa1,pausa2 = Pausa.read(timeout=100)
        Resposta1,Resposta2 = Ver_respostas.read(timeout=100)
        over1,over2 = Game_over.read(timeout=100)
        pedra1,pedra2 = Pedra_papel_tesoura_completo.read(timeout=100)
        #A janela fixa vai mudando os valores conforme as escolhas
        #Atualiza a primeira caixa de texto
        #Estrutura condicional para fechar a janela encerrando o ciclo
        if evento == sg.WIN_CLOSED or over1 == '-GAME_OVER-' or pausa1 == sg.WIN_CLOSED or pedra1 == sg.WIN_CLOSED or over1 == sg.WIN_CLOSED or Resposta1 == sg.WIN_CLOSED:
            break
        #Pausa o jogo para abrir o mapa
        if evento == '-ABRIR_MAPA_NO_RU1-':
              jogo.hide()
              Pausa.un_hide()
        #Fecha o menu de pausa e volta para o jogo
        if pausa1 == '-FECHAR-':
                jogo.un_hide()
                Pausa.hide()
        #Visualiza uma resposta do Gabarito
        #Respostas erradas
        if pausa1 == str(0) and Sabe_resposta1 == False:
              Ver_respostas['-ARTHUR_NÃO_SABE_A_1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur1.PNG')
              Ver_respostas['-TEXTO_QUANDO_NÃO_SABE_A_RESPOSTA-'].update('Eu não sei a resposta da primeira!')
              Pausa.hide()
              Ver_respostas.un_hide()
        if pausa1 == str(1) and Sabe_resposta2 == False:
              Ver_respostas['-ARTHUR_NÃO_SABE_A_1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG')
              Ver_respostas['-TEXTO_QUANDO_NÃO_SABE_A_RESPOSTA-'].update('Talvez eu devesse procurar por aí...')
              Pausa.hide()
              Ver_respostas.un_hide()
        if pausa1 == str(2) and Sabe_resposta3 == False:
              Ver_respostas['-ARTHUR_NÃO_SABE_A_1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG')
              Ver_respostas['-TEXTO_QUANDO_NÃO_SABE_A_RESPOSTA-'].update('Devo explorar pela UFRA e encontrar respostas...')
              Pausa.hide()
              Ver_respostas.un_hide()
        if pausa1 == str(3) and Sabe_resposta4 == False:
              Ver_respostas['-ARTHUR_NÃO_SABE_A_1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG')
              Ver_respostas['-TEXTO_QUANDO_NÃO_SABE_A_RESPOSTA-'].update('Imagino qual seja a resposta da quarta questão')
              Pausa.hide()
              Ver_respostas.un_hide()
        if pausa1 == str(4) and Sabe_resposta5 == False:
              Ver_respostas['-ARTHUR_NÃO_SABE_A_1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur2.PNG')
              Ver_respostas['-TEXTO_QUANDO_NÃO_SABE_A_RESPOSTA-'].update('Suspeito que kayla saiba essa')
              Pausa.hide()
              Ver_respostas.un_hide()
        #Respostas certas
        if pausa1 == str(0) and Sabe_resposta1 == True:
              Ver_respostas['-ARTHUR_NÃO_SABE_A_1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur2.PNG')
              Ver_respostas['-TEXTO_QUANDO_NÃO_SABE_A_RESPOSTA-'].update('A resposta da primeira é a letra B')
              Pausa.hide()
              Ver_respostas.un_hide()
        if pausa1 == str(1) and Sabe_resposta2 == True:
              Ver_respostas['-ARTHUR_NÃO_SABE_A_1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur2.PNG')
              Ver_respostas['-TEXTO_QUANDO_NÃO_SABE_A_RESPOSTA-'].update('A resposta da segunda é a letra D')
              Pausa.hide()
              Ver_respostas.un_hide()
        if pausa1 == str(2) and Sabe_resposta3 == True:
              Ver_respostas['-ARTHUR_NÃO_SABE_A_1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur2.PNG')
              Ver_respostas['-TEXTO_QUANDO_NÃO_SABE_A_RESPOSTA-'].update('A terceira é a letra D')
              Pausa.hide()
              Ver_respostas.un_hide()
        if pausa1 == str(3) and Sabe_resposta4 == True:
              Ver_respostas['-ARTHUR_NÃO_SABE_A_1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG')
              Ver_respostas['-TEXTO_QUANDO_NÃO_SABE_A_RESPOSTA-'].update('De acondo com o que me disseram é a letra C')
              Pausa.hide()
              Ver_respostas.un_hide()
        if pausa1 == str(4) and Sabe_resposta5 == True:
              Ver_respostas['-ARTHUR_NÃO_SABE_A_1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur2.PNG')
              Ver_respostas['-TEXTO_QUANDO_NÃO_SABE_A_RESPOSTA-'].update('De acordo com o que ela me disse, a resposta da 5 é a letra a)')
              Pausa.hide()
              Ver_respostas.un_hide()
        #Fechar gabarito e exibir o menu de pausa de novo
        #Atualizar relógio
        if minutos >= 60:
             minutos = 0
             horas += 1
             Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
        if Resposta1 == '-FECHAR_PAUSA_QUANDO_NÃO_SOUBER_A_RESPOSTA-':
              Ver_respostas.hide()
              Pausa.un_hide()
        #Game over quando o tempo acaba
        if minutos >= 30 and horas == 18:
             jogo.hide()
             Game_over.un_hide()
             Game_over['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Imagem_derrota.png')
             Game_over['-TEXTO_EM_DESTAQUE-'].update('ESSA NÃO!! DERROTA!')
             Game_over['-TEXTO_FINAL-'].update(f'Seu tempo acabou e você perdeu a prova!',visible=True)
             Game_over['-GAME_OVER-'].update('Finalizar')            
        #Após o menu ser fechado se inicia o jogo
        if evento == '-PROSSEGUIR-':
                jogo['-PROSSEGUIR-'].update(visible=False)
                jogo['-INTRO-'].update(visible=False)
                jogo['-PROSSEGUIR1-'].update(visible=True)
                jogo['-ARTHUR1-'].update(visible=True)
                jogo['-CAIXA_DE_TEXTO1-'].update(visible=True)

        #Fecha a introdução e o Arthur aparece
        if evento == '-PROSSEGUIR1-':               
                jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur2.PNG')
                jogo['-CAIXA_DE_TEXTO1-'].update('Preciso escolher para onde ir, mas tenho que gerenciar o meu tempo...',font=('Arial',13))
                jogo['-PROSSEGUIR1-'].update(visible=False)
                jogo['-PROSSEGUIR2-'].update(visible=True)

        #Abre o mapa depois da segunda caixa de Texto
        if evento == '-PROSSEGUIR2-':
                jogo['-CONFIRMAR_IDA_PRO_RU-'].update(visible=False)
                jogo['-PAVILHAO-'].update(visible=False)
                jogo['-CONFIRMAR_IDA_PARA_A_BIBLIOTECA-'].update(visible=False)
                jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur2.PNG')
                jogo['-CAIXA_DE_TEXTO1-'].update(visible=False)
                jogo['-CONFIRMAR_IDA_PRO_RU-'].update(visible=False)
                jogo['-PROSSEGUIR2-'].update('Cancelar',visible=False)
                jogo['-ARTHUR_NOME-'].update(visible=False)
                jogo['-ESCOLHER_RU_DO_PORTAO-'].update(visible=True)
                jogo['-ESCOLHER_PAVILHAO_DO_PORTAO-'].update(visible=True)
                jogo['-ESCOLHER_BIBLIOTECA_DO_PORTAO-'].update(visible=True)
                jogo['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\mapa.png',visible=True)
        #Usuário decide ir para o pavilhão e aparece as opções
        if evento == '-ESCOLHER_PAVILHAO_DO_PORTAO-':
                jogo['-ESCOLHER_RU_DO_PORTAO-'].update(visible=False)
                jogo['-ESCOLHER_PAVILHAO_DO_PORTAO-'].update(visible=False)
                jogo['-ESCOLHER_BIBLIOTECA_DO_PORTAO-'].update(visible=False)
                jogo['-MAPA_PORTAO-'].update(filename='')
                jogo['-PROSSEGUIR2-'].update(visible=True)
                jogo['-PAVILHAO-'].update(visible=True)
                jogo['-ARTHUR_NOME-'].update(visible=True)
                jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG')
                jogo['-CAIXA_DE_TEXTO1-'].update('Direto para o bicho papão...', visible=True)
        if evento == '-PAVILHAO-':
               minutos += 2
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\caminha_para_pavilhao.png',visible=True)
               jogo['-PAVILHAO-'].update(visible=False)
               jogo['-PAVILHAO2-'].update(visible=True)
               jogo['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
               Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
               jogo['-PROSSEGUIR2-'].update(visible=False)
               jogo['-ARTHUR_NOME-'].update(visible=False)
               jogo['-ARTHUR1-'].update(visible=False)
               jogo['-NARRADOR-'].update(visible=True)
               jogo['-CAIXA_DE_TEXTO1-'].update('Arthur caminha para o pavilhão')
        #Chegando no pavilhão aparecem algumas decisões
        if evento == '-PAVILHAO2-' and Comprou_resposta == False:
               Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_pavilhao.png')
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Imagem_no_pavilhao.png',visible=True)
               jogo['-ARTHUR_NOME-'].update(visible=False)
               jogo['-ARTHUR1-'].update(visible=False)
               jogo['-CONFIRMAR_PROVA-'].update(visible=False)
               jogo['-ABRIR_MAPA_NO_RU1-'].update(visible=True)
               jogo['-NARRADOR-'].update(visible=True)
               jogo['-ALUNO_PAVILHAO-'].update(visible=False)
               jogo['-ESPERAR_NO_PORTAO_BIBLIOTECA-'].update(visible=False)
               jogo['-ESPERAR_NO_PORTAO-'].update(visible=False)
               jogo['-PAVILHAO2-'].update(visible=False)
               jogo['-FALAR_COM_PESSOA_PAVILHAO-'].update(visible=True)
               jogo['-INICIAR_PROVA-'].update(visible=True)
               jogo['-PEGAR_BAGE_NO_PAVILHAO-'].update(visible=True)
               jogo['-CAIXA_DE_TEXTO1-'].update('No pavilhão, Arthur precisa decidir o que fazer')
        #Quando Arthur compra a resposta a opção de falar com a pessoa some
        if evento == '-PAVILHAO2-' and Comprou_resposta == True:
               Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_pavilhao.png')
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Imagem_no_pavilhao.png',visible=True)
               jogo['-ARTHUR_NOME-'].update(visible=False)
               jogo['-ARTHUR1-'].update(visible=False)
               jogo['-CONFIRMAR_PROVA-'].update(visible=False)
               jogo['-ABRIR_MAPA_NO_RU1-'].update(visible=True)
               jogo['-NARRADOR-'].update(visible=True)
               jogo['-ALUNO_PAVILHAO-'].update(visible=False)
               jogo['-ESPERAR_NO_PORTAO_BIBLIOTECA-'].update(visible=False)
               jogo['-ESPERAR_NO_PORTAO-'].update(visible=False)
               jogo['-PAVILHAO2-'].update(visible=False)
               jogo['-FALAR_COM_PESSOA_PAVILHAO-'].update(visible=False)
               jogo['-INICIAR_PROVA-'].update(visible=True)
               jogo['-PEGAR_BAGE_NO_PAVILHAO-'].update(visible=True)
               jogo['-CAIXA_DE_TEXTO1-'].update('No pavilhão, Athur precisa decidir o que fazer')
        #Arthur decide fazer a prova
        if evento == '-INICIAR_PROVA-':
               jogo['-IMAGEM-'].update(filename=r'')
               jogo['-FALAR_COM_PESSOA_PAVILHAO-'].update(visible=False)
               jogo['-INICIAR_PROVA-'].update(visible=False)
               jogo['-PEGAR_BAGE_NO_PAVILHAO-'].update(visible=False)
               jogo['-NARRADOR-'].update(visible=False)
               jogo['-ARTHUR_NOME-'].update(visible=True)
               jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG',visible=True)
               jogo['-CAIXA_DE_TEXTO1-'].update('Nossa, que nervoso...será que eu estou pronto mesmo?')
               jogo['-PAVILHAO2-'].update('Explorar mais',visible=True)
               jogo['-CONFIRMAR_PROVA-'].update(visible=True)
        #Arthur confirma prova e não tem mais volta
        if evento == '-CONFIRMAR_PROVA-':
               jogo['-ABRIR_MAPA_NO_RU1-'].update(visible=False)
               jogo['-ABRIR_MAPA_NO_RU1-'].update(visible=False)
               jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur1.PNG')
               jogo['-CAIXA_DE_TEXTO1-'].update('Ok...calma, calma tudo vai ficar bem...')
               jogo['-PAVILHAO2-'].update(visible=False)
               jogo['-CONFIRMAR_PROVA-'].update(visible=False)
               jogo['-CONFIRMAR_PROVA2-'].update(visible=True)
        if evento =='-CONFIRMAR_PROVA2-':
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Prova1.png')
               jogo['-HORAS-'].update(visible=False)
               jogo['-CAIXA_DE_TEXTO1-'].update('De acordo com a expressão, qual circuito melhor se encaixa?')
               jogo['-CONFIRMAR_PROVA2-'].update(visible=False)
               jogo['-ARTHUR1-'].update(visible=False)
               jogo['-PROVA_1_A-'].update(visible=True)
               jogo['-PROVA_1_B-'].update(visible=True)
               jogo['-PROVA_1_C-'].update(visible=True)
               jogo['-PROVA_1_D-'].update(visible=True)
        if evento == '-PROVA_1_A-' or evento == '-PROVA_1_B-' or evento == '-PROVA_1_C-' or evento == '-PROVA_1_D-':
               jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur_nervoso_prova.png',visible=True)
               jogo['-IMAGEM-'].update(filename=r'')
               jogo['-CAIXA_DE_TEXTO1-'].update('De acordo com o estudo da memória, qual é o menor valor endereçável?')
               jogo['-PROVA_1_A-'].update(visible=False)
               jogo['-PROVA_1_B-'].update(visible=False)
               jogo['-PROVA_1_C-'].update(visible=False)
               jogo['-PROVA_1_D-'].update(visible=False)
               jogo['-PROVA_2_A-'].update(visible=True)
               jogo['-PROVA_2_B-'].update(visible=True)
               jogo['-PROVA_2_C-'].update(visible=True)
               jogo['-PROVA_2_D-'].update(visible=True)  
        if evento == '-PROVA_2_A-' or evento == '-PROVA_2_B-' or evento == '-PROVA_2_C-' or evento == '-PROVA_2_D-':
               jogo['-CAIXA_DE_TEXTO1-'].update('Qual é o valor de DB00 em decimal?')
               jogo['-ARTHUR1-'].update(filename=r'')
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Prova3.png')
               jogo['-PROVA_2_A-'].update(visible=False)
               jogo['-PROVA_2_B-'].update(visible=False)
               jogo['-PROVA_2_C-'].update(visible=False)
               jogo['-PROVA_2_D-'].update(visible=False)
               jogo['-PROVA_3_A-'].update(visible=True)
               jogo['-PROVA_3_B-'].update(visible=True)
               jogo['-PROVA_3_C-'].update(visible=True)
               jogo['-PROVA_3_D-'].update(visible=True)
        if evento == '-PROVA_3_A-' or evento == '-PROVA_3_B-' or evento == '-PROVA_3_C-' or evento == '-PROVA_3_D-':
               jogo['-CAIXA_DE_TEXTO1-'].update('Quanto é: 11101101(2) + 63(10) = ????(8)')
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Prova4.png')
               jogo['-PROVA_3_A-'].update(visible=False)
               jogo['-PROVA_3_B-'].update(visible=False)
               jogo['-PROVA_3_C-'].update(visible=False)
               jogo['-PROVA_3_D-'].update(visible=False)
               jogo['-PROVA_4_A-'].update(visible=True)
               jogo['-PROVA_4_B-'].update(visible=True)
               jogo['-PROVA_4_C-'].update(visible=True)
               jogo['-PROVA_4_D-'].update(visible=True)
        if evento == '-PROVA_4_A-' or evento == '-PROVA_4_B-' or evento == '-PROVA_4_C-' or evento == '-PROVA_4_D-':
               jogo['-CAIXA_DE_TEXTO1-'].update('Qual é o tamanho mínimo de barramento para se endereçar 8 gigas de memória?')
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Prova5.png')
               jogo['-PROVA_4_A-'].update(visible=False)
               jogo['-PROVA_4_B-'].update(visible=False)
               jogo['-PROVA_4_C-'].update(visible=False)
               jogo['-PROVA_4_D-'].update(visible=False)
               jogo['-PROVA_5_A-'].update(visible=True)
               jogo['-PROVA_5_B-'].update(visible=True)
               jogo['-PROVA_5_C-'].update(visible=True)
               jogo['-PROVA_5_D-'].update(visible=True)      
        #Arthur acerta a questão e sua pontuação sobe 2 pontos por acerto
        if evento == '-PROVA_1_B-':
               Pontos_prova += 2
        if evento == '-PROVA_2_D-':
               Pontos_prova += 2
        if evento == '-PROVA_3_D-':
               Pontos_prova += 2
        if evento == '-PROVA_4_C-':
               Pontos_prova += 2
        if evento == '-PROVA_5_A-':
               Pontos_prova += 2
        #Prova termina e aparece o botão de resultado que levará a uma janela de sucesso ou fracasso
        if evento == '-PROVA_5_A-' or evento == '-PROVA_5_B-' or evento == '-PROVA_5_C-' or evento == '-PROVA_5_D-':
               jogo['-CAIXA_DE_TEXTO1-'].update('Certo...agora só resta saber minha pontuação')
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Terminou_prova.png')
               jogo['-PROVA_5_A-'].update(visible=False)
               jogo['-PROVA_5_B-'].update(visible=False)
               jogo['-PROVA_5_C-'].update(visible=False)
               jogo['-PROVA_5_D-'].update(visible=False)
               jogo['-FINALIZAR-'].update(visible=True)
        #Teste condicional para verifica se teve boa nota
        #Nota foi boa
        if evento == '-FINALIZAR-' and Pontos_prova >= 6:
               jogo.hide()
               Game_over.un_hide()
               Game_over['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Imagem_vitoria.png')
               Game_over['-TEXTO_EM_DESTAQUE-'].update('VITÓRIA!!!')
               Game_over['-TEXTO_FINAL-'].update(f'Você obteve uma pontuação de {Pontos_prova} pontos!',visible=True)
               Game_over['-GAME_OVER-'].update('Finalizar')
        #Nota abaixo da média
        if evento == '-FINALIZAR-' and Pontos_prova < 6:
               jogo.hide()
               Game_over.un_hide()
               Game_over['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Imagem_derrota.png')
               Game_over['-TEXTO_EM_DESTAQUE-'].update('ESSA NÃO!! DERROTA!')
               Game_over['-TEXTO_FINAL-'].update(f'Sua nota ficou abaixo da média com {Pontos_prova} pontos!',visible=True)
               Game_over['-GAME_OVER-'].update('Finalizar')       
        #Arthur decide falar com a pessoa
        if evento == '-FALAR_COM_PESSOA_PAVILHAO-' and Falou_pela_primeira_vez_pavilhao == True:
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falar_com_pessoa_pavilhao.png')
               jogo['-NARRADOR-'].update(visible=False)
               jogo['-FALAR_COM_PESSOA_PAVILHAO-'].update(visible=False)
               jogo['-FALAR_COM_PESSOA_PAVILHAO2-'].update(visible=True)
               jogo['-INICIAR_PROVA-'].update(visible=False)
               jogo['-PEGAR_BAGE_NO_PAVILHAO-'].update(visible=False)
               jogo['-ALUNO_PAVILHAO-'].update(visible=True)
               jogo['-CAIXA_DE_TEXTO1-'].update('Ei psiu! Tá procurando respostas pra prova? Por quatro reais te entrego uma hehehhe')
        if evento == '-FALAR_COM_PESSOA_PAVILHAO2-':
               Falou_pela_primeira_vez_pavilhao = False
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falar_com_pessoa_pavilhao2.png')
               jogo['-FALAR_COM_PESSOA_PAVILHAO2-'].update(visible=False)
               jogo['-CAIXA_DE_TEXTO1-'].update('E então, o que vai ser?')
               if dinheiro >= 4:
                      jogo['-COMPRAR_RESPOSTA-'].update(visible=True)
                      jogo['-NAO_COMPRAR_RESPOSTA-'].update(visible=True)
               if dinheiro < 4:
                      jogo['-NAO_COMPRAR_RESPOSTA-'].update(visible=True)
        if evento == '-FALAR_COM_PESSOA_PAVILHAO-' and Falou_pela_primeira_vez_pavilhao == False:
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falar_com_pessoa_pavilhao2.png')
               jogo['-NARRADOR-'].update(visible=False)
               jogo['-ALUNO_PAVILHAO-'].update(visible=True)
               jogo['-INICIAR_PROVA-'].update(visible=False)
               jogo['-PEGAR_BAGE_NO_PAVILHAO-'].update(visible=False)
               jogo['-FALAR_COM_PESSOA_PAVILHAO-'].update(visible=False)
               jogo['-CAIXA_DE_TEXTO1-'].update('E então, o que vai ser?')
               if dinheiro >= 4:
                      jogo['-COMPRAR_RESPOSTA-'].update(visible=True)
                      jogo['-NAO_COMPRAR_RESPOSTA-'].update(visible=True)
               if dinheiro < 4:
                      jogo['-NAO_COMPRAR_RESPOSTA-'].update(visible=True)
        #Arthur compra a resposta
        if evento == '-COMPRAR_RESPOSTA-':
               dinheiro -= 4
               Pausa['-DINHEIRO-'].update(f'Dinheiro: {dinheiro:.2f}R$')
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falar_com_pessoa_pavilhao4.png')
               Sabe_resposta4 = True
               Comprou_resposta = True
               Pausa[str(3)].update(f'Questão 04: Letra c)')
               jogo['-COMPRAR_RESPOSTA-'].update(visible=False)
               jogo['-NAO_COMPRAR_RESPOSTA-'].update(visible=False)
               jogo['-CAIXA_DE_TEXTO1-'].update('Negócio fechado hehehehe')
               jogo['-PAVILHAO2-'].update('Voltar',visible=True)
        #Arthur não compra a resposta 
        if evento == '-NAO_COMPRAR_RESPOSTA-':
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falar_com_pessoa_pavilhao3.png')
               jogo['-COMPRAR_RESPOSTA-'].update(visible=False)
               jogo['-NAO_COMPRAR_RESPOSTA-'].update(visible=False)
               jogo['-CAIXA_DE_TEXTO1-'].update('Que pena....')
               jogo['-PAVILHAO2-'].update('Voltar',visible=True)         
        #Arthur decide pegar o bagé e escolhe entre o RU e a biblioteca
        if evento == '-PEGAR_BAGE_NO_PAVILHAO-':
               jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pega_bage_do_pavilhao.png')
               jogo['-CAIXA_DE_TEXTO1-'].update('Para onde?')
               jogo['-FALAR_COM_PESSOA_PAVILHAO-'].update(visible=False)
               jogo['-INICIAR_PROVA-'].update(visible=False)
               jogo['-PEGAR_BAGE_NO_PAVILHAO-'].update(visible=False)
               jogo['-PAVILHAO2-'].update('Cancelar',visible=True)
               jogo['-ESPERAR_NO_PORTAO_BIBLIOTECA-'].update('Biblioteca',visible=True)
               jogo['-ESPERAR_NO_PORTAO-'].update('RU',visible=True)
               
        #Usuário escolhe ir para a biblioteca
        if evento == '-ESCOLHER_BIBLIOTECA_DO_PORTAO-':  
                jogo['-ESCOLHER_RU_DO_PORTAO-'].update(visible=False)
                jogo['-ESCOLHER_PAVILHAO_DO_PORTAO-'].update(visible=False)
                jogo['-ESCOLHER_BIBLIOTECA_DO_PORTAO-'].update(visible=False)
                jogo['-MAPA_PORTAO-'].update(filename='')
                jogo['-ARTHUR_NOME-'].update(visible=True)
                jogo['-CAIXA_DE_TEXTO1-'].update('Biblioteca hein? Vamos ver se o bagé aparece cedo', visible=True)
                jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG')
                jogo['-PROSSEGUIR2-'].update(visible=True)
                jogo['-CONFIRMAR_IDA_PARA_A_BIBLIOTECA-'].update(visible=True)
        #Confirmar ida para a biblioteca        
        if evento == '-CONFIRMAR_IDA_PARA_A_BIBLIOTECA-':
                jogo['-ARTHUR1-'].update(visible=False)
                jogo['-ARTHUR_NOME-'].update(visible=False)
                jogo['-NARRADOR-'].update(visible=True)
                jogo['-IMAGEM-'].update(visible=True)
                jogo['-CAIXA_DE_TEXTO1-'].update('Arthur espera no portão, agora deverá testar sua sorte para ver quanto tempo \nIrá esperar pelo Bagé')
                jogo['-PROSSEGUIR2-'].update(visible=False)
                jogo['-CONFIRMAR_IDA_PARA_A_BIBLIOTECA-'].update(visible=False)
                jogo['-ESPERAR_NO_PORTAO_BIBLIOTECA-'].update(visible=True)
        #Teste de sorte para ver quanto tempo irá esperar o bagé
        if evento == '-ESPERAR_NO_PORTAO_BIBLIOTECA-':
             tempo_de_espera = random.randint(1,15)
             minutos += tempo_de_espera
             jogo['-ESPERAR_NO_PORTAO-'].update(visible=False)
             jogo['-PAVILHAO2-'].update(visible=False)

             #Se o tempo de espera for menor que 10 irá ser adicionado um 0 na frente para melhor escrita do tempo
             if minutos >= 10:
                jogo['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Dentro_do_bage.png')
                jogo['-CAIXA_DE_TEXTO1-'].update(f'O tempo de espera foi de {tempo_de_espera} minutos, logo Arthur embarca e prossegue para a biblioteca')
                jogo['-ESPERAR_NO_PORTAO_BIBLIOTECA-'].update(visible=False)
                jogo['-VIAJAR_PARA_A_BIBLIOTECA-'].update(visible=True)
             else:
                jogo['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Dentro_do_bage.png')
                jogo['-CAIXA_DE_TEXTO1-'].update(f'O tempo de espera foi de {tempo_de_espera} minuto(s), logo Arthur embarca e prossegue para a biblioteca')
                jogo['-ESPERAR_NO_PORTAO_BIBLIOTECA-'].update(visible=False)
                jogo['-VIAJAR_PARA_A_BIBLIOTECA-'].update(visible=True)
        #Arthur viaja para a biblioteca 
        if evento == '-VIAJAR_PARA_A_BIBLIOTECA-':
              loc = 'Biblioteca'
              tempo_de_espera = random.randint(3,5)
              minutos += tempo_de_espera

        #Teste condicional para ajustar o relógio corretamente
              if minutos >= 10:
                    Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_biblioteca.png')
                    jogo['-ABRIR_MAPA_NO_RU1-'].update(visible=True)
                    jogo['-ARTHUR_NOME-'].update(visible=True)
                    jogo['-NARRADOR-'].update(visible=False)
                    jogo['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                    Pausa['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                    jogo['-IMAGEM-'].update(filename=r'')
                    jogo['-ARTHUR1-'].update(visible=True)
                    jogo['-VIAJAR_PARA_A_BIBLIOTECA-'].update(visible=False)
                    jogo['-CAIXA_DE_TEXTO1-'].update(f'Fiquei {tempo_de_espera} minutos no bagé, bem, imagino se vir para cá foi a decisão certa...')
                    jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=True)
                    jogo['-ABRIR_MAPA_NO_RU1-'].update(visible=True)
              else:
                    Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_biblioteca.png')
                    jogo['-ARTHUR_NOME-'].update(visible=True)
                    jogo['-NARRADOR-'].update(visible=False)
                    jogo['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                    Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                    jogo['-IMAGEM-'].update(filename=r'')
                    jogo['-ARTHUR1-'].update(visible=True)
                    jogo['-VIAJAR_PARA_A_BIBLIOTECA-'].update(visible=False)
                    jogo['-CAIXA_DE_TEXTO1-'].update(f'Fiquei {tempo_de_espera} minutos no bagé, bem, imagino se vir para cá foi a decisão certa...')
                    jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Prosseguir>>',visible=True)
                    jogo['-ABRIR_MAPA_NO_RU1-'].update(visible=True)
        #Arthur chega na biblioteca e decide o que fazer
        if evento == '-IR_PARA_BIBLIOTECA_DO_RU-':
                    Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_biblioteca.png')
                    jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Na_frente_da_biblioteca.png')     
                    jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
                    jogo['-COMPRAR_JANTA-'].update(visible=False)
                    jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
                    jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=False)
                    jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
                    jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
                    jogo['-ARTHUR_NOME-'].update(visible=False)
                    jogo['-NARRADOR-'].update(visible=True)
                    jogo['-ARTHUR1-'].update(visible=False)
                    jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur chega na entrada da biblioteca e decide o que fazer...')
                    jogo['-CAMINHAR_DA_BIBLIOTECA_PARA_RU-'].update(visible=True)
                    jogo['-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-'].update(visible=True)
                    jogo['-ENTRAR_NA_BIBLIOTECA-'].update(visible=True)
        #Usuário decide ir para o RU e o tempo aumenta levemente
        if evento == '-CAMINHAR_DA_BIBLIOTECA_PARA_RU-':
                    tempo_de_espera = random.randint(1,2)
                    minutos += tempo_de_espera
                    if minutos >= 10:
                         jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur_caminha1.png')    
                         jogo['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                         Pausa['-HORAS-'].update(f'Relógio: {horas}:{minutos}')                    
                         jogo['-CAMINHAR_DA_BIBLIOTECA_PARA_RU-'].update(visible=False)
                         jogo['-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-'].update(visible=False)
                         jogo['-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur caminha para o RU')
                         jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Continuar',visible=True)
                         jogo['-ENTRAR_NA_BIBLIOTECA-'].update(visible=False)
                    else:
                         jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur_caminha1.png')
                         jogo['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                         Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')                    
                         jogo['-CAMINHAR_DA_BIBLIOTECA_PARA_RU-'].update(visible=False)
                         jogo['-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-'].update(visible=False)
                         jogo['-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur caminha para o RU')
                         jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Continuar',visible=True)
                         jogo['-ENTRAR_NA_BIBLIOTECA-'].update('Entrar na bibllioteca',visible=False)
        #Arthur decide entrar na biblioteca
        if evento == '-ENTRAR_NA_BIBLIOTECA-' and Leu_livro == False and Ajudou_pessoa_na_biblioteca == False:
                    jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Biblioteca.png')
                    jogo['-ALUNO_BIBLIOTECA-'].update(visible=False)
                    jogo['-AJUDAR-'].update(visible=False)
                    jogo['-NARRADOR-'].update(visible=True)
                    jogo['-CAMINHAR_DA_BIBLIOTECA_PARA_RU-'].update(visible=False)
                    jogo['-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-'].update(visible=False)
                    jogo['-ENTRAR_NA_BIBLIOTECA-'].update(visible=False)
                    jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur decide explorar a biblioteca...')
                    jogo['-SAIR_DA_BIBLIOTECA-'].update(visible=True)
                    jogo['-FALAR_COM_PESSOA-'].update(visible=True)
                    jogo['-LER_LIVRO-'].update(visible=True)
        if evento == '-ENTRAR_NA_BIBLIOTECA-' and Leu_livro == True and Ajudou_pessoa_na_biblioteca == False:
                    jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Biblioteca.png')
                    jogo['-CAMINHAR_DA_BIBLIOTECA_PARA_RU-'].update(visible=False)
                    jogo['-NARRADOR-'].update(visible=True)
                    jogo['-AJUDAR-'].update(visible=False)
                    jogo['-ALUNO_BIBLIOTECA-'].update(visible=False)
                    jogo['-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-'].update(visible=False)
                    jogo['-ENTRAR_NA_BIBLIOTECA-'].update(visible=False)
                    jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur decide explorar a biblioteca...')
                    jogo['-SAIR_DA_BIBLIOTECA-'].update(visible=True)
                    jogo['-FALAR_COM_PESSOA-'].update(visible=True)
                    jogo['-LER_LIVRO-'].update(visible=False)
        if evento == '-ENTRAR_NA_BIBLIOTECA-' and Leu_livro == False and Ajudou_pessoa_na_biblioteca == True:
                    jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Biblioteca.png')
                    jogo['-CAMINHAR_DA_BIBLIOTECA_PARA_RU-'].update(visible=False)
                    jogo['-NARRADOR-'].update(visible=True)
                    jogo['-AJUDAR-'].update(visible=False)
                    jogo['-ALUNO_BIBLIOTECA-'].update(visible=False)
                    jogo['-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-'].update(visible=False)
                    jogo['-ENTRAR_NA_BIBLIOTECA-'].update(visible=False)
                    jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur decide explorar a biblioteca...')
                    jogo['-SAIR_DA_BIBLIOTECA-'].update(visible=True)
                    jogo['-FALAR_COM_PESSOA-'].update(visible=False)
                    jogo['-LER_LIVRO-'].update(visible=True)
        #Arthur fez tudo na biblioteca
        if evento == '-ENTRAR_NA_BIBLIOTECA-' and Leu_livro == True and Ajudou_pessoa_na_biblioteca == True:
                    jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Biblioteca.png')
                    jogo['-CAMINHAR_DA_BIBLIOTECA_PARA_RU-'].update(visible=False)
                    jogo['-NARRADOR-'].update(visible=True)
                    jogo['-AJUDAR-'].update(visible=False)
                    jogo['-ALUNO_BIBLIOTECA-'].update(visible=False)
                    jogo['-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-'].update(visible=False)
                    jogo['-ENTRAR_NA_BIBLIOTECA-'].update(visible=False)
                    jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur decide explorar a biblioteca...')
                    jogo['-SAIR_DA_BIBLIOTECA-'].update(visible=True)
                    jogo['-FALAR_COM_PESSOA-'].update(visible=False)
                    jogo['-LER_LIVRO-'].update(visible=False)           
        #Usuário decide sair da biblioteca e há uma penalidade de tempo e há uma estrutura de if para corrigir o relógio
        if evento == '-SAIR_DA_BIBLIOTECA-':
                    minutos += 2
                    if minutos >= 10:
                         jogo['-IMAGEM-'].update(filename=r'')
                         jogo['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                         Pausa['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                         jogo['-SAIR_DA_BIBLIOTECA-'].update(visible=False)
                         jogo['-FALAR_COM_PESSOA-'].update(visible=False)
                         jogo['-LER_LIVRO-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur decidiu sair da biblioteca')
                         jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Prosseguir>>',visible=True)
                    if minutos < 10:
                         jogo['-IMAGEM-'].update(filename=r'')
                         jogo['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                         Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                         jogo['-SAIR_DA_BIBLIOTECA-'].update(visible=False)
                         jogo['-FALAR_COM_PESSOA-'].update(visible=False)
                         jogo['-LER_LIVRO-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur decidiu sair da biblioteca')
                         jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Prosseguir>>',visible=True)       
       
        #Usuário decide ler um livro
        if evento == '-LER_LIVRO-':
                         numero_da_sorte = random.randint(1,2)
                         Leu_livro = True
                         if numero_da_sorte == 1:
                              jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Sucesso_livro.png')
                              Livro_util = True
                              jogo['-SAIR_DA_BIBLIOTECA-'].update(visible=False)
                              jogo['-FALAR_COM_PESSOA-'].update(visible=False)
                              jogo['-LER_LIVRO-'].update(visible=False)
                              jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur leu um livro e adquiriu informações importantes')
                              jogo['-ENTRAR_NA_BIBLIOTECA-'].update('Voltar',visible=True)
                         if numero_da_sorte == 2:
                              jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falhou_livro.png')
                              jogo['-SAIR_DA_BIBLIOTECA-'].update(visible=False)
                              jogo['-FALAR_COM_PESSOA-'].update(visible=False)
                              jogo['-LER_LIVRO-'].update(visible=False)
                              jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur leu um livro, mas não aprendeu nada')
                              jogo['-ENTRAR_NA_BIBLIOTECA-'].update('Voltar',visible=True)
        #Usuário decide falar com a pessoa na biblioteca  
        if evento == '-FALAR_COM_PESSOA-' and Falou_pela_primeira_vez_bilioteca == True:
                         jogo['-IMAGEM-'].update(filename=r'')
                         jogo['-SAIR_DA_BIBLIOTECA-'].update(visible=False)
                         jogo['-FALAR_COM_PESSOA-'].update(visible=False)
                         jogo['-LER_LIVRO-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update(f'Arthur decide falar com uma pessoa, ela aparenta estar estudando...')
                         jogo['-FALAR_COM_PESSOA2-'].update(visible=True)
        if evento == '-FALAR_COM_PESSOA2-':
                         jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Ajudar_biblioteca.png')
                         jogo['-NARRADOR-'].update(visible=False)
                         jogo['-FALAR_COM_PESSOA2-'].update(visible=False)
                         jogo['-FALAR_COM_PESSOA3-'].update(visible=True)
                         jogo['-ALUNO_BIBLIOTECA-'].update(visible=True)
                         jogo['-CAIXA_DE_TEXTO1-'].update(f'Que questões difíceis, porcaria!')
        if evento == '-FALAR_COM_PESSOA3-':
                         jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Ajudar_biblioteca2.png')
                         Falou_pela_primeira_vez_bilioteca = False
                         jogo['-FALAR_COM_PESSOA3-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update(f'Ei você pode me ajudar?Garanto que não vai se arrepender...')
                         jogo['-AJUDAR-'].update(visible=True)
                         jogo['-ENTRAR_NA_BIBLIOTECA-'].update('Voltar',visible=True)
        if evento == '-FALAR_COM_PESSOA-' and Falou_pela_primeira_vez_bilioteca == False:
                         jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Ajudar_biblioteca2.png')
                         jogo['-NARRADOR-'].update(visible=False)
                         jogo['-ALUNO_BIBLIOTECA-'].update(visible=True)
                         jogo['-SAIR_DA_BIBLIOTECA-'].update(visible=False)
                         jogo['-FALAR_COM_PESSOA-'].update(visible=False)
                         jogo['-LER_LIVRO-'].update(visible=False)
                         jogo['-AJUDAR-'].update(visible=True)
                         jogo['-ENTRAR_NA_BIBLIOTECA-'].update('Voltar',visible=True)
                         jogo['-CAIXA_DE_TEXTO1-'].update(f'E então?')
        #Arthur resolve ajudar
        if evento == '-AJUDAR-':
                         jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Ajudar_biblioteca3.png')
                         jogo['-ENTRAR_NA_BIBLIOTECA-'].update(visible=False)
                         jogo['-AJUDAR-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update('Excelente, então a primeira pergunta é.....')
                         jogo['-AJUDAR2-'].update(visible=True)
        #Quando o usuário teve sucesso no teste condicional do livro só aparece a opção correta
        if evento == '-AJUDAR2-' and Livro_util == True:
                         jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Ajudar_biblioteca4.png')
                         jogo['-AJUDAR2-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update('Quanto é DB00 de hexadecimal para decimal?')
                         jogo['-QUESTAO_1_C1-'].update(visible=True)
        if evento == '-QUESTAO_1_C1-' and Livro_util == True:
                         jogo['-CAIXA_DE_TEXTO1-'].update('Qual é o tamanho mínimo de barramento para se endereçar 4 gigas de memória?')
                         jogo['-QUESTAO_1_C1-'].update(visible=False)
                         jogo['-QUESTAO_2_A1-'].update(visible=True)
        if evento == '-QUESTAO_2_A1-' and Livro_util == True:
                         jogo['-CAIXA_DE_TEXTO1-'].update('Baseado nos seguintes dados: 1,7,6,3,9,1,11,22,7 - Qual é a mediana?')
                         jogo['-QUESTAO_2_A1-'].update(visible=False)
                         jogo['-QUESTAO_3_C1-'].update(visible=True)
        if evento == '-QUESTAO_3_C1-' and Livro_util == True:
                         jogo['-CAIXA_DE_TEXTO1-'].update('Baseado nos dados: Q1 = 6 |Mediana = 13 |Q3 = 16 - quais são os outliners?\n(inferior e superior respectivamente)')
                         jogo['-QUESTAO_3_C1-'].update(visible=False)
                         jogo['-QUESTAO_4_D1-'].update(visible=True)
        if evento == '-QUESTAO_4_D1-' and Livro_util == True:
                         jogo['-CAIXA_DE_TEXTO1-'].update('Quanto é 60 de decimal para hexadecimal?')
                         jogo['-QUESTAO_4_D1-'].update(visible=False)
                         jogo['-QUESTAO_5_A1-'].update(visible=True)                      
        #Quando o usuário falhou no teste do livro todas as alternativas possíveis aparecem
        if evento == '-AJUDAR2-' and Livro_util == False:
                         jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Ajudar_biblioteca4.png')
                         jogo['-CAIXA_DE_TEXTO1-'].update('Quanto é DB00 de hexadecimal para decimal?')
                         jogo['-AJUDAR2-'].update(visible=False)
                         jogo['-QUESTAO_1_A-'].update(visible=True)
                         jogo['-QUESTAO_1_B-'].update(visible=True)
                         jogo['-QUESTAO_1_C-'].update(visible=True)
                         jogo['-QUESTAO_1_D-'].update(visible=True)
        if evento == '-QUESTAO_1_A-' or evento == '-QUESTAO_1_B-' or evento == '-QUESTAO_1_C-' or evento == '-QUESTAO_1_D-' and Livro_util == False:
                         jogo['-CAIXA_DE_TEXTO1-'].update('Qual é o tamanho mínimo de barramento para se endereçar 4 gigas de memória?')
                         jogo['-QUESTAO_1_A-'].update(visible=False)
                         jogo['-QUESTAO_1_B-'].update(visible=False)
                         jogo['-QUESTAO_1_C-'].update(visible=False)
                         jogo['-QUESTAO_1_D-'].update(visible=False)
                         jogo['-QUESTAO_2_A-'].update(visible=True)
                         jogo['-QUESTAO_2_B-'].update(visible=True)
                         jogo['-QUESTAO_2_C-'].update(visible=True)
                         jogo['-QUESTAO_2_D-'].update(visible=True)
        if evento == '-QUESTAO_2_A-' or evento == '-QUESTAO_2_B-' or evento == '-QUESTAO_2_C-' or evento == '-QUESTAO_2_D-' and Livro_util == False:
                         jogo['-CAIXA_DE_TEXTO1-'].update('Baseado nos seguintes dados: 1,7,6,3,9,1,11,22,7 - Qual é a mediana?')
                         jogo['-QUESTAO_2_A-'].update(visible=False)
                         jogo['-QUESTAO_2_B-'].update(visible=False)
                         jogo['-QUESTAO_2_C-'].update(visible=False)
                         jogo['-QUESTAO_2_D-'].update(visible=False)
                         jogo['-QUESTAO_3_A-'].update(visible=True)
                         jogo['-QUESTAO_3_B-'].update(visible=True)
                         jogo['-QUESTAO_3_C-'].update(visible=True)
                         jogo['-QUESTAO_3_D-'].update(visible=True)
        if evento == '-QUESTAO_3_A-' or evento == '-QUESTAO_3_B-' or evento == '-QUESTAO_3_C-' or evento == '-QUESTAO_3_D-' and Livro_util == False:
                         jogo['-CAIXA_DE_TEXTO1-'].update('Baseado nos dados: Q1 = 6 |Mediana = 13 |Q3 = 16 - quais são os outliners?\n(inferior e superior respectivamente)')
                         jogo['-QUESTAO_3_A-'].update(visible=False)
                         jogo['-QUESTAO_3_B-'].update(visible=False)
                         jogo['-QUESTAO_3_C-'].update(visible=False)
                         jogo['-QUESTAO_3_D-'].update(visible=False)
                         jogo['-QUESTAO_4_A-'].update(visible=True)
                         jogo['-QUESTAO_4_B-'].update(visible=True)
                         jogo['-QUESTAO_4_C-'].update(visible=True)
                         jogo['-QUESTAO_4_D-'].update(visible=True)
        if evento == '-QUESTAO_4_A-' or evento == '-QUESTAO_4_B-' or evento == '-QUESTAO_4_C-' or evento == '-QUESTAO_4_D-' and Livro_util == False:
                         jogo['-CAIXA_DE_TEXTO1-'].update('Quanto é 60 de decimal para hexadecimal?')
                         jogo['-QUESTAO_4_A-'].update(visible=False)
                         jogo['-QUESTAO_4_B-'].update(visible=False)
                         jogo['-QUESTAO_4_C-'].update(visible=False)
                         jogo['-QUESTAO_4_D-'].update(visible=False)
                         jogo['-QUESTAO_5_A-'].update(visible=True)
                         jogo['-QUESTAO_5_B-'].update(visible=True)
                         jogo['-QUESTAO_5_C-'].update(visible=True)
                         jogo['-QUESTAO_5_D-'].update(visible=True)
        #Usuário responde corretamente  
        if evento == '-QUESTAO_1_C-' or evento == '-QUESTAO_1_C1-':
                         Questoes_certas += 1
        if evento == '-QUESTAO_2_A-' or evento == '-QUESTAO_2_A1-':
                         Questoes_certas += 1
        if evento == '-QUESTAO_3_C-' or evento == '-QUESTAO_3_C1-':
                         Questoes_certas += 1
        if evento == '-QUESTAO_4_D-' or evento == '-QUESTAO_4_D1-':
                         Questoes_certas += 1
        if evento == '-QUESTAO_5_A-' or evento == '-QUESTAO_5_A1-':
                         Questoes_certas += 1
        #Usuário termina de responder e vemos se ele teve sucesso
        #Sucesso
        if evento == '-QUESTAO_5_A1-' and Questoes_certas == 5:
                         jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Biblioteca_sucesso.png')
                         jogo['-QUESTAO_5_A1-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update('Hmmmm, tudo bate de acordo como você disse, obrigado!')
                         jogo['-SUCESSO-'].update(visible=True)
        if (evento == '-QUESTAO_5_A-' or evento == '-QUESTAO_5_B-' or evento == '-QUESTAO_5_C-' or evento == '-QUESTAO_5_D-') and Questoes_certas == 5:
                         jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Biblioteca_sucesso.png')
                         jogo['-QUESTAO_5_A-'].update(visible=False)
                         jogo['-QUESTAO_5_B-'].update(visible=False)
                         jogo['-QUESTAO_5_C-'].update(visible=False)
                         jogo['-QUESTAO_5_D-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update('Hmmmm, tudo bate de acordo como você disse, obrigado!')
                         jogo['-SUCESSO-'].update(visible=True)
        #Falha
        if (evento == '-QUESTAO_5_A-' or evento == '-QUESTAO_5_B-' or evento == '-QUESTAO_5_C-' or evento == '-QUESTAO_5_D-') and Questoes_certas < 5:
                         jogo['-QUESTAO_5_A-'].update(visible=False)
                         jogo['-QUESTAO_5_B-'].update(visible=False)
                         jogo['-QUESTAO_5_C-'].update(visible=False)
                         jogo['-QUESTAO_5_D-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update('Hmmm, não bate com os meus cálculos, deve ter alguma coisa errada, mas obrigado')
                         jogo['-FALHA-'].update(visible=True)
        #Após apertar o botão de sucesso Arthur passa a saber a resposta da 2° e o evento ficará como ocorrido
        if evento == '-SUCESSO-':
                         Pausa[str(2)].update(f'Questão 03: Letra d)')
                         Sabe_resposta3 = True
                         Ajudou_pessoa_na_biblioteca = True
                         jogo['-NARRADOR-'].update(visible=True)
                         jogo['-ALUNO_BIBLIOTECA-'].update(visible=False)
                         jogo['-SUCESSO-'].update(visible=False)
                         jogo['-ENTRAR_NA_BIBLIOTECA-'].update('Voltar',visible=True)
                         jogo['-CAIXA_DE_TEXTO1-'].update('Ao ajudar o aluno, Arthur descobre a resposta da 3° questão!')
        #Após apertar o botão de falha Arthur retorna sem respostas  
        if evento == '-FALHA-':
                         Ajudou_pessoa_na_biblioteca = True
                         jogo['-NARRADOR-'].update(visible=True)
                         jogo['-ALUNO_BIBLIOTECA-'].update(visible=False)
                         jogo['-ENTRAR_NA_BIBLIOTECA-'].update('Voltar',visible=True)
                         jogo['-FALHA-'].update(visible=False)
                         jogo['-CAIXA_DE_TEXTO1-'].update('Arthur tenta ajudar, mas não ganhou experiência com isso')
        #Fecha o mapa na escolha do Portão para o Ru
        if evento == '-ESCOLHER_RU_DO_PORTAO-':
                jogo['-ESCOLHER_RU_DO_PORTAO-'].update(visible=False)
                jogo['-ESCOLHER_PAVILHAO_DO_PORTAO-'].update(visible=False)
                jogo['-ESCOLHER_BIBLIOTECA_DO_PORTAO-'].update(visible=False)
                jogo['-MAPA_PORTAO-'].update(filename='')
                jogo['-ARTHUR_NOME-'].update(visible=True)
                jogo['-CAIXA_DE_TEXTO1-'].update('Parece que terei de esperar o Bagé, imagino quanto tempo ele levará para chegar', visible=True)
                jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG')
                jogo['-PROSSEGUIR2-'].update(visible=True)
                jogo['-CONFIRMAR_IDA_PRO_RU-'].update(visible=True)

        #Cofirma a ida pro RU
        if evento == '-CONFIRMAR_IDA_PRO_RU-':
                jogo['-ARTHUR1-'].update(visible=False)
                jogo['-ARTHUR_NOME-'].update(visible=False)
                jogo['-NARRADOR-'].update(visible=True)
                jogo['-IMAGEM-'].update(visible=True)
                jogo['-CAIXA_DE_TEXTO1-'].update('Arthur espera no portão, agora deverá testar sua sorte para ver quanto tempo \nIrá esperar pelo Bagé')
                jogo['-PROSSEGUIR2-'].update(visible=False)
                jogo['-CONFIRMAR_IDA_PRO_RU-'].update(visible=False)
                jogo['-ESPERAR_NO_PORTAO-'].update(visible=True)

        #Testar a sorte do tempo de espera
        if evento == '-ESPERAR_NO_PORTAO-':
             tempo_de_espera = random.randint(1,15)
             minutos += tempo_de_espera
             jogo['-ESPERAR_NO_PORTAO_BIBLIOTECA-'].update(visible=False)
             jogo['-PAVILHAO2-'].update(visible=False)

             #Se o tempo de espera for menor que 10 irá ser adicionado um 0 na frente para melhor escrita do tempo
             if minutos >= 10:
                jogo['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Dentro_do_bage.png')
                jogo['-CAIXA_DE_TEXTO1-'].update(f'O tempo de espera foi de {tempo_de_espera} minutos, logo Arthur embarca e prossegue para o RU')
                jogo['-ESPERAR_NO_PORTAO-'].update(visible=False)
                jogo['-VIAJAR_NO_BAGÉ_DO_PORTAO_PARA_O_RU-'].update(visible=True)
             else:
                jogo['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Dentro_do_bage.png')
                jogo['-CAIXA_DE_TEXTO1-'].update(f'O tempo de espera foi de {tempo_de_espera} minuto(s), logo Arthur embarca e prossegue para o RU')
                jogo['-ESPERAR_NO_PORTAO-'].update(visible=False)
                jogo['-VIAJAR_NO_BAGÉ_DO_PORTAO_PARA_O_RU-'].update(visible=True)

        #Arthur viaja do portão para o RU e a localização muda
        #Todas as possíveis ações no RU
        if evento == '-VIAJAR_NO_BAGÉ_DO_PORTAO_PARA_O_RU-':
              loc = 'RU'
              tempo_de_espera = random.randint(3,5)
              minutos += tempo_de_espera

        #Teste condicional para ajustar o relógio corretamente
              if minutos >= 10:
                    Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_RU.png')
                    jogo['-ARTHUR_NOME-'].update(visible=True)
                    jogo['-NARRADOR-'].update(visible=False)
                    jogo['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                    Pausa['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                    jogo['-IMAGEM-'].update(filename=r'')
                    jogo['-ARTHUR1-'].update(visible=True)
                    jogo['-VIAJAR_NO_BAGÉ_DO_PORTAO_PARA_O_RU-'].update(visible=False)
                    jogo['-CAIXA_DE_TEXTO1-'].update(f'Puxa!Devo ter ficado uns {tempo_de_espera} minutos no bagé, bem, imagino se vir para cá foi a decisão certa...')
                    jogo['-PROXIMA_ACAO_DO_PORTAO_PARA_RU-'].update(visible=True)
                    jogo['-ABRIR_MAPA_NO_RU1-'].update(visible=True)
              else:
                    Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_RU.png')
                    jogo['-ARTHUR_NOME-'].update(visible=True)
                    jogo['-NARRADOR-'].update(visible=False)
                    jogo['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                    Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                    jogo['-IMAGEM-'].update(filename=r'')
                    jogo['-ARTHUR1-'].update(visible=True)
                    jogo['-VIAJAR_NO_BAGÉ_DO_PORTAO_PARA_O_RU-'].update(visible=False)
                    jogo['-CAIXA_DE_TEXTO1-'].update(f'Puxa!Devo ter ficado uns {tempo_de_espera} minutos no bagé, bem, imagino se vir para cá foi a decisão certa...')
                    jogo['-PROXIMA_ACAO_DO_PORTAO_PARA_RU-'].update(visible=True)
                    jogo['-ABRIR_MAPA_NO_RU1-'].update(visible=True)

        #Arthur chega no RU
        if evento == '-PROXIMA_ACAO_DO_PORTAO_PARA_RU-':
                jogo['-CAIXA_DE_TEXTO1-'].update('Vejamos o que temos aqui')
                jogo['-PROXIMA_ACAO_DO_PORTAO_PARA_RU-'].update(visible=False)
                jogo['-PROXIMA_ACAO_DO_PORTAO_PARA_RU2-'].update(visible=True)
                #Mudar a imagem do ARTHUR aqui --> jogo['-ARTHUR-'].update(bambambambam)

        #Possíveis coisas pra se fazer após chegar no RU
        if evento == '-PROXIMA_ACAO_DO_PORTAO_PARA_RU2-':
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\RU_entrada.png')
            jogo['-ARTHUR1-'].update(visible=False)
            jogo['-ARTHUR_NOME-'].update(visible=False)
            jogo['-NARRADOR-'].update(visible=True)
            jogo['-PROXIMA_ACAO_DO_PORTAO_PARA_RU2-'].update(visible=False)
            jogo['-PROXIMA_ACAO_DO_PORTAO_PARA_RU3-'].update(visible=True)
            jogo['-CAIXA_DE_TEXTO1-'].update('Arthur olha ao redor e precisa decidir o que fazer...')
        if evento == '-PROXIMA_ACAO_DO_PORTAO_PARA_RU3-':
            jogo['-PROXIMA_ACAO_DO_PORTAO_PARA_RU3-'].update(visible=False)
            jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=True)
            jogo['-COMPRAR_JANTA-'].update(visible=True)
            jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Ir para a biblioteca',visible=True)
            jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=True)
            jogo['-VASCULHAR_AO_REDOR-'].update(visible=True)

        #Usuário decide procurar ao redor e há testes condicionais para ver se ele acha pelo menos um item, ou não achar nada ou acha os dois há uma variável para checar se o usuário vasculhou para se usar mais tarde
        if evento == '-VASCULHAR_AO_REDOR-':
            Vasculhou_ao_redor_RU = True
            numero_da_sorte = random.randint(0,4)
            if numero_da_sorte == 1:
                Achou_papel_amassado = True
                numero_da_sorte = 5
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Vasculhar3.png')
                jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
                jogo['-COMPRAR_JANTA-'].update(visible=False)
                jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
                jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
                jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=False)
                jogo['-CAIXA_DE_TEXTO1-'].update('Na tentativa de procurar algo ao redor, Arthur encontra um papel amassado')
                jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Voltar',visible=True)
            if numero_da_sorte == 0:
                numero_da_sorte = 5
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Vasculhar4.png')
                jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
                jogo['-COMPRAR_JANTA-'].update(visible=False)
                jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
                jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
                jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=False)
                jogo['-CAIXA_DE_TEXTO1-'].update('Arthur procura algo ao redor, mas não encontra nada!')
                jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Voltar',visible=True)
            if numero_da_sorte == 3:
                numero_da_sorte = 5
                dinheiro += 2.50
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Vasculhar2.png')
                Pausa['-DINHEIRO-'].update(f'Dinheiro: {dinheiro:.2f}R$')
                jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
                jogo['-COMPRAR_JANTA-'].update(visible=False)
                jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
                jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
                jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=False)
                jogo['-CAIXA_DE_TEXTO1-'].update('Arthur encontra 2,50R$ ao procurar nos arredores')
                jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Voltar',visible=True)
            if numero_da_sorte == 4:
                Achou_papel_amassado = True
                numero_da_sorte = 5
                dinheiro += 2.50
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Vasculhar.png')
                Pausa['-DINHEIRO-'].update(f'Dinheiro: {dinheiro:.2f}R$')
                jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
                jogo['-COMPRAR_JANTA-'].update(visible=False)
                jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
                jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
                jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=False)
                jogo['-CAIXA_DE_TEXTO1-'].update('Arthur encontra um papel amassado e 2.50R$ vasculhando ao redor')
                jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Voltar',visible=True)
        #Usuário retorna para o ponto de partida após ter vasculhado, a opção de vasculhar some(o mesmo para quando janta e fala com a pessoa)
        if evento == '-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-' and Vasculhou_ao_redor_RU == True and Jantou_no_RU == False and Falou_com_pessoa_RU == False:
            jogo['-PAGAR_A_JANTA_DA_KAYLA-'].update(visible=False)
            jogo['-ATENDENTE(RU)-'].update(visible=False)
            Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_RU.png')
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\RU_entrada.png')
            jogo['-Kayla-'].update(visible=False)
            jogo['-PAGAR_JANTA_NO_DINHEIRO-'].update(visible=False)
            jogo['-PAGAR_JANTA_NO_DINHEIRO-'].update(visible=False)
            jogo['-CAIXA_DE_TEXTO1-'].update('Após procura ao redor, Arthur retorna para onde estava...',font=('Segoe UI',13))
            jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=True)
            jogo['-COMPRAR_JANTA-'].update(visible=True)
            jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Ir para a biblioteca',visible=True)
            jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=True)
            jogo['-COMPRAR_JANTA3-'].update(visible=False)
        if evento == '-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-' and Vasculhou_ao_redor_RU == True and Jantou_no_RU == True and Falou_com_pessoa_RU == False:
            jogo['-PAGAR_A_JANTA_DA_KAYLA-'].update(visible=False)
            jogo['-ATENDENTE(RU)-'].update(visible=False)
            Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_RU.png')
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\RU_entrada.png')
            jogo['-Kayla-'].update(visible=False)   
            jogo['-ALUNO_RU1-'].update(visible=False)
            jogo['-ALUNO_RU2-'].update(visible=False)
            jogo['-NARRADOR-'].update(visible=True)
            jogo['-PAGAR_JANTA_NO_DINHEIRO-'].update(visible=False)
            jogo['-PAGAR_JANTA_NO_DINHEIRO-'].update(visible=False)
            jogo['-CAIXA_DE_TEXTO1-'].update('Arthur volta para o ponto de partida para tomar a próxima decisão...',font=('Segoe UI',13))
            jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=True)
            jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Ir para a biblioteca',visible=True)
            jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=True)
            jogo['-COMPRAR_JANTA3-'].update(visible=False)
        #Usuário decide falar com a pessoa perto dele
        if evento == '-ABORDAR_PESSOA_NA_PARADA-' and Falou_pela_primeira_vez == True:
            jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
            jogo['-ABORDAR_PESSOA_NA_PARADA2-'].update(visible=True)
            jogo['-COMPRAR_JANTA-'].update(visible=False)
            jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
            jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=False)
            jogo['-CAIXA_DE_TEXTO1-'].update('Arthur vai falar com uma pessoa que estava ali perto')
        if evento == '-ABORDAR_PESSOA_NA_PARADA2-':
            jogo['-IMAGEM-'].update(filename=r'')
            jogo['-NARRADOR-'].update(visible=False)
            jogo['-ARTHUR_NOME-'].update(visible=True)
            jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG',visible=True)
            jogo['-CAIXA_DE_TEXTO1-'].update('Olá, você errr....Kayla, por acaso você pode me ajudar?')
            jogo['-ABORDAR_PESSOA_NA_PARADA2-'].update(visible=False)
            jogo['-ABORDAR_PESSOA_NA_PARADA3-'].update(visible=True)
        if evento == '-ABORDAR_PESSOA_NA_PARADA3-':
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falar_com_kayla.png')
            jogo['-ARTHUR_NOME-'].update(visible=False)
            jogo['-ARTHUR1-'].update(visible=False)
            jogo['-Kayla-'].update(visible=True)
            jogo['-CAIXA_DE_TEXTO1-'].update('Ah, oi Arthur não estudou para a prova de hoje? Isso é um problema',font='Impact')
            jogo['-ABORDAR_PESSOA_NA_PARADA3-'].update(visible=False)
            jogo['-ABORDAR_PESSOA_NA_PARADA4-'].update(visible=True)
        if evento == '-ABORDAR_PESSOA_NA_PARADA4-':
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falar_com_kayla2.png')
            jogo['-ABORDAR_PESSOA_NA_PARADA4-'].update(visible=False)
            jogo['-ABORDAR_PESSOA_NA_PARADA5-'].update(visible=True)
            jogo['-CAIXA_DE_TEXTO1-'].update('Bem, se você me ajudar a encontrar o maldito dinheiro que deixei cair eu te ajudo\n\tEu preciso comprar uma janta para mim, estou morrendo de fome',font='Impact')
        if evento == '-ABORDAR_PESSOA_NA_PARADA5-':
            Falou_pela_primeira_vez = False
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falar_com_kayla3.png')
            jogo['-CAIXA_DE_TEXTO1-'].update('E então, o que vai ser?',font='Impact')
            jogo['-ABORDAR_PESSOA_NA_PARADA5-'].update(visible=False)
        #Uma checagem se o usuário possui dinheiro
            if dinheiro >= 2.50:
                  jogo['-PAGAR_A_JANTA_DA_KAYLA-'].update(visible=True)
                  jogo['-NAO_PAGAR_JANTA_DA_KAYLA-'].update(visible=True)
            if dinheiro < 2.50:
                  jogo['-NAO_PAGAR_JANTA_DA_KAYLA-'].update(visible=True)
        #Opção quando o usuário tem dinheiro e paga Kayla
        if evento == '-PAGAR_A_JANTA_DA_KAYLA-':
             dinheiro -= 2.50
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falar_com_kayla5.png')
             Pausa['-DINHEIRO-'].update(f'Dinheiro: {dinheiro:.2f}R$')
             jogo['-PAGAR_A_JANTA_DA_KAYLA-'].update(visible=False)
             jogo['-NAO_PAGAR_JANTA_DA_KAYLA-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Heh, sabia que podia contar contigo',font='Impact')
             jogo['-ABORDAR_PESSOA_NA_PARADA6-'].update(visible=True)
        if evento == '-ABORDAR_PESSOA_NA_PARADA6-':
             Pausa[str(4)].update(f'Questão 05: Letra a)')
             Sabe_resposta5 = True
             Falou_com_pessoa_RU = True
             jogo['-ABORDAR_PESSOA_NA_PARADA6-'].update(visible=False)
             jogo['-Kayla-'].update(visible=False)
             jogo['-NARRADOR-'].update(visible=True)
             jogo['-CAIXA_DE_TEXTO1-'].update('Obteve a resposta da questão 5!',font=('Segoe UI',13))
             jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Voltar',visible=True)
          #Opção quando o usuário não tem dinheiro
        if evento == '-NAO_PAGAR_JANTA_DA_KAYLA-':
             jogo['-PAGAR_A_JANTA_DA_KAYLA-'].update(visible=False)         
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falar_com_kayla4.png')
             jogo['-NAO_PAGAR_JANTA_DA_KAYLA-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Fazer o que, bem acho que ficarei sem a minha janta...')
             jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Voltar',visible=True)
        if evento == '-ABORDAR_PESSOA_NA_PARADA-' and Falou_pela_primeira_vez == False:
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Falar_com_kayla3.png')
            jogo['-Kayla-'].update(visible=True)
            jogo['-NARRADOR-'].update(visible=False)
            jogo['-CAIXA_DE_TEXTO1-'].update('Humm?',font='Impact') 
            jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
            jogo['-COMPRAR_JANTA-'].update(visible=False)
            jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
            jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=False)         
            if dinheiro >= 2.50:
                  jogo['-PAGAR_A_JANTA_DA_KAYLA-'].update(visible=True)
                  jogo['-NAO_PAGAR_JANTA_DA_KAYLA-'].update(visible=True)
            if dinheiro < 2.50:
                  jogo['-NAO_PAGAR_JANTA_DA_KAYLA-'].update(visible=True)    
        #Usuário decide comprar uma janta e há testes para ver se ele tem dinheiro ou terá que pagar no pix se não tiver
        if evento == '-COMPRAR_JANTA-':
            if dinheiro >= 2.50:
                jogo['-IMAGEM-'].update(filename=r'')
                jogo['-ARTHUR_NOME-'].update(visible=True)
                jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
                jogo['-NARRADOR-'].update(visible=False)
                jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG',visible=True)
                jogo['-NARRADOR-'].update(visible=False)
                jogo['-ARTHUR_NOME-'].update(visible=True)
                jogo['-COMPRAR_JANTA-'].update(visible=False)
                jogo['-COMPRAR_JANTA2-'].update(visible=True)
                jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
                jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
                jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=False)
                jogo['-CAIXA_DE_TEXTO1-'].update('Acho que comprar uma janta não faria mal')
            if dinheiro < 2.50:
                jogo['-IMAGEM-'].update(filename=r'')
                jogo['-ARTHUR_NOME-'].update(visible=True)
                jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
                jogo['-NARRADOR-'].update(visible=False)
                jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG',visible=True)
                jogo['-NARRADOR-'].update(visible=False)
                jogo['-ARTHUR_NOME-'].update(visible=True)
                jogo['-COMPRAR_JANTA-'].update(visible=False)
                jogo['-COMPRAR_JANTA2-'].update(visible=True)
                jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
                jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
                jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=False)
                jogo['-CAIXA_DE_TEXTO1-'].update('Acho que comprar uma janta não faria mal, mas terei que pagar no pix')
        #Usuário decide comprar a janta apertando botões de prosseguir e há a opção de cancelar essa ação
        if evento == '-COMPRAR_JANTA2-':
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Dentro_RU.png')
            jogo['-COMPRAR_JANTA2-'].update(visible=False)
            jogo['-ARTHUR_NOME-'].update(visible=False)
            jogo['-ARTHUR1-'].update(filename=r'')
            jogo['-NARRADOR-'].update(visible=True)
            jogo['-CAIXA_DE_TEXTO1-'].update('Arthur caminha para dentro do RU para comprar uma janta, mas não sabe quanto tempo\n\t\t\tPode acabar ficando na fila')
            jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Cancelar',visible=True)
            jogo['-COMPRAR_JANTA3-'].update(visible=True)
        #Usuário decide cancelar a janta no RU
        if evento == '-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-' and Vasculhou_ao_redor_RU == False and Jantou_no_RU == False and Falou_com_pessoa_RU == False:
            jogo['-PAGAR_A_JANTA_DA_KAYLA-'].update(visible=False)
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\RU_entrada.png')
            Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_RU.png')
            jogo['-ATENDENTE(RU)-'].update(visible=False)
            jogo['-Kayla-'].update(visible=False)
            jogo['-NARRADOR-'].update(visible=True)
            jogo['-PAGAR_JANTA_NO_PIX-'].update(visible=False)
            jogo['-PROXIMA_ACAO_DO_PORTAO_PARA_RU3-'].update(visible=False)
            jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=True)
            jogo['-COMPRAR_JANTA-'].update(visible=True)
            jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Ir para a biblioteca',visible=True)
            jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=True)
            jogo['-VASCULHAR_AO_REDOR-'].update(visible=True)
            jogo['-COMPRAR_JANTA3-'].update(visible=False)
            jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-CAIXA_DE_TEXTO1-'].update('Arthur repensa no que deve fazer',font=('Segoe UI',13))
        if evento == '-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-' and Vasculhou_ao_redor_RU == False and Jantou_no_RU == True and Falou_com_pessoa_RU == False:
            jogo['-PAGAR_A_JANTA_DA_KAYLA-'].update(visible=False)
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\RU_entrada.png')
            Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_RU.png')
            jogo['-ATENDENTE(RU)-'].update(visible=False)
            jogo['-Kayla-'].update(visible=False)
            jogo['-ALUNO_RU1-'].update(visible=False)
            jogo['-ALUNO_RU2-'].update(visible=False)
            jogo['-NARRADOR-'].update(visible=True)
            jogo['-PAGAR_JANTA_NO_PIX-'].update(visible=False)
            jogo['-PROXIMA_ACAO_DO_PORTAO_PARA_RU3-'].update(visible=False)
            jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=True)
            jogo['-COMPRAR_JANTA-'].update(visible=False)
            jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Ir para a biblioteca',visible=True)
            jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=True)
            jogo['-VASCULHAR_AO_REDOR-'].update(visible=True)
            jogo['-COMPRAR_JANTA3-'].update(visible=False)
            jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-CAIXA_DE_TEXTO1-'].update('Arthur repensa no que deve fazer',font=('Segoe UI',13))
        if evento == '-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-' and Vasculhou_ao_redor_RU == True and Jantou_no_RU == False and Falou_com_pessoa_RU == True:
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\RU_entrada.png')
            Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_RU.png')
            jogo['-ATENDENTE(RU)-'].update(visible=False)
            jogo['-Kayla-'].update(visible=False)
            jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-COMPRAR_JANTA-'].update(visible=True)
            jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
            jogo['-ALUNO_RU1-'].update(visible=False)
            jogo['-ALUNO_RU2-'].update(visible=False)
            jogo['-NARRADOR-'].update(visible=True)
            jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Ir para a biblioteca',visible=True)
            jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=True)
            jogo['-PAGAR_JANTA_NO_PIX-'].update(visible=False)
            jogo['-COMPRAR_JANTA3-'].update(visible=False)
            jogo['-CAIXA_DE_TEXTO1-'].update('Arthur repensa no que deve fazer',font=('Segoe UI',13))
        if evento == '-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-' and Vasculhou_ao_redor_RU == True and Jantou_no_RU == False and Falou_com_pessoa_RU == False:
            jogo['-PAGAR_A_JANTA_DA_KAYLA-'].update(visible=False)
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\RU_entrada.png')
            Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_RU.png')
            jogo['-ATENDENTE(RU)-'].update(visible=False)
            jogo['-Kayla-'].update(visible=False)
            jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-COMPRAR_JANTA-'].update(visible=True)
            jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=True)
            jogo['-ALUNO_RU1-'].update(visible=False)
            jogo['-ALUNO_RU2-'].update(visible=False)
            jogo['-NARRADOR-'].update(visible=True)
            jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Ir para a biblioteca',visible=True)
            jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=True)
            jogo['-PAGAR_JANTA_NO_PIX-'].update(visible=False)
            jogo['-COMPRAR_JANTA3-'].update(visible=False)
            jogo['-CAIXA_DE_TEXTO1-'].update('Arthur repensa no que deve fazer',font=('Segoe UI',13))
        if evento == '-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-' and Vasculhou_ao_redor_RU == False and Jantou_no_RU == False and Falou_com_pessoa_RU == True:
            jogo['-PAGAR_A_JANTA_DA_KAYLA-'].update(visible=False)
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\RU_entrada.png')
            Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_RU.png')
            jogo['-ATENDENTE(RU)-'].update(visible=False)
            jogo['-Kayla-'].update(visible=False)
            jogo['-VASCULHAR_AO_REDOR-'].update(visible=True)
            jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-COMPRAR_JANTA-'].update(visible=True)
            jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
            jogo['-ALUNO_RU1-'].update(visible=False)
            jogo['-ALUNO_RU2-'].update(visible=False)
            jogo['-NARRADOR-'].update(visible=True)
            jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Ir para a biblioteca',visible=True)
            jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=True)
            jogo['-PAGAR_JANTA_NO_PIX-'].update(visible=False)
            jogo['-COMPRAR_JANTA3-'].update(visible=False)
            jogo['-CAIXA_DE_TEXTO1-'].update('Arthur repensa no que deve fazer',font=('Segoe UI',13))
        #Quando todas as ações do RU são feitas só resta a opção de ir para a biblioteca e pegar o bagé
        if evento == '-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-' and Vasculhou_ao_redor_RU == True and Jantou_no_RU == True and Falou_com_pessoa_RU == True:
            jogo['-PAGAR_A_JANTA_DA_KAYLA-'].update(visible=False)
            jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\RU_entrada.png')
            Pausa['-MAPA_PORTAO-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Mapa_RU.png')
            jogo['-ATENDENTE(RU)-'].update(visible=False)
            jogo['-Kayla-'].update(visible=False)
            jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False)
            jogo['-COMPRAR_JANTA-'].update(visible=False)
            jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
            jogo['-ALUNO_RU1-'].update(visible=False)
            jogo['-ALUNO_RU2-'].update(visible=False)
            jogo['-NARRADOR-'].update(visible=True)
            jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update('Ir para a biblioteca',visible=True)
            jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=True)
            jogo['-PAGAR_JANTA_NO_PIX-'].update(visible=False)
            jogo['-COMPRAR_JANTA3-'].update(visible=False)
            jogo['-CAIXA_DE_TEXTO1-'].update('Arthur repensa no que deve fazer',font=('Segoe UI',13))

        #Usuário decide esperar na fila para comprar a janta e há mais um teste
        if evento == '-COMPRAR_JANTA3-':
              tempo_de_espera = random.randint(1,15)
              minutos += tempo_de_espera
              jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Comprar_janta.png')
              if minutos >= 10:
                jogo['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                jogo['-CAIXA_DE_TEXTO1-'].update(f'Devido ao tamanho da fila, Arthur esperou {tempo_de_espera} minuto(s)')
                jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False)
                jogo['-COMPRAR_JANTA3-'].update(visible=False)
                jogo['-COMPRAR_JANTA4-'].update(visible=True)
              else:
                jogo['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                jogo['-CAIXA_DE_TEXTO1-'].update(f'Devido ao tamanho da fila, Arthur esperou {tempo_de_espera} minuto(s)')
                jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False)
                jogo['-COMPRAR_JANTA3-'].update(visible=False)
                jogo['-COMPRAR_JANTA4-'].update(visible=True)
        #Após passar pela fila há um teste para verificar o dinheiro do usuário, se tiver ele pagará a janta sem problema
        if evento == '-COMPRAR_JANTA4-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Comprar_janta2.png')
             jogo['-NARRADOR-'].update(visible=False)
             jogo['-ATENDENTE(RU)-'].update(visible=True)
             jogo['-CAIXA_DE_TEXTO1-'].update(f'Qual vai ser a forma de pagamento?')
             jogo['-COMPRAR_JANTA4-'].update(visible=False)
             if dinheiro >= 2.50:
                  jogo['-PAGAR_JANTA_NO_DINHEIRO-'].update(visible=True)
                  jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Ir embora',visible=True)
             else:
                  jogo['-PAGAR_JANTA_NO_PIX-'].update('Pagar no pix(teste sua sorte)',visible=True)
                  jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Ir embora',visible=True)
        #Quando o usuário não tem dinheiro ele pagará no pix que irá causar penalidade
        if evento == '-PAGAR_JANTA_NO_PIX-':
            jogo['-ATENDENTE(RU)-'].update(visible=False)
            jogo['-NARRADOR-'].update(visible=True)
            numero_da_sorte = random.randint(1,5)
        #testes condicionais se o número da sorte saiu ou não, e também há o ajuste para o relógio
            if (numero_da_sorte == 2 or numero_da_sorte == 3 or numero_da_sorte == 4 or numero_da_sorte == 5) and minutos >= 10:
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pagamento_falha.png')
                tempo_de_espera = random.randint(1,2)
                minutos += tempo_de_espera
                tempo_de_espera_total_do_pagamento_via_pix_no_RU += tempo_de_espera
                jogo['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                jogo['-CAIXA_DE_TEXTO1-'].update(f'Pagamento mal sucedido!')
                jogo['-PAGAR_JANTA_NO_PIX-'].update('Tentar novamente',visible=True) 
            if numero_da_sorte == 1 and minutos >= 10:
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pagamento_sucesso.png') 
                tempo_de_espera = random.randint(1,2)
                minutos += tempo_de_espera
                tempo_de_espera_total_do_pagamento_via_pix_no_RU += tempo_de_espera
                jogo['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                jogo['-PAGAR_JANTA_NO_PIX-'].update(visible=False)
                jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False) 
                jogo['-CAIXA_DE_TEXTO1-'].update(f'Pagamento bem-sucedido!\nA internet no RU está horrível e levou {tempo_de_espera_total_do_pagamento_via_pix_no_RU} minuto(s) para efetuar o pagamento')
                jogo['-COMPRAR_JANTA5-'].update(visible=True)
            if (numero_da_sorte == 2 or numero_da_sorte == 3 or numero_da_sorte == 4 or numero_da_sorte == 5) and minutos < 10:
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pagamento_falha.png')
                tempo_de_espera = random.randint(1,2)
                minutos += tempo_de_espera
                tempo_de_espera_total_do_pagamento_via_pix_no_RU += tempo_de_espera
                jogo['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                jogo['-CAIXA_DE_TEXTO1-'].update(f'Pagamento mal sucedido!')
                jogo['-PAGAR_JANTA_NO_PIX-'].update('Tentar novamente',visible=True) 
            if numero_da_sorte == 1 and minutos < 10:
                jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pagamento_sucesso.png') 
                tempo_de_espera = random.randint(1,2)
                minutos += tempo_de_espera
                tempo_de_espera_total_do_pagamento_via_pix_no_RU += tempo_de_espera
                jogo['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                jogo['-PAGAR_JANTA_NO_PIX-'].update(visible=False)
                jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False) 
                jogo['-CAIXA_DE_TEXTO1-'].update(f'Pagamento bem-sucedido!\nA internet no RU está horrível e levou {tempo_de_espera_total_do_pagamento_via_pix_no_RU} minuto(s) para efetuar o pagamento')
                jogo['-COMPRAR_JANTA5-'].update(visible=True)
        #Quando o usuário tem dinheiro ele pagar em dinheiro, quando tem o valor é subtraído
        if evento == '-PAGAR_JANTA_NO_DINHEIRO-':
             dinheiro -= 2.50
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pagou_no_dinheiro.png')
             jogo['-NARRADOR-'].update(visible=True)
             jogo['-ATENDENTE(RU)-'].update(visible=False)
             jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False)
             Pausa['-DINHEIRO-'].update(f'Dinheiro: {dinheiro:.2f}R$')
             jogo['-PAGAR_JANTA_NO_DINHEIRO-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Arthur paga em espécie e prossegue para o RU')
             jogo['-COMPRAR_JANTA5-'].update(visible=True)
        if evento == '-COMPRAR_JANTA5-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pegou_janta1.png')
             tempo_de_espera_total_do_pagamento_via_pix_no_RU = 0
             jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update(visible=False)
             jogo['-COMPRAR_JANTA5-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Arthur pega sua janta e se acomoda em uma mesa ele consegue ouvir uma conversa...')
             jogo['-COMPRAR_JANTA6-'].update(visible=True)
        if evento == '-COMPRAR_JANTA6-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pegou_janta2.png')
             jogo['-COMPRAR_JANTA6-'].update(visible=False)
             jogo['-COMPRAR_JANTA7-'].update(visible=True)
             jogo['-NARRADOR-'].update(visible=False)
             jogo['-ALUNO_RU1-'].update(visible=True)
             jogo['-CAIXA_DE_TEXTO1-'].update('Cara, que prova foi aquela?! Mal pude acreditar quando vi!')
        if evento == '-COMPRAR_JANTA7-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pegou_janta3.png')
             jogo['-COMPRAR_JANTA7-'].update(visible=False)
             jogo['-COMPRAR_JANTA8-'].update(visible=True)
             jogo['-ALUNO_RU1-'].update(visible=False)
             jogo['-ALUNO_RU2-'].update(visible=True)
             jogo['-CAIXA_DE_TEXTO1-'].update('Difícil sim, mas consegui lidar com ela...')
        if evento == '-COMPRAR_JANTA8-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pegou_janta4.png')
             jogo['-COMPRAR_JANTA8-'].update(visible=False)
             jogo['-COMPRAR_JANTA9-'].update(visible=True)
             jogo['-ALUNO_RU2-'].update(visible=False)
             jogo['-ALUNO_RU1-'].update(visible=True)
             jogo['-CAIXA_DE_TEXTO1-'].update('Parece que hoje é a vez do pessoal de LC, hehehe')
        #Após ouvir a conversa o usuário precisa tomar uma decisão de ir embora ou falar com os alunos
        if evento == '-COMPRAR_JANTA9-':
             jogo['-ALUNO_RU1-'].update(visible=False)
             jogo['-NARRADOR-'].update(visible=True)
             jogo['-COMPRAR_JANTA9-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Arthur nota a menção a respeito de seu curso e toma uma decisão...')
             jogo['-NAO_FALAR_COM_ALUNOS_RU-'].update(visible=True)
             jogo['-FALAR_COM_ALUNOS_RU-'].update(visible=True)
        if evento == '-FALAR_COM_ALUNOS_RU-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pegou_janta5.png')
             jogo['-COMPRAR_JANTA10-'].update(visible=True)
             jogo['-NAO_FALAR_COM_ALUNOS_RU-'].update(visible=False)
             jogo['-FALAR_COM_ALUNOS_RU-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Logo Arthur se aproxima dos dois alunos e eles logo notam sua presença')
        if evento == '-COMPRAR_JANTA10-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pegou_janta6.png')
             jogo['-ALUNO_RU1-'].update(visible=True)
             jogo['-NARRADOR-'].update(visible=False)
             jogo['-COMPRAR_JANTA11-'].update(visible=True)
             jogo['-COMPRAR_JANTA10-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Ah, você deve ser um aluno de LC em que posso te ajudar?')
        if evento == '-COMPRAR_JANTA11-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pegou_janta7.png')
             jogo['-ALUNO_RU2-'].update(visible=True)
             jogo['-ALUNO_RU1-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Talvez ele queira ajuda em relação a prova?')
             jogo['-COMPRAR_JANTA11-'].update(visible=False)
             jogo['-COMPRAR_JANTA12-'].update(visible=True)
        #Após a primeira impressão, o usuário aperta um botão obrigatório
        if evento == '-COMPRAR_JANTA12-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pegou_janta8.png')
             jogo['-COMPRAR_JANTA12-'].update(visible=False)
             jogo['-ALUNO_RU2-'].update(visible=False)
             jogo['-NARRADOR-'].update(visible=True)
             jogo['-CAIXA_DE_TEXTO1-'].update('Após uma troca de olhares, você precisa decidir o que fazer...')
             jogo['-PEDIR_RESPOSTA_PARA_PESSOAS_NO_RU-'].update(visible=True)
        if evento == '-PEDIR_RESPOSTA_PARA_PESSOAS_NO_RU-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pegou_janta9.png')
             jogo['-PEDIR_RESPOSTA_PARA_PESSOAS_NO_RU-'].update(visible=False)
             jogo['-PEDIR_RESPOSTA_PARA_PESSOAS_NO_RU2-'].update(visible=True)
             jogo['-NARRADOR-'].update(visible=False)
             jogo['-ALUNO_RU2-'].update(visible=True)
             jogo['-CAIXA_DE_TEXTO1-'].update('Bem, eu até te ajudaria, mas deixei algumas anotações caírem em algum lugar, eu tinha o número \n\t\tde um cara que me mandou umas questões que caíram')
        #Arthur precisa tomar uma decisão se vai tentar obter as respostas ou ir embora
        if evento == '-PEDIR_RESPOSTA_PARA_PESSOAS_NO_RU2-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pegou_janta10.png')
             jogo['-ALUNO_RU2-'].update(visible=False)
             jogo['-ALUNO_RU1-'].update(visible=True)
             jogo['-PEDIR_RESPOSTA_PARA_PESSOAS_NO_RU2-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Eu tenho elas bem aqui! mas não te entregarei facilmente, que tal uma aposta?')
             if Achou_papel_amassado == False:
                  jogo['-JOGAR_PEDRA_PAPEL_TESOURA_CONTRA_PESSOA_NO_RU-'].update(visible=True)
             if Achou_papel_amassado == True:
                  jogo['-JOGAR_PEDRA_PAPEL_TESOURA_CONTRA_PESSOA_NO_RU-'].update(visible=True)
                  jogo['-MOSTRAR_PAPEL_AMASSADO_RU-'].update(visible=True)
        #Arthur decide jogar pedra,papel e tesoura
        if evento == '-JOGAR_PEDRA_PAPEL_TESOURA_CONTRA_PESSOA_NO_RU-':
             Pedra_papel_tesoura_completo['-ESCOLHA_DO_ARTHUR-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\pedra_papel_tesoura.png')
             jogo['-CAIXA_DE_TEXTO1-'].update('Pedra papel e tesoura então? Ok!')
             jogo['-JOGAR_PEDRA_PAPEL_TESOURA_CONTRA_PESSOA_NO_RU-'].update(visible=False)
             jogo['-MOSTRAR_PAPEL_AMASSADO_RU-'].update(visible=False)
             jogo['-COMEÇAR_PEDRA_PAPEL_TESOURA-'].update(visible=True)
        #pedra, papel e tesoura começa
        if evento == '-COMEÇAR_PEDRA_PAPEL_TESOURA-':
             #A escolha do pc será o seguinte: Pedra = 1; Papel = 2; Tesoura = 3
             #O jogo fecha e o pedra,papel e tesoura abre
             jogo.hide()
             Pedra_papel_tesoura_completo.un_hide()
             Pedra_papel_tesoura_completo['-TITULO_DO_PEDRA_PAPEL_TESOURA-'].update('Pedra,papel e tesoura')
             Pedra_papel_tesoura_completo['-PLACAR_ARTHUR-'].update(f'{Arthur_placar}\t\t\t\t')
             Pedra_papel_tesoura_completo['-PLACAR_PC-'].update(f'{Pc_placar}')
             #As escolhas condicionais do pedra,papel e tesoura, toda vez que uma escolha é feita o pc escolhe aleatoriamente um valor
        if pedra1 == '-PEDRA-' or pedra1 == '-PAPEL-' or pedra1 == '-TESOURA-':
                Pc_escolha = random.randint(1,3)
                print(Pc_escolha)
                if pedra1 == '-PEDRA-' and Pc_escolha == 1:
                     Pc_escolha = 0
                     Pedra_papel_tesoura_completo['-ESCOLHA_DO_ARTHUR-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\pedra_pedra.png')
                     Pedra_papel_tesoura_completo['-RESULTADO_DA_JOGADA-'].update('Empate!')
                if pedra1 == '-PEDRA-' and Pc_escolha == 2:
                     Pc_placar += 1
                     Pedra_papel_tesoura_completo['-PLACAR_PC-'].update(f'{Pc_placar}')
                     Pedra_papel_tesoura_completo['-ESCOLHA_DO_ARTHUR-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\pedra_papel.png')
                     Pc_escolha = 0
                     Pedra_papel_tesoura_completo['-RESULTADO_DA_JOGADA-'].update('Rodada perdida!')
                if pedra1 == '-PEDRA-' and Pc_escolha == 3:
                     Arthur_placar += 1
                     Pedra_papel_tesoura_completo['-PLACAR_ARTHUR-'].update(f'{Arthur_placar}\t\t\t\t')
                     Pedra_papel_tesoura_completo['-ESCOLHA_DO_ARTHUR-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\pedra_tesoura.png')
                     Pc_escolha = 0
                     Pedra_papel_tesoura_completo['-RESULTADO_DA_JOGADA-'].update('Ganhou a rodada!')
                if pedra1 == '-PAPEL-' and Pc_escolha == 1:
                     Arthur_placar += 1
                     Pedra_papel_tesoura_completo['-PLACAR_ARTHUR-'].update(f'{Arthur_placar}\t\t\t\t')
                     Pedra_papel_tesoura_completo['-ESCOLHA_DO_ARTHUR-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\papel_pedra.png')
                     Pc_escolha = 0
                     Pedra_papel_tesoura_completo['-RESULTADO_DA_JOGADA-'].update('Venceu a rodada!')
                if pedra1 == '-PAPEL-' and Pc_escolha == 2:
                     Pedra_papel_tesoura_completo['-ESCOLHA_DO_ARTHUR-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\papel_papel.png')
                     Pc_escolha = 0
                     Pedra_papel_tesoura_completo['-RESULTADO_DA_JOGADA-'].update('Rodada empatada!')
                if pedra1 == '-PAPEL-' and Pc_escolha == 3:
                     Pc_placar += 1
                     Pedra_papel_tesoura_completo['-PLACAR_PC-'].update(f'{Pc_placar}')
                     Pedra_papel_tesoura_completo['-ESCOLHA_DO_ARTHUR-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\papel_tesoura.png')
                     Pc_escolha = 0
                     Pedra_papel_tesoura_completo['-RESULTADO_DA_JOGADA-'].update('Perdeu a rodada!')
                if pedra1 == '-TESOURA-' and Pc_escolha == 1:
                     Pc_placar += 1
                     Pedra_papel_tesoura_completo['-PLACAR_PC-'].update(f'{Pc_placar}')
                     Pedra_papel_tesoura_completo['-ESCOLHA_DO_ARTHUR-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\tesoura_pedra.png')
                     Pc_escolha = 0
                     Pedra_papel_tesoura_completo['-RESULTADO_DA_JOGADA-'].update('Perdeu a rodada!')
                if pedra1 == '-TESOURA-' and Pc_escolha == 2:
                     Arthur_placar += 1
                     Pedra_papel_tesoura_completo['-PLACAR_ARTHUR-'].update(f'{Arthur_placar}\t\t\t\t')
                     Pedra_papel_tesoura_completo['-ESCOLHA_DO_ARTHUR-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\tesoura_papel.png')
                     Pc_escolha = 0
                     Pedra_papel_tesoura_completo['-RESULTADO_DA_JOGADA-'].update('Rodada ganha!')
                if pedra1 == '-TESOURA-' and Pc_escolha == 3:
                     Pedra_papel_tesoura_completo['-ESCOLHA_DO_ARTHUR-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\tesoura_tesoura.png')
                     Pc_escolha = 0
                     Pedra_papel_tesoura_completo['-RESULTADO_DA_JOGADA-'].update('Rodada empatada!')
        #Pedra, papel e tesoura termina quando um dos dois chega a 3
        if Arthur_placar == 3:
             Pedra_papel_tesoura_completo['-PEDRA-'].update(visible=False)
             Pedra_papel_tesoura_completo['-PAPEL-'].update(visible=False)
             Pedra_papel_tesoura_completo['-TESOURA-'].update(visible=False)
             Pedra_papel_tesoura_completo['-RESULTADO_DA_JOGADA-'].update('Venceu o jogo!')
             Pedra_papel_tesoura_completo['-VITORIA-'].update(visible=True)
        #Pc ganha o jogo
        if Pc_placar == 3:
             Pedra_papel_tesoura_completo['-PEDRA-'].update(visible=False)
             Pedra_papel_tesoura_completo['-PAPEL-'].update(visible=False)
             Pedra_papel_tesoura_completo['-TESOURA-'].update(visible=False)
             Pedra_papel_tesoura_completo['-RESULTADO_DA_JOGADA-'].update('Derrota!')
             Pedra_papel_tesoura_completo['-DERROTA-'].update(visible=True)
        #Usuário ganha o jogo
        if pedra1 == '-VITORIA-':
             jogo.un_hide()
             Pedra_papel_tesoura_completo.hide()
             jogo['-COMEÇAR_PEDRA_PAPEL_TESOURA-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Tudo bem você ganhou, me passa teu número pra mandar as questões')
             jogo['-GANHOU_PEDRA_PAPEL_TESOURA-'].update(visible=True)
        if evento == '-GANHOU_PEDRA_PAPEL_TESOURA-':
            Pausa[str(0)].update(f'Questão 01: Letra b)')
            Pausa[str(1)].update(f'Questão 02: Letra d)')
            Sabe_resposta1 = True
            Sabe_resposta2 = True
            dinheiro += 2
            Pausa['-DINHEIRO-'].update(f'Dinheiro: {dinheiro:.2f}R$')
            jogo['-ALUNO_RU1-'].update(visible=False)
            jogo['-NARRADOR-'].update(visible=True)
            jogo['-GANHOU_PEDRA_PAPEL_TESOURA-'].update(visible=False)
            jogo['-GANHOU_PEDRA_PAPEL_TESOURA2-'].update(visible=True)
            jogo['-CAIXA_DE_TEXTO1-'].update('Você recebeu as respostas no whatsapp e recebeu dois reais!')
        if evento == '-GANHOU_PEDRA_PAPEL_TESOURA2-':
            Jantou_no_RU = True
            jogo['-ALUNO_RU1-'].update(visible=True)
            jogo['-NARRADOR-'].update(visible=False)
            jogo['-GANHOU_PEDRA_PAPEL_TESOURA2-'].update(visible=False)
            jogo['-CAIXA_DE_TEXTO1-'].update('Espero que seja tão bom em cálculo quanto em pedra papel e tesoura')
            jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Voltar',visible=True)
        #Usuário perde o jogo
        if pedra1 == '-DERROTA-':
             jogo.un_hide()
             Pedra_papel_tesoura_completo.hide()
             jogo['-CAIXA_DE_TEXTO1-'].update('Quem sabe na próxima parceiro')
             jogo['-COMEÇAR_PEDRA_PAPEL_TESOURA-'].update(visible=False)
             jogo['-PERDEU_PEDRA_PAPEL_TESOURA-'].update(visible=True)
        if evento == '-PERDEU_PEDRA_PAPEL_TESOURA-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Pegou_janta11.png')
             jogo['-ALUNO_RU1-'].update(visible=False)
             jogo['-ALUNO_RU2-'].update(visible=True)
             jogo['-PERDEU_PEDRA_PAPEL_TESOURA-'].update(visible=False)
             jogo['-PERDEU_PEDRA_PAPEL_TESOURA2-'].update(visible=True)
             jogo['-CAIXA_DE_TEXTO1-'].update('Lhe desejo sorte...')
        if evento == '-PERDEU_PEDRA_PAPEL_TESOURA2-':
             Jantou_no_RU = True
             dinheiro -= 2
             Pausa['-DINHEIRO-'].update(f'Dinheiro: {dinheiro:.2f}R$')
             jogo['-ALUNO_RU2-'].update(visible=False)
             jogo['-NARRADOR-'].update(visible=True)
             jogo['-PERDEU_PEDRA_PAPEL_TESOURA2-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Arthur não conseguiu obter as respostas e perdeu 2 reais!')
             jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Voltar',visible=True)

        #Arthur mostra o papel e obtém as respostas da forma mais fácil
        if evento == '-MOSTRAR_PAPEL_AMASSADO_RU-':
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\mostrou_papel.png')
             jogo['-ALUNO_RU2-'].update(visible=True)
             jogo['-ALUNO_RU1-'].update(visible=False)
             jogo['-JOGAR_PEDRA_PAPEL_TESOURA_CONTRA_PESSOA_NO_RU-'].update(visible=False)
             jogo['-MOSTRAR_PAPEL_AMASSADO_RU-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Ah, você encontrou...me dê um momento') 
             jogo['-MOSTRAR_PAPEL_RU2-'].update(visible=True) 
        if evento == '-MOSTRAR_PAPEL_RU2-':
             Pausa[str(0)].update(f'Questão 01: Letra b)')
             Pausa[str(1)].update(f'Questão 02: Letra d)')
             Sabe_resposta1 = True
             Sabe_resposta2 = True
             jogo['-ALUNO_RU2-'].update(visible=False)
             jogo['-NARRADOR-'].update(visible=True)
             jogo['-CAIXA_DE_TEXTO1-'].update('Após trocar mensagem com o contato, você recebeu a resposta da 1 e 2!')
             jogo['-MOSTRAR_PAPEL_RU2-'].update(visible=False)
             jogo['-MOSTRAR_PAPEL_RU3-'].update(visible=True) 
        #Após esse ponto a variável "Jantou_no_RU" se torna True indicando que acabou as ações dentro do RU
        if evento == '-MOSTRAR_PAPEL_RU3-':
             Jantou_no_RU = True
             jogo['-MOSTRAR_PAPEL_RU3-'].update(visible=False)
             jogo['-ALUNO_RU2-'].update(visible=True)
             jogo['-NARRADOR-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Boa sorte com a prova, não desista!')
             jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Voltar',visible=True)          
        if evento == '-NAO_FALAR_COM_ALUNOS_RU-':
             Jantou_no_RU = True
             jogo['-NAO_FALAR_COM_ALUNOS_RU-'].update(visible=False)
             jogo['-FALAR_COM_ALUNOS_RU-'].update(visible=False)
             jogo['-CAIXA_DE_TEXTO1-'].update('Arthur termina de jantar e retorna para o ponto de partida')
             jogo['-VOLTAR_DEPOIS_DE_VASCULHAR_AO_REDOR-'].update('Voltar',visible=True)
        #Usuário decide voltar para o pavilhão
        if evento == '-PEGAR_O_BAGÉ_DO_RU-' or evento == '-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-':
                    jogo['-IMAGEM-'].update(filename=r'')
                    jogo['-ABORDAR_PESSOA_NA_PARADA-'].update(visible=False)
                    jogo['-COMPRAR_JANTA-'].update(visible=False)
                    jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
                    jogo['-PEGAR_O_BAGÉ_DO_RU-'].update(visible=False)
                    jogo['-VASCULHAR_AO_REDOR-'].update(visible=False)
                    jogo['-IR_PARA_BIBLIOTECA_DO_RU-'].update(visible=False)
                    jogo['-ARTHUR_NOME-'].update(visible=True)
                    jogo['-NARRADOR-'].update(visible=False)
                    jogo['-ARTHUR1-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Arthur3.PNG',visible=True)
                    jogo['-CAMINHAR_DA_BIBLIOTECA_PARA_RU-'].update(visible=False)
                    jogo['-PEGAR_BAGÉ_A_PARTIR_DA_BIBLIOTECA-'].update(visible=False)
                    jogo['-ENTRAR_NA_BIBLIOTECA-'].update(visible=False)
                    jogo['-VIAJAR_DO_RU_OU_BIBLIOTECA-'].update(visible=True)
                    jogo['-CAIXA_DE_TEXTO1-'].update(f'Talvez seja melhor eu ir para o pavilhão...')
        if evento ==  '-VIAJAR_DO_RU_OU_BIBLIOTECA-':
             tempo_de_espera = random.randint(1,15)
             minutos += tempo_de_espera
             jogo['-VIAJAR_DO_RU_OU_BIBLIOTECA-'].update(visible=False)
             jogo['-ARTHUR_NOME-'].update(visible=False)
             jogo['-NARRADOR-'].update(visible=True)
             jogo['-ARTHUR1-'].update(visible=False)
             jogo['-IMAGEM-'].update(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\Dentro_do_bage.png')

             #Se o tempo de espera for menor que 10 irá ser adicionado um 0 na frente para melhor escrita do tempo
             if minutos >= 10:
                jogo['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:{minutos}')
                jogo['-CAIXA_DE_TEXTO1-'].update(f'O tempo de espera foi de {tempo_de_espera} minutos, Arthur viaja até o pavilhão')
                jogo['-PAVILHAO2-'].update('Prosseguir para o pavilhão',visible=True)
             else:
                jogo['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                Pausa['-HORAS-'].update(f'Relógio: {horas}:0{minutos}')
                jogo['-CAIXA_DE_TEXTO1-'].update(f'O tempo de espera foi de {tempo_de_espera} minuto(s), e Arthur prossegue para o pavilhão')
                jogo['-PAVILHAO2-'].update('Prosseguir para o pavilhão',visible=True)
cont = 0
#Tema da janela
sg.theme("Black")
#Deixa o menu aberto
jogo_aberto = True

#Menu principal dividido em partes
imagem_no_menu1 =[
        [sg.Image(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\atrasadinho_menu2.png',size=(300,500))]
]
menu =  [
        [sg.Text('O Procastinador',size=(36,1),font=('Comic Sans MS',30),justification='center')],
        [sg.Text('')],
        [sg.Button('Iniciar',font=('Courier'),size=(13,1))],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Button('Sair',font=('Courier'),size=(13,1))]
    ]
imagem_no_menu2 =[
        [sg.Image(filename=r'c:\Users\user\Downloads\O Procastinador(executável)\imagens\atrasadinho_menu.png',size=(300,500))]
]
#Menu completo e a criação da janela
juntar_partes_do_menu = [[sg.Column(imagem_no_menu1,element_justification='right'),sg.Column(menu,element_justification='center'),sg.Column(imagem_no_menu2)]]
menu_principal_completo = sg.Window('O Procastinador',juntar_partes_do_menu)
#O ciclo que vai manter o menu aberto
while cont < 1:
    
    evento,value = menu_principal_completo.Read()
    #opção de sair do jogo pelo x e pelo botão sair
    #opção para começar o jogo
    if evento == 'Iniciar':
        cont += 1
        #A janela antiga fecha e executa a função para o ato 1 com Ato01()
        menu_principal_completo.close()
        #Janela do ato 1 e sua função
        Ato01()
    if evento in ['Sair',sg.WIN_CLOSED]:
        break
            
        









#Fecha o jogo se o ciclo for quebrado
menu_principal_completo.close()