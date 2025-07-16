from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(name)
CORS(app)

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Olá da VitaClin!'})

if name == 'main':
    app.run(debug=True)
    