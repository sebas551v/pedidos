from click.types import DateTime
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask.signals import request_finished
import requests, json

app = Flask(__name__)

#settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    data = requests.get('http://127.0.0.1:3000/pedidos').json()
    return render_template('index.html', pedidos=data)

@app.route('/agg')
def Create():
    return render_template('create-pedido.html')

@app.route('/add', methods=['POST'])
def add_pedido():
    if request.method == 'POST':
        pedido = dict(request.values)
        requests.post('http://127.0.0.1:3000/pedidos', json=pedido)
        flash('Pedido adicionado correctamente')
        return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_pedido(id):
    data = requests.get('http://127.0.0.1:3000/pedidos/{0}'.format(id)).json()
    return render_template('edit-pedido.html', pedido=data)

@app.route('/update', methods=['POST'])
def update_pedido():
    if request.method == 'POST':
        pedido = dict(request.values)
        requests.put('http://127.0.0.1:3000/pedidos', json=pedido)
        flash('Pedido actualizado correctamente')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_pedido(id):
    requests.delete('http://127.0.0.1:3000/pedidos/{0}'.format(id))
    flash('Pedido eliminado correctamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3001, debug = True)