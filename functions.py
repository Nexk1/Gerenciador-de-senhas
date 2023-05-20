import PySimpleGUI as sg
import sqlite3 as sql
import bcrypt as bc
import layout as lo

con = sql.connect("Banco_de_dados.db")
user_con = sql.connect("Banco_de_dados_Users.db")

cursor = con.cursor()
user_cursor = user_con.cursor()

window, event, values = sg.read_all_windows()



