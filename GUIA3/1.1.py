from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home() -> str:
    return "<h1>Sistema de control Agroindustrial Activos</h1>"

if __name__ == '__main__':
    print("Iniciando servidor en http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)
    
    










