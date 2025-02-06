import PySimpleGUI as sg            # dia 01/02/25
sg.theme('light grey 1')

menu_layout = [['Sobre'],
               ['Creditos']]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Bem - vindo ao Quiz de história ' , size = (60,2),font=('Arial' , 16 ))],
    [sg.Text('Digite seu nome :', size = (15,1), font= ('Arial' , 12)),sg.Input( size = (15,1))],
    [sg.Button('Sair', size=(8,2)), sg.Button('Continuar', size=(8,2))]
    
]

janela1 = sg.Window('QUIZ DE HISTÓRIA' , layout, size = (600,300), element_justification= 'center')
def Creditos():
    return sg.popup('Agradecimento','Creditos para os alunos Fulano, Ciclano , beutrano e jubisclano de licenciatura em computação')

def Sobre():
    return sg.popup( 'Sobre','O programa é um quiz de história para testar seu conhecimento na área')
    
while True:
    button,values = janela1.read()

    if button == 'Sair' or button == sg.WIN_CLOSED:
        break
    
    if button in ('Sobre'):
        Sobre()
    
    if button in ('Creditos'):
        Creditos()
        
janela1.close