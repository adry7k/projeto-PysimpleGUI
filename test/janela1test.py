import PySimpleGUI as sg  #09/02/2025


#criando a primeira janela de login
def janela_login(): 
    sg.theme('light gray 1')
    
    #Este aqui é lista que será o menu que aparecerá no canto superior esquerdo das janelas
    menu_layout = [['Sobre'], 
                    ['Creditos']]

    layout_inicial = [
        [sg.Menu(menu_layout)],
        [sg.Text('Bem-vindo ao QUIZ de conhecimentos gerais', font=('Calibri', 16),expand_x=True, text_color='White', background_color='Black', justification='c')],
        [sg.Text()],
        [sg.Image(filename='question200.png')],
        [sg.Text()], #Estas linhas vazias são espaçamentos que aparecem para fins estéticos da janela
        [sg.Text()],
        [sg.Text()],
        [sg.Push(), sg.Button('Sair', size=(8, 2)), sg.Button('Continuar', size=(8, 2))],
    ]

    return sg.Window('QUIZ DE CONHECIMENTO GERAIS', layout_inicial, size=(500, 500), element_justification='center', finalize=True)

#Criando a segunda janela
def janela_questions():
    sg.theme('light gray 1')
    
    menu_dois = [['Sobre'], 
                 ['Creditos']]
     
    layout_dois = [
        [sg.Menu(menu_dois)],
        [sg.Text('Pergunta', font=('Calibri bold', 16)), sg.Image('imagempergunta.png')],
        [sg.Text()],
        [sg.Text()],
        [sg.Checkbox('Alternativa1', font=('Arial', 12), size=(15, 1))],
        [sg.Checkbox('Alternativa2', font=('Arial', 12), size=(15, 1))],
        [sg.Checkbox('Alternativa3', font=('Arial', 12), size=(15, 1))],
        [sg.Checkbox('Alternativa4', font=('Arial', 12), size=(15, 1))],
        [sg.Checkbox('Alternativa5', font=('Arial', 12), size=(15, 1))],
        [sg.Text()],
        [sg.Push(), sg.Button('Continuar', size=(8, 2))],
    ]
    
    return sg.Window('QUIZ DE CONHECIMENTO GERAIS', layout_dois, size=(500, 500), finalize=True, element_justification='c')

def Creditos():
    sg.popup('Agradecimento', 'Creditos para os alunos:', 'CICLANO', 'BELTRANO', 'JUBISCLANO', 'Alunos de licenciatura em computação')

def Sobre():
    sg.popup('Sobre', 'O programa é um quiz de conhecimentos gerais para testar seu nível de inteligência')

janela1, janela2 = janela_login(), None  #Faz com o que as duas janelas não sejam abertas ao mesmo tempo e somente a de login

while True:
    """window: Identifica as janelas para interações
    evento: As interações que o usuário fará nas janelas
    valores: é o valor que ficará guardado na memória do programa"""
    window, evento, valores = sg.read_all_windows() 
    
    if window == janela1 and evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    
    if window == janela1 and evento == 'Continuar':
        usuario = valores['-USUARIO-']
        if usuario:
            janela2 = janela_questions()
            janela1.hide()
        else:
            janela1['-MENSAGEM-'].update('Digite seu nome para "continuar"')
    
    if window == janela2 and evento == sg.WIN_CLOSED:
        janela2.close()
        janela1.un_hide()
    
    if evento == 'Sobre':
        Sobre()
    
    if evento == 'Creditos':
        Creditos()

janela1.close()