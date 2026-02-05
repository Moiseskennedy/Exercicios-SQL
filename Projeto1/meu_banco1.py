import sqlite3

conexao = sqlite3.connect('/storage/emulated/0/Documents/SQL/Projeto1/meu_aprendizado.db')
#Bucando OU criando um arquivo banco e conectando

cursor = conexao.cursor()
#Cursor() é para quem a gente "pede" coisas para ADICIONAR, CHAMAR, EXCUTAR ou EXCLUIR do banco que criamos

#Excutar a instrução
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS datasets (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
nome TEXT NOT NULL,
idade INTEGER NOT NULL,
profissao TEXT
)
""")

#INSERINDO DADOS 
cursor.execute("""
INSERT INTO datasets(nome, idade, profissao) 
VALUES ('Moises Kennedy', 20, 'Programador')
""")

cursor.execute("""
INSERT INTO datasets(nome, idade, profissao) 
VALUES ('Samuel Kennedy', 12, 'Bombeiro')
""")

#SALVANDO 
conexao.commit()

# LENDO OS DADOS
cursor.execute("SELECT * FROM datasets") #selecione tudo primeiro 
for linha in cursor.fetchall():
  print(linha)
  
#Fechar conexao do BD
cursor.close()
conexao.close()



"""
PRIMARY KEY -> chave unica um usuario so pode ter um unico ID 

AUTOINCREMENTE -> Deixa o ID autimatico a cada novo dado, também facilita o historico caso vanhamos deletar o ID5 o proximo ID ainds será ID6 para não haver confusão de historico.

NOT NULL -> para garantir que a coluna nunca fique vazia, ela serve para garatir que o usuario seja obrigado a preencher esse campo
"""

