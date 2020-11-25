from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.GestionCompras import GestionCompras

app = Flask(__name__)
CORS(app)

@app.route('/compras',methods=['GET'])
def getAll():
    return (GestionCompras.list())

@app.route('/compras',methods=['POST'])
def postOne():
    body = request.json
    return (GestionCompras.create(body))

@app.route('/compras/<id>',methods=['GET'])
def getOne(id):
    return (GestionCompras.find(id))

@app.route('/delete/<string:id>',methods=['DELETE'])
def delete(id):
    body = request.json
    return (GestionCompras.delete(id))

#app.run(port=5000,debug=True)