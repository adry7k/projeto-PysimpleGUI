import PySimpleGUI as sg
from perguntas import quiz_data




# Criar a janela inicial com o botão "Jogar" e a imagem


layout_inicial = [
    [sg.Push(), sg.Image(filename="question200.png", size=(128, 128)), sg.Push()],  # Centraliza a imagem no topo
    [sg.Push(), sg.Button("Jogar", key="start_button", button_color=("white", "#009EE3"), size=(15, 2), border_width=0, font=("Arial", 10)), sg.Push()]
]

# Janela inicial
janela = sg.Window("Quiz PySimpleGUI", layout_inicial, size=(500, 400), resizable=True, element_justification="center")

# Esperar o evento "Jogar" para iniciar o quiz
evento, valores = janela.read()

# Fechar a janela inicial quando "Jogar" for pressionado
if evento == "start_button":
    janela.close()

acertos = 0

# Loop para as perguntas
for i, item in enumerate(quiz_data):
    layout = [
        [sg.Text(item["pergunta"], font=("Arial", 14, "bold"), justification="center")]
    ]
    
    # Adiciona as opções de resposta
    for opcao in item["opcoes"]:
        layout.append([sg.Button(opcao, key=opcao, size=(40, 2), button_color=("white", "#009EE3"), border_width=0)])

    # Janela para cada pergunta, sem a imagem
    janela = sg.Window("Quiz PySimpleGUI", layout, size=(500, 400), resizable=True, element_justification="center")

    while True:
        evento, valores = janela.read()
        
        if evento == sg.WINDOW_CLOSED:
            janela.close()
            exit()

        if evento in item["opcoes"]:
            if evento == item["resposta"]:
                acertos += 1
                sg.popup(f"Resposta correta! {evento}", title="Resultado")
            else:
                sg.popup(f"Errado! A resposta correta era {item['resposta']}", title="Resultado")
            break  # Sai do loop da pergunta atual

    janela.close()  # Fecha a janela antes de ir para a próxima pergunta

# Exibir pontuação final
sg.popup(f"Quiz finalizado! Você acertou {acertos} de {len(quiz_data)} perguntas.", title="Resultado Final")