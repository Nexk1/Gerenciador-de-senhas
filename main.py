#banco de dados e layout
import PySimpleGUI as sg
import sqlite3 as sql

#criptografia
import bcrypt
import bcrypt as bc

#minhas funcoes
import layout as lo
import functions as fc

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
        if window == janela1:
            email = values[0]
            user_cursor.execute(f'SELECT usuario FROM Usuarios WHERE email = "{email}"')
            usuario = user_cursor.fetchall()
            usuario = usuario[0][0]
        janela3 = lo.tela_logado(usuario)
        janela1.hide()
    else:
        sg.popup("Senha Errada!")

def confirm_cadastro():
    cripto = cript_senha(senha, check)

    user_cursor.execute(f'CREATE TABLE IF NOT EXISTS "Usuarios" ("usuario" VARCHAR(255), "senha" VARCHAR(255), "email" VARCHAR(255))')
    user_cursor.execute(f'INSERT INTO "Usuarios" VALUES ("{usuario}", "{cripto}", "{email}")')
    user_con.commit()

    if window == janela2 and event == "Fazer Cadastro":
        cursor.execute(f'CREATE TABLE IF NOT EXISTS "{usuario}"("Locais" VARCHAR(255), "Senhas" VARCHAR(255))')
        con.commit()
        janela2.hide()
        janela1.un_hide()
        sg.popup("Seu Cadastro foi concluido")


def fazer_login():
        global senha
        global email
        global check
        global login_sen

        email = values[0]
        senha = values[1]

        user_cursor.execute(f"SELECT senha FROM 'Usuarios' WHERE email = '{email}'")
        login = user_cursor.fetchall()
        login_sen = login[0][0]
        return reconhecer_cript(senha, login_sen)

def add_senha():
    pass


#--------------------------------------------------------------Layout das telas------------------------------------------------

janela1, janela2, janela3, janela4, janela5= lo.tela_login(), None, None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Cadastro':
        janela2 = lo.tela_cadastro()
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
        email = values[3]

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
        email = values[0]
        senha = values[1]

        if senha == "" and email == "":
            sg.popup("Preencha os campos!")
        elif email == "":
            sg.popup("Coloque o email")
        elif senha == "":
            sg.popup("Coloque a senha!")
        else:
            fazer_login()


    if window == janela3 and event == sg.WIN_CLOSED:
        break

    if window == janela3 and event == "Fazer logout":
        janela3.hide()
        janela1.un_hide()

    if window == janela3 and event == "Adicionar Senha":
        janela4 = lo.tela_add_senha()

    if window == janela4 and event == sg.WIN_CLOSED:
        janela4.hide()

    if window == janela4 and event == 'Voltar':
        janela4.hide()
