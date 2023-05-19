import PySimpleGUI as sg

def tela_login():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Usuario')],
        [sg.InputText()],
        [sg.Text('Senha')],
        [sg.InputText()],
        [sg.Text('Nome da Tabela')],
        [sg.InputText()],
        [sg.Button('Fazer login'), sg.Button('Cadastro')]
    ]
    return sg.Window('janela_login', layout=layout, finalize=True)


def tela_cadastro():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Usuario desejado \n')],
        [sg.InputText()],
        [sg.Text('Senha desejada \n')],
        [sg.InputText()],
        [sg.Text('Nome da Tabela desejado \n')],
        [sg.InputText()],
        [sg.Button('Fazer Cadastro'), sg.Button('Voltar')]
    ]
    return sg.Window('janela_cadastro', layout=layout, finalize=True)