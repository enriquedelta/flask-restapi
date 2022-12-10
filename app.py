from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/products', methods=['GET'])
def getProducts():
    fecha = request.json['fecha']
    return jsonify({"products": fecha})

if __name__ == '__main__':
    app.run(debug=True)