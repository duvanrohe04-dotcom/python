import os
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)


class InventarioTrapiche:

    def __init__(self):
        self._productos: list[dict] = []

    def agregar_lote(self, tipo: str, kilos: float) -> dict:
        lote = {
            "id": len(self._productos) + 1,
            "tipo": tipo,
            "kilos": kilos
        }
        self._productos.append(lote)
        return lote

    def obtener_todos(self) -> list[dict]:
        return self._productos


gestor_inventario = InventarioTrapiche()


@app.route('/api/inventario', methods=['GET'])
def ver_inventario() -> tuple[Response, int]:

    datos = gestor_inventario.obtener_todos()

    return jsonify({
        "total": len(datos),
        "lotes": datos
    }), 200


@app.route('/api/inventario', methods=['POST'])
def registrar_lote() -> tuple[Response, int]:

    payload = request.get_json()

    # Validación del JSON
    if not payload or "tipo" not in payload or "kilos" not in payload:
        return jsonify({
            "error": "Debe enviar 'tipo' y 'kilos' en el JSON"
        }), 400

    try:
        nuevo_lote = gestor_inventario.agregar_lote(
            payload["tipo"],
            float(payload["kilos"])
        )

        return jsonify({
            "mensaje": "Lote registrado",
            "data": nuevo_lote
        }), 201

    except Exception:
        return jsonify({
            "error": "Error al registrar el lote"
        }), 500


if __name__ == '__main__':

    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"

    app.run(host="0.0.0.0", port=port, debug=debug)
