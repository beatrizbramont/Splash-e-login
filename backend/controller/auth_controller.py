from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import random
from flask_mail import Message
from extensions import mail

from model.user_model import create_user, get_user_by_email
from model.otp_model import create_otp, get_valid_otp, mark_otp_as_used

auth_bp = Blueprint("auth", __name__)

def generate_otp():
    return str(random.randint(100000, 999999))

@auth_bp.route("/cadastro", methods=["POST"])
def cadastro():
    data = request.json
    nome = data.get("nome")
    email = data.get("email")
    senha = generate_password_hash(data.get("senha"))

    if get_user_by_email(email):
        return jsonify({"error": "Email já cadastrado"}), 400

    create_user(nome, email, senha)
    return jsonify({"message": "Usuário cadastrado com sucesso"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    senha = data.get("senha")

    user = get_user_by_email(email)

    if not user:
        return jsonify({"redirect": "cadastro"}), 404

    if not check_password_hash(user["senha"], senha):
        return jsonify({"error": "Senha incorreta"}), 401

    otp_code = generate_otp()
    expiration = (datetime.utcnow() + timedelta(minutes=5)).isoformat()

    create_otp(user["id"], otp_code, expiration)

    msg = Message(
    subject="Seu código OTP",
    sender="no-reply@splashlogin.com",
    recipients=[email]
    )

    msg.body = f"""
    Olá!

    Seu código OTP é: {otp_code}

    Ele expira em 5 minutos.
    """

    mail.send(msg)

    return jsonify({
        "message": "OTP enviado",
        "user_id": user["id"]
    }), 200

@auth_bp.route("/verify-otp", methods=["POST"])
def verify_otp():
    data = request.json
    user_id = data.get("user_id")
    code = data.get("code")

    otp = get_valid_otp(user_id, code)

    if not otp:
        return jsonify({"error": "OTP inválido"}), 400

    if datetime.fromisoformat(otp["expires_at"]) < datetime.utcnow():
        return jsonify({"error": "OTP expirado"}), 400

    mark_otp_as_used(otp["id"])

    return jsonify({"message": "Login autorizado"}), 200

print("AUTH CONTROLLER CARREGADO")
