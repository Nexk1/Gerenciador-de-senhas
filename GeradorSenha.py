import secrets
import string


class tam_senha():
    def __init__(self):
        letras = string.ascii_letters
        digitos = string.digits
        chars_espec = string.punctuation
        alfabeto = letras + digitos + chars_espec

        senha = ""
        tamanho_senha = self

        for i in range(tamanho_senha):
            senha += "".join(secrets.choice(alfabeto))
        print(senha)
