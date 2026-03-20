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

def cadastrar_clientes(Nome, Telefone, Evento, Data_evento, Valor, observacao):

    cursor.execute("""INSERT INTO clientes(Nome, Telefone, Evento, Data_evento, Valor, observacao)
    VALUES (?, ?, ?, ?, ?, ?)
""", (Nome, Telefone, Evento, Data_evento, Valor, observacao))
    
    conexao.commit()

def listar_clientes():
    cursor.execute("""SELECT * FROM clientes""") 
    resultado_listar_clientes = cursor.fetchall()
    for cliente in resultado_listar_clientes:
        print(cliente)

listar_clientes()

def apagar_cliente(id):
    cursor.execute("""DELETE FROM clientes WHERE id = ?""", (id,))
    conexao.commit() 

def alterar_cliente(id, novo_status):
    cursor.execute("""UPDATE clientes SET Status = ? WHERE id = ?""", (novo_status, id))
    conexao.commit() 
alterar_cliente(1, "confirmado")

conexao.close()
print("Bannco criado com sucesso!")

