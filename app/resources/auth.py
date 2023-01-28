from flask import jsonify, request
from flask_restful import Resource
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from app.models import UserModel

class Auth(Resource):
    def post(self):
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        user = UserModel.query.filter_by(email=email).first()
        if user == None:
            return 'Email was not found', 404

        is_email = email != user.email
        is_password = check_password_hash(user.password, password) == False

        if is_email:
            return 'Bad email', 401

        if is_password:
            return 'Bad password', 401

        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)
