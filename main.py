import PySimpleGUI as sg
import sqlite3 as sql
#Bunda
import bcrypt
import bcrypt as bc

#----------------------------------------------------------Variaveis e Coisas importantes---------------------------------------

con = sql.connect("Banco_de_dados.db")
user_con = sql.connect("Banco_de_dados_Users.db")

cursor = con.cursor()
user_cursor = user_con.cursor()

login_sen = ""
#--------------------------------------------------------------Funcionamento Tecnico-------------------------------------------------
def cript_senha(passwordi, checkinp):
    password = passwordi
    check = checkinp
    password = password.encode('utf-8')
    hashed = bc.hashpw(password, bc.gensalt(10))
    check = check.encode('utf-8')

    if bc.checkpw(check, hashed):
        return hashed
    else:
        sg.popup("Senhas Diferentes!")


def reconhecer_cript(senhai, hashedi):
    global janela3
    senha = str(senhai)
    senha = senha.encode('utf-8')

    hashed = hashedi
    hashed = hashed.strip('b')
    hashed = hashed.replace("'", "")
    hashed = hashed.encode('utf-8')

    if bcrypt.checkpw(senha, hashed):
        janela3 = tela_logado()
        janela1.hide()
    else:
        sg.popup("Senha Errada!")

def confirm_cadastro():
    cripto = cript_senha(senha, check)

    try:
        user_cursor.execute(f'INSERT INTO "Usuarios" VALUES ("{usuario}", "{cripto}")')
        user_con.commit()
    except:
        sg.popup("Usuário já Cadastrado")

    if window == janela2 and event == "Fazer Cadastro":
        janela2.hide()
        janela1.un_hide()
        sg.popup("Seu Cadastro foi concluido")


def fazer_login():
        global senha
        global usuario
        global check
        global login_sen

        usuario = values[0]
        senha = values[1]

        user_cursor.execute(f"SELECT senha FROM 'Usuarios' WHERE usuario = '{usuario}'")
        login = user_cursor.fetchall()
        login_sen = login[0][0]

        return reconhecer_cript(senha, login_sen)


#--------------------------------------------------------------Layout das telas------------------------------------------------


def tela_login():
  sg.theme('DarkGray')
  layout = [[sg.Text('Usuario', size = (15,1), font=(16))],
            [sg.InputText(font=16)],
            [sg.Text('Senha', size = (15,1), font=(16))],
            [sg.InputText(font=16, password_char='*')],
            [sg.Button('Fazer Login', size=(18), font=(8)), sg.Button('Cadastro', size=(21), font=(16))]]
  return sg.Window('janela_login', layout=layout, finalize=True)


def tela_cadastro():
  sg.theme('DarkGray')
  layout = [[sg.Text('Usuario desejado', size = (15,1), font=(16))], [sg.InputText(font=16)],
            [sg.Text('Senha desejada', size = (15,1), font=(16))], [sg.InputText(font=16, password_char='*')],
            [sg.Text('Confirmar Senha', size = (15,1), font=(16))], [sg.InputText(font=16, password_char='*')],
            [sg.Button('Fazer Cadastro', size=(18), font=(8)),
             sg.Button('Voltar', size=(21), font=(8))]]
  return sg.Window('janela_cadastro', layout=layout, finalize=True)

def tela_logado():
    if window == janela1:
        usuario = values[0]
    layout = [[sg.Text(f'Ola {usuario}')],
              [sg.Button('Adicionar Senha'), sg.Button('Excluir Senha'), sg.Button("Fazer logout")],
              [sg.Text("        Suas senhas abaixo      ")]
]

    return sg.Window('janela_login', layout=layout, finalize=True)



janela1, janela2, janela3, janela4 = tela_login(), None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Cadastro':
        janela2 = tela_cadastro()
        janela1.hide()
    if window == janela2 and event == sg.WIN_CLOSED:
        break

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == 'Fazer Cadastro':
        usuario = values[0]
        senha = values[1]
        check = values[2]

        if usuario == "":
            sg.popup('Erro, Digite um usuario')
        elif senha == "":
            sg.popup('Erro, Digite uma senha')
        elif check == "":
            sg.popup('Erro, Digite a senha igual')


        senha_num = len(senha)

        if senha_num < 8:
            sg.popup('Senha muito pequena, tente outra!')

        else:
            confirm_cadastro()

    if window == janela1 and event == "Fazer Login":
        fazer_login()


    if window == janela3 and event == sg.WIN_CLOSED:
        break

    if window == janela3 and event == "Fazer logout":
        janela3.hide()
        janela1.un_hide()

    if window == janela4 and event == "Adicionar Senha":
        janela1