from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from data_base import listar_clientes, cadastrar_clientes,  apagar_cliente, alterar_cliente, buscar_cliente, editar_cliente_completo
import os 

app = Flask(__name__)

os.makedirs('uploads', exist_ok=True)

# Rota principal — lista todos os clientes
@app.route ("/clientes")
def index():
    return render_template('clientes.html', clientes = listar_clientes())

# pega os campos do formulário com request.form
# chama cadastrar_clientes() com esses valores
# redireciona pra /clientes depois de salva
@app.route ("/cadastrar", methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    telefone = request.form['Telefone']
    evento = request.form['evento']
    data_evento = request.form['data_evento']
    valor = request.form['Valor']
    observacao = request.form['observacao']
    documento = request.form['documento']
    arquivo = request.files['arquivo']
    nome_arquivo = arquivo.filename
    arquivo.save(os.path.join('uploads', nome_arquivo))
    cadastrar_clientes(nome, telefone, evento, data_evento, valor, observacao, documento, nome_arquivo)
    return redirect(url_for('index'))

# Serve os arquivos PDF da pasta uploads
@app.route ('/uploads/<nome_arquivo>')
def download_arquivo(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

# Deleta um cliente pelo id
@app.route('/deletar/<id>', methods=['POST'])
def tirar_cliente(id):
    apagar_cliente(id)
    return  redirect(url_for('index'))

# Atualiza só o status de um cliente
@app.route('/atualizar/<id>', methods=['POST'])
def atualizar_status(id):
    novo_status = request.form['novo_status']
    alterar_cliente(id, novo_status)
    return redirect(url_for('index'))

# Abre o formulário de edição preenchido com os dados do cliente
@app.route('/editar/<id>', methods=['GET'])
def editar_cliente(id):
    cliente = buscar_cliente(id)
    return render_template('editar.html', cliente=cliente)

# Recebe os dados editados e salva no banco
@app.route('/editar/<id>', methods=['POST'])
def salvar_edicao(id):
    nome = request.form['nome']
    telefone = request.form['Telefone']
    evento = request.form['evento']
    data_evento = request.form['data_evento']
    valor = request.form['Valor']
    observacao = request.form['observacao']
    documento = request.form['documento']
    arquivo = request.files['arquivo']
    if arquivo.filename != '':
        # usuário enviou um arquivo novo salva e atualiza
        nome_arquivo = arquivo.filename
        arquivo.save(os.path.join('uploads', nome_arquivo))
    else:
        # usuário não enviou arquivo  busca o nome atual do banco
        cliente_atual = buscar_cliente(id)
        nome_arquivo = cliente_atual[10]
    
    editar_cliente_completo(id, nome, telefone, evento, data_evento, valor, observacao, documento, nome_arquivo)
    return redirect(url_for('index'))
    

if __name__ == "__main__":
    app.run(debug = True)