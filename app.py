from flask import Flask, render_template, request, redirect, url_for 
from data_base import listar_clientes, cadastrar_clientes 

app = Flask(__name__)

@app.route ("/clientes")
def index():
    return render_template('clientes.html', clientes = listar_clientes())
# pega os campos do formulário com request.form
# chama cadastrar_clientes() com esses valores
# redireciona pra /clientes depois de salv
@app.route ("/cadastrar", methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    telefone = request.form['Telefone']
    evento = request.form['evento']
    data_evento = request.form['data_evento']
    valor = request.form['Valor']
    observacao = request.form['observacao']
    documento = request.form['documento']
    cadastrar_clientes(nome, telefone, evento, data_evento, valor, observacao, documento)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug = True)