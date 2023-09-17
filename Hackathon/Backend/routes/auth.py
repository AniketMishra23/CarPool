from flask import Blueprint, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User
from utils import hash_password, verify_password
from validations import validate_registration, validate_login

auth_blueprint = Blueprint('auth', __name__)
CORS(auth_blueprint)

@auth_blueprint.route('/createUser', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        validation_errors = validate_registration(data)
        
        if validation_errors:
            return jsonify(errors=validation_errors), 400

        email = data['email']
        password = data['password']

        if User.query.filter_by(email=email).first():
            return jsonify(error="Email already exists"), 409

        hashed_password = hash_password(password)
        user = User(email=email, password=hashed_password)
        user.save()

        access_token = create_access_token(identity=user.id)
        return jsonify(success=True, token=access_token), 201

    except Exception as e:
        print(e)
        return jsonify(error="Internal Server Error"), 500

@auth_blueprint.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        validation_errors = validate_login(data)

        if validation_errors:
            return jsonify(errors=validation_errors), 400

        email = data['email']
        password = data['password']

        user = User.query.filter_by(email=email).first()

        if not user or not verify_password(password, user.password):
            return jsonify(error="Invalid credentials"), 401

        access_token = create_access_token(identity=user.id)
        return jsonify(success=True, token=access_token), 200

    except Exception as e:
        print(e)
        return jsonify(error="Internal Server Error"), 500

@auth_blueprint.route('/getUser', methods=['POST'])
@jwt_required()
def get_user():
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if not user:
            return jsonify(error="User not found"), 404

        user_data = {
            'id': user.id,
            'email': user.email,
        }

        return jsonify(user=user_data), 200

    except Exception as e:
        print(e)
        return jsonify(error="Internal Server Error"), 500
