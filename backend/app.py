# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS              # ← import Flask-CORS
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from config import Config
from database import db           # uninitialized SQLAlchemy
from models import User

def create_app():
    # 1. Create and configure the app
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)                             # ← enable CORS for all origins & routes :contentReference[oaicite:4]{index=4}

    # 2. Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)

    # 3. Create database tables
    with app.app_context():
        db.create_all()           # issues CREATE TABLE IF NOT EXISTS… :contentReference[oaicite:4]{index=4}

    # 4. Define routes
    @app.route('/')
    def index():
        return '✅ Main page is up and running!'

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'message': 'User already exists'}), 409
        new_user = User(username=data['username'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.username)
            return jsonify({'access_token': access_token}), 200
        return jsonify({'message': 'Invalid credentials'}), 401

    @app.route('/protected', methods=['GET'])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        return jsonify({'logged_in_as': current_user}), 200

    return app

# Entry point
if __name__ == '__main__':
    create_app().run(debug=True)
