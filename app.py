from flask import Flask, jsonify, request
from operationBD import koha


app = Flask(__name__)

@app.route ('/')
def index():            
    return '<h1>Api Rest para insercion y modificacion</h1>'


@app.route ('/get', methods = ['POST'])
def get():            
    kohas =koha()
    try:
        res = kohas.getJson(request.json)
        return jsonify(res)
    except:
        return jsonify({"respuesta":"error"})


@app.route ('/insert', methods = ['POST'])
def insert():            
    kohas =koha()
    res = kohas.insertJson(request.json )
    return jsonify(res)


@app.route ('/update', methods = ['POST'])
def update():            
    kohas =koha()
    res =kohas.actualizar(request.json)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=False, port=5000)

