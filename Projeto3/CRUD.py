import sqlite3
from tabulate import tabulate


BD_PATH = "/storage/emulated/0/Documents/SQL/Aprendendo/CRUD/sistema_treino.db"

#1. CREATE (Inserir Usuario)
def criar_usuario(nome, email):
  with sqlite3.connect(BD_PATH) as conexao:
    cursor = conexao.cursor()
    try:
      cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?,?)", (nome, email))
      conexao.commit()
      
      print(f'\n\033[1;32mO nome: \033[1;35m{nome}\033[m \033[1;32me o e-mail: \033[1;34m{email}\033[m \033[1;32mfoi guardado no SQLite!\033[m')
      
    except sqlite3.IntegrityError:
      print(f'\033[1;31mEmail já existente no Banco de Dados!\033[m')
      
    except Exception as e:
      print('\n\033[1;31mOcorreu um erro inesperado\033[m')


#2. READ (Ler todos os Usuarios)
def ler_usuarios():
  with sqlite3.connect(BD_PATH) as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    
    resultado = cursor.fetchall()
    colunas = ['ID', 'NOME', 'E-MAIL']
    print('\n' + tabulate(resultado, headers=colunas, tablefmt="fancy_grid"))
    
    return resultado

#UPDATE (Mudar o E-mail de um Usario)
def atualizar_email(id_usuario, novo_nome, novo_email):
  with sqlite3.connect(BD_PATH) as conexao:
    cursor = conexao.cursor()
    
    try:
      cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, id_usuario))
      
      if cursor.rowcount == 0:
        print(f'\n\033[1;31mAviso: O usuário com o ID: \033[1;34m{id_usuario}\033[m \033[1;31mnão foi encontrado. Nada foi alterado.\033[m')
      else:
        print(f'\n\033[1;32mSucesso! \033[1;34m{cursor.rowcount}\033[m \033[1;32mlinha(s) atualizada(s)\033[m')
        conexao.commit()
      
    except sqlite3.IntegrityError:
      print(f'\n\033[1;31mEmail já existente no Banco de Dados!\033[m')
      
    except Exception as e:
      print('\n\033[1;31mOcorreu um erro inesperado\033[m')
    

#Delete (apagar um usuario pelo ID)
def deletar_usuario(id_usuario):
  with sqlite3.connect(BD_PATH) as conexao:
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    
    if cursor.rowcount == 0:
      print(f'\n\033[1;31mERROR: O ID \033[1;34m{id_usuario}\033[m \033[1;31mnão existe! Nada foi removido...\033[m')
    else:
      print(f'\n\033[1;32mID \033[1;34m{id_usuario}\033[m \033[1;32mfoi removido!\033[m')
      conexao.commit()
      
# EXECUÇÃO DE TESTE
def tabela_CRUD():
  with sqlite3.connect(BD_PATH) as conexao:
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
    )
    """)
    
    print(f"{' MENU DE CADASTRO ':=^30}")
    while True:
      opcao = input("""\n
      Digite as letras para as execucões:
      (C) - Deseja cadastrar
      (L) - Ler Usuario 
      (A) - Atualizar Informações
      (D) - Deletar Informações
      (S) - Sair
      Opcão: """).upper()
      
      if opcao == 'C':
        nome = input('\n\033[1;33mDigite um nome:\033[m ').upper()
        email = input('\033[1;33mDigite um email:\033[m ').lower()
        criar_usuario(nome, email)
      
      elif opcao == 'L':
        ler_usuarios()
      
      elif opcao == 'A':
        id_usuario = int(input('\n\033[1;33mQual ID de usuario você quer modificar:\033[m '))
        
        novo_nome = input('\033[1;33mDigite o nome do novo Usuário:\033[m ').upper()
        
        novo_email = input('\033[1;33mDigite o novo Email do Usuário:\033[m ').lower()
        
        atualizar_email(id_usuario, novo_nome, novo_email)
      
      elif opcao == 'D':
        id_usuario = int(input('\n\033[1;33mDigite o numero de ID que você quer deletar:\033[m '))
    
        deletar_usuario(id_usuario)
        
      elif opcao == 'S':
        print('\n\033[1;34mSaindo do Sistema! Até logo...\033[m')
        break
      
      else:
        print('\n\033[1;31mERROR! Dados invalidos, tente novamete... \033[m')

tabela_CRUD()