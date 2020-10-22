from flask import Flask, request
from flask_cors import CORS
from api.controllers.Pedidos import Pedido

app = Flask(__name__)
CORS(app)

@app.route('/pedidos', methods=['GET'])
def getAll():
    return (Pedido.list())

@app.route('/pedidos/<id_pedido>', methods=['GET'])
def getOne(id_pedido):
    return (Pedido.getOne(id_pedido))

@app.route('/pedidos', methods=['POST'])
def postOne():
    body = request.json
    return (Pedido.create(body))

@app.route('/pedidos', methods=['PUT'])
def putOne():
    body = request.json
    return (Pedido.update(body))

@app.route('/pedidos/<id_pedido>', methods=['DELETE'])
def deleteOne(id_pedido):
    return (Pedido.delete(id_pedido))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)