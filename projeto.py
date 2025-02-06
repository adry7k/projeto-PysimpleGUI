import PySimpleGUI as sg            # dia 01/02/25
sg.theme('light grey 1')

menu_layout = [['Ajuda', ['Sobre']],
               ['Creditos']]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Bem - vindo ao Quiz de história ' ,justification='c', size = (60,2),font=('Arial' , 16 ))],
    [sg.Text('Digite seu nome:', size = (15,1)),sg.Input( size = (15,1))],
    [sg.Button('Sair', size=(10,2)), sg.Button('Continuar', size=(10,2))]
    
]

janela1 = sg.Window('QUIZ DE HISTÓRIA' , layout, size = (500,200))

def Sobre():
    sg.popup('Sobre', 'O programa é um quiz de história para testar seu conhecimento na área')
    
while True:
    button,values = janela1.read()

    if button == 'Sair' or button == sg.WIN_CLOSED:
        break
    
if button in ('Ajuda'):
    Sobre()
        
janela1.close


