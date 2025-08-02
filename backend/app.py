from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)  # CORRETO
CORS(app)

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Olá da OdontoCare!'})

if __name__ == '__main__':  # CORRETO
    app.run(debug=True)
