import PySimpleGUI as sg
from perguntas import quiz_data

#criando a primeira janela 
def janela_login(): 
    sg.theme('light gray 1')
    
    #Este aqui é lista que será o menu que aparecerá no canto superior esquerdo das janelas
    menu_layout = [['Sobre'], 
                    ['Creditos']]

    layout_inicial = [
        [sg.Menu(menu_layout)],
        [sg.Text('Bem-vindo ao QUIZ de conhecimentos gerais', font=('Calibri', 16, 'Bold'),expand_x=True, text_color='White', background_color='Black', justification='c')],
        [sg.Text()],
        [sg.Image(filename='question200.png')],
        [sg.Text()], #Estas linhas vazias são espaçamentos que aparecem para fins estéticos da janela
        [sg.Text()],
        [sg.Text()],
        [sg.Push(), sg.Button('Sair', size=(8, 2)), sg.Button('Jogar',key='-JOGAR-',size=(8, 2))],
    ]

    return sg.Window('QUIZ DE CONHECIMENTO GERAIS', layout_inicial, size=(500, 500), element_justification='center', finalize=True)

evento, valores = janela_login().read()

if janela_login == '-JOGAR-':
    janela_login.close()
    
acertos = 0

for i, item in enumerate(quiz_data):
    pergunta = item['pergunta']
    alternativas = item['alternativas']
    resposta_correta = item['resposta_correta']
    explicacao = item['explicacao']
    
    layout = [
        [sg.Text(f'Pergunta {i+1}', font=('Calibri bold', 16)), sg.Image('imagempergunta.png')],
        [sg.Text(pergunta)],
        [sg.Radio(alternativas[0], 'alternativas'), sg.Radio(alternativas[1], 'alternativas'), sg.Radio(alternativas[2], 'alternativas'), sg.Radio(alternativas[3], 'alternativas'), sg.Radio(alternativas[4], 'alternativas')],
        [sg.Button('Responder')]
    ]
    
    janela = sg.Window('QUIZ DE CONHECIMENTO GERAIS', layout, finalize=True)
    
    evento, valores = janela.read()
    
    if evento == sg.WIN_CLOSED:
        break
    
    if valores['alternativas'] == resposta_correta:
        acertos += 1
        sg.popup('Resposta correta!', explicacao)
    else:
        sg.popup('Resposta incorreta!', explicacao)
        
    janela.close()
