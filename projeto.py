import PySimpleGUI as sg
import random
from perguntas import quiz_data




sg.theme('Reddit')  # Define o tema da janela

menu_layout = [['Sobre'], ['Créditos']]

# Criar a janela inicial com o botão "Jogar" e a imagem
layout_inicial = [
    [sg.Menu(menu_layout)],
    [sg.Image(filename="acertou4.png", pad = (35,20)),sg.Text('Bem-vindo ao QUIZ de conhecimentos gerais', font=('Calibri', 17, 'bold'), justification='center', text_color= 'green'), sg.Image(filename="pensativo2.png", pad = (35,20))],
    [sg.Image(filename="question300.png", expand_x=True)],  
    [sg.Text()],
    [sg.Text()],
    [sg.Button("Sair", key='-SAIR-', size=(15, 2),button_color= 'green' , font=("Arial", 10)),
     sg.Button("Iniciar", key="-INICIAR-", size=(15, 2), button_color= 'green' , font=("Arial", 10))],
    [sg.Image(filename="ufra100.png",pad=(35,20)),sg.Push()],
]

# Criar a janela inicial
janela = sg.Window("Quiz de Conhecimentos Gerais", layout_inicial, size=(850, 570), resizable=True, element_justification="center")

# Funções para exibir popups
def Creditos():
    sg.popup( 'Créditos para os alunos:', 'Adriano Messias', 'Vinicius Coelho', 'Danielly Ribeiro','Geovanna Moy','Yamara Barbosa' ,'Alunos de Licenciatura em Computação', title='Créditos')

def Sobre():
    sg.popup( 'O objetivo do programa é testar seus conhecimentos nas demais aréas do saber, com a finalidade de ajudar em seu desenvolvimento intelectual. O programa é composto por 15 perguntas, sendo elas de Humanas, Ciências e Matemática. DIVIRTA-SE!!!.', title='Sobre')

# Loop de eventos da janela inicial
while True:
    evento, valores = janela.read()
    
    if evento == sg.WINDOW_CLOSED or evento == '-SAIR-':
        janela.close() # Fecha a janela
        exit()
        
    # Verifica se o usuário clicou no menu "Sobre" ou "Créditos"
    if evento == 'Sobre':
        Sobre()

    if evento == 'Créditos':
        Creditos()

    if evento == "-INICIAR-":
        break  # Sai do loop e inicia o quiz

janela.close()  # Fecha a janela inicial antes de iniciar o quiz

# Iniciar contagem de acertos
acertos = 0


limite_das_perguntas = random.sample(quiz_data, 15) #busca 15 perguntas aleatórias


# Loop para as perguntas
for i, item in enumerate(limite_das_perguntas):
    layout_pergunta = [
        [sg.Menu(menu_layout)],
        [sg.Text(item["pergunta"], font=("Arial", 14, "bold"), justification="center"), sg.Image(filename="que2.png")],
         ]
        

    
    # Adiciona as opções de resposta
    for alternativa in item["alternativas"]:
        layout_pergunta.append([
            [sg.Text()],
            [sg.Button(alternativa, key=alternativa, button_color='green' ,size=(48, 2))],
        ]
            )
        
        

    # Criar a janela para cada pergunta
    janela = sg.Window("Quiz de conhecimentos gerais", layout_pergunta, size=(850, 570), resizable=True, element_justification="center")
    


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
                sg.popup(f"Resposta correta!", item["explicacao"], title="Resultado")
            else:
                sg.popup(f"Resposta errada!", item["explicacao"], title="Resultado")
            break  # Sai do loop e passa para a próxima pergunta

    janela.close()  # Fecha a janela da pergunta atual antes de ir para a próxima

# Exibir pontuação final

if acertos == 15:
    sg.popup(f"Meus Parabéns!!! Você acertou {acertos} das {len(limite_das_perguntas)} perguntas!","Você é uma pessoa muito inteligente! sabia? ;)", title="Resultado Final")
    
if acertos < 15 and acertos >= 10:
    sg.popup(f"Parabéns! Você acertou {acertos} de {len(limite_das_perguntas)} das perguntas.","Você se saiu muito bem!", title="Resultado Final")

if acertos < 10 and acertos >= 7:
    sg.popup(f"Bom trabalho! Você acertou {acertos} de {len(limite_das_perguntas)} das perguntas.","Você pode melhorar! não desista.", title="Resultado Final")
    
if acertos < 7 and acertos >= 5:
    sg.popup(f"Você acertou {acertos} de {len(limite_das_perguntas)} das perguntas.","Você precisa estudar mais! não perca o foco.", title="Resultado Final")

if acertos < 5:
    sg.popup(f"Você acertou {acertos} de {len(limite_das_perguntas)} das perguntas.","Você se saiu muito mal! :(", title="Resultado Final")

