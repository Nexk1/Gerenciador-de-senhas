import PySimpleGUI as sg


def tela_login():
  sg.theme('LightGrey6')
  layout = [[sg.Text('Email', size=(15, 1), font=(16))],
            [sg.InputText(font=16)],
            [sg.Text('Senha', size = (15,1), font=(16))],
            [sg.InputText(font=16, password_char='*')],
            [sg.Button('Fazer Login', size=(18), font=(8)), sg.Button('Cadastro', size=(21), font=(16))]]
  return sg.Window('janela_login', layout=layout, finalize=True)
#Tela de login
def tela_cadastro():
  sg.theme('LightGrey6')
  layout = [[sg.Text('Usuario desejado', size = (15,1), font=(16))], [sg.InputText(font=16)],
            [sg.Text('Senha desejada', size = (15,1), font=(16))], [sg.InputText(font=16, password_char='*')],
            [sg.Text('Confirmar Senha', size = (15,1), font=(16))], [sg.InputText(font=16, password_char='*')],
            [sg.Text('Email', size=(15, 1), font=(16))], [sg.InputText(font=16)],
            [sg.Button('Fazer Cadastro', size=(18), font=(8)),
             sg.Button('Voltar', size=(21), font=(8))]]
  return sg.Window('janela_cadastro', layout=layout, finalize=True)
#Tela de cadastro
def tela_logado(usuario):
    layout = [[sg.Text(f'Ola {usuario}', size = (15,1), font=(16))],
              [sg.Button('Adicionar Senha', size=(18), font=(8)), sg.Button('Excluir Senha', size=(18), font=(8)), sg.Button("Fazer logout", size=(18), font=(8))],
              [sg.Text("        Suas senhas abaixo      ")]]

    return sg.Window('janela_login', layout=layout, finalize=True)
#Tela Logado

def tela_add_senha():
    tam = [i for i in range(1, 32)]
    sg.theme('LightGrey6')
    layout = [[sg.Text('Adicione o Local abaixo:', size=(20, 1), font=(16))], [sg.InputText(font=(16))],
              [sg.InputText(font=(16)), sg.Checkbox("Senha Gerada"), sg.Spin(tam, initial_value=1, readonly=True, enable_events=True, size=3, background_color='#99ccff',text_color='Black', font=16)],
              [sg.Button('Cadastrar Senha', size=(21), font=(8)),
               sg.Button('Voltar', size=(21), font=(8))]]
    return sg.Window('janela_cadastro', layout=layout, finalize=True)