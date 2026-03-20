from flask import Flask, render_template 
from data_base import listar_clientes 

app = Flask(__name__)

@app.route ("/clientes")
def index():
    return render_template('clientes.html', clientes = listar_clientes())

if __name__ == "__main__":
    app.run(debug = True)