import sqlite3
from tabulate import tabulate

BD_PATH = '/storage/emulated/0/Documents/SQL/Projeto2/meu_aprendizado2.db'

#FUNÇÃO 1: APENAS LISTAS:
def listar_usuarios():
  conexao = sqlite3.connect(BD_PATH)
  cursor = conexao.cursor()
  
  cursor.execute("SELECT * FROM login")
  dados = cursor.fetchall()
  
  colunas = ["ID", "NOME", "E-MAIL"]
  print("\n" + tabulate(dados, headers = colunas, tablefmt = "grid"))
  
  cursor.close()
  conexao.close()
  

# FUNÇÃO 2: GERENCIA MENU E CADASTRO:
def sistema_de_cadastro():
  conexao = sqlite3.connect(BD_PATH)
  cursor = conexao.cursor()
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS login(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE
  )
  """)
  
  print(f"{' MENU DE CADASTRO ':=^30}")
  while True:
    opcao = input('Deseja cadastrar (C), Listar (L), ou sair (S): ').upper()
    
    if opcao == 'C':
      nome_usuario = input('Digite um nome: ').upper()
      email_usuario = input('Digite um e-mail: ').lower()
      
      try:
        cursor.execute("""
        INSERT INTO login (nome, email)
        VALUES (?, ?)""", (nome_usuario, email_usuario))
        conexao.commit()
        print(f'\033[1;32m{nome_usuario} foi guardado no SQLite!\033[m')
        
      except sqlite3.IntegrityError:
        print('\033[1;31mERROR!!! Este e-mail já existe\033[m')
      
      except Exception as e:
        print(f'\033[1;31mOcorreu um erro inesperado: {e} \033[m')
        
    elif opcao == 'L':
      listar_usuarios()
    
    elif opcao == 'S':
      print('\033[1;33mSaindo do sistema... Até logo!\033[m')
      break
      
    else:
      print('\033[1;31mOpção invalida! Digite (C) para cadastrar, (L) para ver lista ou (S) para sair\033[m')
  cursor.close()
  conexao.close()
  
sistema_de_cadastro()