from flask import jsonify
from api.db.db import cnx

class Pedido():
    global cur
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM pedidos")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns, row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close
    
    def getOne(id_pedido):
        sql = "SELECT * FROM pedidos WHERE id_pedido = %s"
        cur.execute(sql, (id_pedido,))
        data = cur.fetchone()
        return jsonify(data)
    
    def create(body):
        data = (body['producto'],body['url_imagen'],body['fecha_pedido'],body['fecha_entrega'])
        sql = "INSERT INTO pedidos(producto, url_imagen, fecha_pedido, fecha_entrega) VALUES(%s, %s, %s, %s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': "Insertado"}, 200

    def update(body):
        data = (body['producto'] ,body['url_imagen'], body['fecha_pedido'], body['fecha_entrega'], body['id_pedido'])
        sql = "UPDATE pedidos SET producto = %s, url_imagen = %s,  fecha_pedido = %s, fecha_entrega = %s WHERE id_pedido = %s"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': "Actualizado"}, 200

    def delete(id_pedido):
        sql = "DELETE FROM pedidos WHERE id_pedido = %s"
        cur.execute(sql, (id_pedido,))
        cnx.commit()
        return {'estado': "Eliminado"}, 200