import hashlib
import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('familycare.db')
cursor = conn.cursor()

# Criptografia de senha com MD5 para cadastrar no banco de dados
def criptografar_senha(senha):
    return hashlib.md5(senha.encode()).hexdigest()

# Método de login para o idoso
def login_idoso(conn, nome, senha):
    cursor = conn.cursor()
    senha_hash = criptografar_senha(senha)  # Criptografa a senha fornecida e compara no banco
    cursor.execute('''
        SELECT * FROM Idosos WHERE nome = ? AND senha = ?
    ''', (nome, senha_hash))
    
    idoso = cursor.fetchone()
    if idoso:
        print("Login bem-sucedido.")
        return True
    else:
        print("Nome ou senha incorretos.")
        return False

# Método de login para o cuidador
def login_cuidador(conn, nome, senha):
    cursor = conn.cursor()
    senha_hash = criptografar_senha(senha)  # Criptografa a senha fornecida e compara no banco
    cursor.execute('''
        SELECT * FROM Cuidadores WHERE nome = ? AND senha = ?
    ''', (nome, senha_hash))
    
    idoso = cursor.fetchone()
    if idoso:
        print("Login bem-sucedido.")
        return True
    else:
        print("Nome ou senha incorretos.")
        return False


# Menu para escolher o tipo de usuário para o login
escolha = int(input("\nEscolha o tipo de usuário que deseja realizar login: \n1 - Idoso\n2 - Cuidador\n"))

if escolha == 1:
    nome = input("\nInforme seu nome: ")
    senha = input("Informe sua senha: ")
    login_idoso(conn, nome, senha)
elif escolha == 2:
    nome = input("\nInforme seu nome: ")
    senha = input("Informe sua senha: ")
    login_cuidador(conn, nome, senha)
else:
    print("Você não escolheu uma opção válida.\n")
