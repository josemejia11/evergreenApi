from flask import jsonify, request
from db.db import cnx

class GestionCompras():
    global cur
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("select * from gestioncompras")
        rows = cur.fetchall()
        colums = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(colums, row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close()

    def create(body):
        data = (body['tipoEgreso'],body['tipoElemento'],body['proveedor'],body['formaPago'],body['aprobacion'],body['realizarPago'])
        sql = "INSERT INTO gestioncompras(tipoEgreso,tipoElemento,proveedor,formaPago,aprobacion,realizarPago) VALUES(%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': "insertado"},200

    def find(id):
        sembrado = cur.execute( "select * from gestioncompras where id = '" + id + "'")
        return jsonify(cur.fetchone())
        cnx.close
    
    def delete(id):
        cur.execute("delete from gestioncompras where id = %(id)s", {'id' : id});
        cnx.commit()
        cnx.close
        return {'info': "Compra eliminada"}, 200 

    