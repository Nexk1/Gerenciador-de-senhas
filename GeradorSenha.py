import secrets
import string

def gerador(senhag):
    letras = string.ascii_letters
    digitos = string.digits
    chars_espec = string.punctuation
    alfabeto = letras + digitos + chars_espec

    senha = ""
    tamanho_senha = senhag

    for i in range(tamanho_senha):
        senha += "".join(secrets.choice(alfabeto))
    print(senha)
