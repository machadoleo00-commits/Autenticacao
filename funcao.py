import database
import werkzeug.security



def cadastro(username, senha):
    senha_hash = werkzeug.security.generate_password_hash(senha)
    return database.adicionar_usuario(username, senha_hash)
