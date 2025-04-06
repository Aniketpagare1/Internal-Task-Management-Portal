from flask import Blueprint, request, jsonify
from models import db, User
import jwt, datetime
from config import Config

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email already registered"}), 400

    user = User(username=data['username'], email=data['email'], role=data['role'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered"}), 201

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, Config.SECRET_KEY, algorithm='HS256')
        return jsonify({
            "token": token,
            "user": {
                "id": user.id,
                "email": user.email,
                "role": user.role,
                "username": user.username
            }
        })
    return jsonify({"message": "Invalid credentials"}), 401
