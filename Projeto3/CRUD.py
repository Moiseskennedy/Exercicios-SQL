import sqlite3
from tabulate import tabulate


BD_PATH = "sistema_treino.db"

#1. CREATE (Inserir Usuario)
def criar_usuario(nome, email):
  with sqlite3.connect(BD_PATH) as conexao:
    cursor = conexao.cursor()
    try:
      cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?,?)", (nome, email))
      conexao.commit()
      
      print(f'O nome: {nome} e o e-mail{email} foi guardado no SQLite!')
      
    except sqlite3.IntegrityError:
      print(f'Email já existente no Banco de Dados!')
      
    except Exception as e:
      print('Ocorreu um erro inesperado')


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
      conexao.commit()
      
      if cursor.rowcount == 0:
        print(f'Aviso: O usuário com o ID {id_usuario} não foi encontrado. Nada foi alterado.')
      else:
        print(f"Sucesso! {cursor.rowcount} linha(s) atualizada(s)")
      
    except sqlite3.IntegrityError:
      print(f'Email já existente no Banco de Dados!')
      
    except Exception as e:
      print('Ocorreu um erro inesperado')
    

#Delete (apagar um usuario pelo ID)
def deletar_usuario(id_usuario):
  with sqlite3.connect(BD_PATH) as conexao:
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conexao.commit()
    
    if cursor.rowcount == 0:
      print(f'ERROR: O ID {id_usuario} não existe! Nada foi removido...')
    else:
      print(f'ID {id_usuario} foi removido!')
    
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
        nome = input('Digite um nome: ').upper()
        email = input('Digite um email: ').lower()
        criar_usuario(nome, email)
      
      elif opcao == 'L':
        ler_usuarios()
      
      elif opcao == 'A':
        id_usuario = int(input('Qual ID de usuario você quer modificar: '))
        
        novo_nome = input('Digite o nome do novo Usuário: ').upper()
        
        novo_email = input('Digite o novo Email do Usuário: ').lower()
        
        atualizar_email(id_usuario, novo_nome, novo_email)
      
      elif opcao == 'D':
        id_usuario = int(input('Digite o numero de ID que você quer deletar: '))
    
        deletar_usuario(id_usuario)
        
      elif opcao == 'S':
        print('Saindo do Sistema! Até logo...')
        break

tabela_CRUD()