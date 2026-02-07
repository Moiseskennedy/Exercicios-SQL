import sqlite3
from tabulate import tabulate

BD_PATH = 'meu_aprendizado2.db'

# FUNÇÃO 1: APENAS LISTAR
def listar_usuarios():
    with sqlite3.connect(BD_PATH) as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM login")
        
        dados = cursor.fetchall()
        colunas = ["ID", "NOME", "E-MAIL"]
        print("\n" + tabulate(dados, headers=colunas, tablefmt="fancy_grid"))
        
        return dados

# FUNÇÃO 2: GERENCIA MENU E CADASTRO
def sistema_de_cadastro():
    with sqlite3.connect(BD_PATH) as conexao:
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
            opcao = input('\nDeseja cadastrar (C), Listar (L), ou sair (S): ').upper()
            
            if opcao == 'C':
                nome_usuario = input('Digite um nome: ').upper()
                email_usuario = input('Digite um e-mail: ').lower()
                
                try:
                    cursor.execute("""
                    INSERT INTO login (nome, email)
                    VALUES (?, ?)""", (nome_usuario, email_usuario))
                    conexao.commit() # Corrigido: Agora está dentro do try e indentado
                    print(f'\n\033[1;32m{nome_usuario} foi guardado no SQLite!\033[m')
                
                except sqlite3.IntegrityError:
                    print('\n\033[1;31mERROR!!! Este e-mail já existe\033[m')
                except Exception as e:
                    print(f'\n\033[1;31mOcorreu um erro inesperado: {e}\033[m')
                
            elif opcao == 'L':
                listar_usuarios()
            
            elif opcao == 'S':
                print('\n\033[1;33mSaindo do sistema... Até logo!\033[m')
                break # O break deve ficar dentro do elif 'S' para só sair quando você quiser
            
            else:
                print('\n\033[1;31mOpção inválida!\033[m')

sistema_de_cadastro()
