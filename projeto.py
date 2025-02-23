import PySimpleGUI as sg
from perguntas import quiz_data

sg.theme('light blue')

menu_layout = [['Sobre'], ['Créditos']]

# Criar a janela inicial com o botão "Jogar" e a imagem
layout_inicial = [
    [sg.Menu(menu_layout)],
    [sg.Text()],
    [sg.Text('Bem-vindo ao QUIZ de conhecimentos gerais', font=('Calibri', 16, 'bold'), justification='center')],
    [sg.Text()],
    [sg.Image(filename="question200.png")],  # Centraliza a imagem no topo
    [sg.Text()],
    [sg.Text()],
    [sg.Button("Sair", key='-SAIR-', button_color=("white", "#009EE3"), size=(15, 2), border_width=0, font=("Arial", 10)), 
     sg.Button("Jogar", key="-JOGAR-", button_color=("white", "#009EE3"), size=(15, 2), border_width=0, font=("Arial", 10))]
]

# Criar a janela inicial
janela = sg.Window("Quiz de Conhecimentos Gerais", layout_inicial, size=(800, 500), resizable=True, element_justification="center")

# Funções para exibir popups
def Creditos():
    sg.popup('Agradecimento', 'Créditos para os alunos:', 'CICLANO', 'BELTRANO', 'JUBISCLANO', 'Alunos de Licenciatura em Computação')

def Sobre():
    sg.popup('Sobre', 'O programa é um quiz de conhecimentos gerais para testar seu nível de inteligência')

# Loop de eventos da janela inicial
while True:
    evento, valores = janela.read()
    
    if evento == sg.WINDOW_CLOSED or evento == '-SAIR-':
        janela.close()
        exit()

    if evento == 'Sobre':
        Sobre()

    if evento == 'Créditos':
        Creditos()

    if evento == "-JOGAR-":
        break  # Sai do loop e inicia o quiz

janela.close()  # Fecha a janela inicial antes de iniciar o quiz

# Iniciar contagem de acertos
acertos = 0

# Loop para as perguntas
for i, item in enumerate(quiz_data):
    layout_pergunta = [
        [sg.Menu(menu_layout)],
        [sg.Text(item["pergunta"], font=("Arial", 14, "bold"), justification="center")]
    ]
    
    # Adiciona as opções de resposta
    for alternativa in item["alternativas"]:
        layout_pergunta.append([
            [sg.Text()],
            [sg.Button(alternativa, key=alternativa, size=(40, 2), button_color=("white", "#009EE3"), border_width=0)]
            ])

    # Criar a janela para cada pergunta
    janela = sg.Window("Quiz de conhecimentos gerais", layout_pergunta, size=(800, 500), resizable=True, element_justification="center")

    while True:
        evento, valores = janela.read()

        if evento in (sg.WINDOW_CLOSED, '-SAIR-'):
            janela.close()
            exit()

        if evento == 'Sobre':
            Sobre()

        if evento == 'Créditos':
            Creditos()

        if evento in item["alternativas"]:
            if evento == item["resposta_correta"]:
                acertos += 1
                sg.popup(f"Resposta correta! {evento}", item["explicacao"], title="Resultado")
            else:
                sg.popup(f"Resposta errada!", item["explicacao"], title="Resultado")
            break  # Sai do loop e passa para a próxima pergunta

    janela.close()  # Fecha a janela da pergunta atual antes de ir para a próxima

# Exibir pontuação final
sg.popup(f"Quiz finalizado! Você acertou {acertos} de {len(quiz_data)} perguntas.", title="Resultado Final")
