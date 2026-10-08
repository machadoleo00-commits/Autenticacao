import sqlite3

conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    hash TEXT NOT NULL
)""")
conexao.commit()
conexao.close()

def carregar_usuarios(): 
    conexao = sqlite3.connect('database.db')
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM users")
    retorno = [dict(user) for user in cursor.fetchall()]
    conexao.close()
    return retorno

def carregar_usuario_por_username(username):
    conexao = sqlite3.connect('database.db')
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    retorno = cursor.fetchone()
    conexao.close()
    return dict(retorno) if retorno else None

def carregar_usuario_por_id(id_usuario):
    conexao = sqlite3.connect('database.db')
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (id_usuario,))
    retorno = cursor.fetchone()
    conexao.close()
    return dict(retorno) if retorno else None

def adicionar_usuario(username, senha_hash):
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (username, senha_hash))
        conexao.commit()
        print(f"Usuário {username} adicionado com sucesso.")
    except sqlite3.IntegrityError:
        print(f"Usuário {username} já existe.")
        return False  
    finally:
        conexao.close()
    return True
