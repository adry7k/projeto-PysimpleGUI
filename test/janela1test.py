import PySimpleGUI as sg            # dia 08/02/25
sg.theme('light gray 1')

menu_layout = [['Sobre'],
               ['Creditos']]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Bem-vindo ao QUIZ de conhecimentos gerais ',font=('Arial', 16 ),expand_x=True, text_color = 'White', background_color= 'Grey', size=50, justification='c' )],
    [sg.Text()],
    [sg.Image(filename='question200.png')],
    [sg.Text()],
    [sg.Text()],
    [sg.Text()],
    [sg.Text('Digite seu nome :', size = (15,1), font= ('Arial' , 12)),sg.Input( size = (20,1))],
    [sg.Text()],
    [sg.Push(),sg.Button('Sair', size=(8,2)), sg.Button('Continuar', size=(8,2))]
    
]

janela1 = sg.Window('QUIZ DE HISTÓRIA' , layout, size = (500,500), element_justification= 'center')
def Creditos():
    return sg.popup('Agradecimento','Creditos para os alunos:','CICLANO', 'BELTRANO', 'JUBISCLANO', 'Alunos de licenciatura em computação')

def Sobre():
    return sg.popup( 'Sobre','O programa é um quiz de conhecimentos gerais para testar seu nivel de inteligência.                                           DIVIRTA-SE!!!!!!')
    
while True:
    button,values = janela1.read()

    if button == 'Sair' or button == sg.WIN_CLOSED:
        break
    
    if button in ('Sobre'):
        Sobre()
    
    if button in ('Creditos'):
        Creditos()
        
janela1.close