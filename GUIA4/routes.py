from flask import Blueprint, request, jsonify, Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from models import db, Usuario


api_bp = Blueprint('api', __name__)


@api_bp.route('/usuarios/registrar', methods=['POST'])
def registrar_usuario() -> tuple[Response, int]:

    try:
        payload = request.get_json()

        if not payload or "username" not in payload or "password" not in payload:
            return jsonify({"error": "Debe enviar username y password"}), 400

        # Hash de la contraseña
        clave_segura = generate_password_hash(payload['password'])

        # Crear objeto Usuario
        nuevo_user = Usuario(
            username=payload['username'],
            password_hash=clave_segura,
            rol=payload.get('rol', 'Operario')
        )

        # Guardar en base de datos
        db.session.add(nuevo_user)
        db.session.commit()

        return jsonify({
            "mensaje": "Éxito",
            "data": nuevo_user.serializar()
        }), 201

    except Exception as e:

        db.session.rollback()

        return jsonify({
            "error": "Fallo de integridad",
            "detalle": str(e)
        }), 400


@api_bp.route('/usuarios', methods=['GET'])
def listar_usuarios() -> tuple[Response, int]:

    pagina = request.args.get('page', 1, type=int)

    paginacion = Usuario.query.paginate(
        page=pagina,
        per_page=10,
        error_out=False
    )

    resultado = [u.serializar() for u in paginacion.items]

    return jsonify({
        "pagina_actual": paginacion.page,
        "total_paginas": paginacion.pages,
        "usuarios": resultado
    }), 200
