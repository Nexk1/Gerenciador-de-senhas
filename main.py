#banco de dados e layout
import PySimpleGUI as sg
import sqlite3 as sql

#criptografia
import bcrypt
import bcrypt as bc
import secrets
import string

#minhas funcoes
import layout as lo

#----------------------------------------------------------Variaveis e Coisas importantes---------------------------------------

con = sql.connect("Banco_de_dados.db")
user_con = sql.connect("Banco_de_dados_Users.db")

cursor = con.cursor()
user_cursor = user_con.cursor()

login_sen = ""
#--------------------------------------------------------------Funcionamento Tecnico-------------------------------------------------
def gerador(senhasize):
    letras = string.ascii_letters
    digitos = string.digits
    chars_espec = string.punctuation
    alfabeto = letras + digitos + chars_espec

    senha_gerada = ""
    tamanho_senha = int(senhasize)

    for i in range(tamanho_senha):
        senha_gerada += "".join(secrets.choice(alfabeto))

    return senha_gerada

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


def mostrar_senha():
    dadosbd = cursor.execute(f"SELECT * FROM {email}")
    dados = dadosbd.fetchone()
    dados = str(dados)
    dados = dados.strip("()")
    dados = dados.replace("'", "")
    dados = dados.replace(",", "      -->      ")

    print(dados)
    for i in dadosbd:
        dados = i
        dados = str(dados)
        dados = dados.strip("()")
        dados = dados.replace("'", "")
        dados = dados.replace(",", "      -->      ")

        print(dados)

def reconhecer_cript(senhai, hashedi):
    global telalogado
    senha = str(senhai)
    senha = senha.encode('utf-8')

    hashed = hashedi
    hashed = hashed.strip('b')
    hashed = hashed.replace("'", "")
    hashed = hashed.encode('utf-8')

    if bcrypt.checkpw(senha, hashed):
        if window == lwin:
            email = values[0]
            user_cursor.execute(f'SELECT usuario FROM Usuarios WHERE email = "{email}"')
            usuario = user_cursor.fetchall()
            usuario = usuario[0][0]
        telalogado = lo.tela_logado(usuario)
        lwin.hide()
        mostrar_senha()
    else:
        sg.popup("Senha Errada!")

def confirm_cadastro():
    cripto = cript_senha(senha, check)

    user_cursor.execute(f'CREATE TABLE IF NOT EXISTS "Usuarios" ("usuario" VARCHAR(255), "senha" VARCHAR(255), "email" VARCHAR(255))')
    user_cursor.execute(f'INSERT INTO "Usuarios" VALUES ("{usuario}", "{cripto}", "{email}")')
    user_con.commit()

    if window == cadwin and event == "Fazer Cadastro":
        if cripto:
            cursor.execute(f'CREATE TABLE IF NOT EXISTS "{email}"("Locais" VARCHAR(255), "Senhas" VARCHAR(255))')
            con.commit()
            cadwin.hide()
            lwin.un_hide()
            sg.popup("Seu Cadastro foi concluido")
        else:
            pass


def fazer_login():
        global senha
        global email
        global check
        global login_sen

        email = values[0]
        senha = values[1]

        user_cursor.execute(f"SELECT senha FROM 'Usuarios' WHERE email = '{email}'")
        login = user_cursor.fetchall()
        hashed_sen = login[0][0]

        return reconhecer_cript(senha, hashed_sen)


def add_senha(local, senhaU, checkbox, num):
    global email
    if checkbox == True:
        senhauser = gerador(num)
        cadpass.hide()
        sg.popup("Senha Cadastrada!")
    else:
        senhauser = senhaU
        cadpass.hide()
        sg.popup("Senha Cadastrada!")

    cursor.execute(f'INSERT INTO "{email}" VALUES("{local}", "{senhauser}")')
    con.commit()


#--------------------------------------------------------------Layout das telas------------------------------------------------

lwin, cadwin, telalogado, cadpass, detpass = lo.tela_login(), None, None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == lwin and event == sg.WIN_CLOSED:
        break
    if window == lwin and event == 'Cadastro':
        cadwin = lo.tela_cadastro()
        lwin.hide()
    if window == cadwin and event == sg.WIN_CLOSED:
        break

    if window == cadwin and event == 'Voltar':
        cadwin.hide()
        lwin.un_hide()

    if window == cadwin and event == 'Fazer Cadastro':
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

    if window == lwin and event == "Fazer Login":
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


    if window == telalogado and event == sg.WIN_CLOSED:
        break

    if window == telalogado and event == "Fazer logout":
        telalogado.hide()
        lwin.un_hide()

    if window == telalogado and event == "Adicionar Senha":
        cadpass = lo.tela_add_senha()

    if window == telalogado and event == "↻":
        window.FindElement("_output_").Update("")
        mostrar_senha()

    if window == cadpass and event == "Cadastrar Senha":
        local = values[0]
        senhaU = values[1]
        checkbox = values[2]
        numero = values[3]
        add_senha(local, senhaU, checkbox, numero)

    if window == cadpass and event == sg.WIN_CLOSED:
        cadpass.hide()

    if window == cadpass and event == 'Voltar':
        cadpass.hide()

    if window == telalogado and event == "Excluir Senha":
        lo.tela_delete_pass()