import sqlite3

conexao = sqlite3.connect("banco.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    Nome Varchar(100) NOT NULL,
    Telefone VARCHAR(100) NOT NULL,                            
    Evento Varchar(100) NOT NULL,             
    Data_evento date NOT NULL,
    Valor DECIMAL(10, 2) NOT NULL, 
    Status VARCHAR(30) NOT NULL DEFAULT 'Pendente',
    observacao VARCHAR(100) NOT NULL,
    Data_criacao  TEXT DEFAULT (DATE('now'))                                           
     )                
""")

def cadastrar_clientes(Nome, Telefone, Evento, Data_evento, Valor, observacao, documento, arquivo):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("""INSERT INTO clientes(Nome, Telefone, Evento, Data_evento, Valor, observacao, documento, arquivo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", (Nome, Telefone, Evento, Data_evento, Valor, observacao, documento, arquivo))
    conexao.commit()
    conexao.close()


def listar_clientes():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM clientes""") 
    resultado_listar_clientes = cursor.fetchall()
    conexao.close()
    return resultado_listar_clientes
    
    
def apagar_cliente(id):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("""DELETE FROM clientes WHERE id = ?""", (id,))
    conexao.commit()
    conexao.close() 


def alterar_cliente(id, novo_status):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("""UPDATE clientes SET Status = ? WHERE id = ?""", (novo_status, id))
    conexao.commit()
    conexao.close() 

def adicionar_coluna():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("""ALTER TABLE clientes ADD COLUMN arquivo TEXT""")
    conexao.commit()
    conexao.close() 

def buscar_cliente(id):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM clientes WHERE id = ?""", (id,))
    resultado = cursor.fetchone()
    conexao.close() 
    return resultado


print("Bannco criado com sucesso!")

