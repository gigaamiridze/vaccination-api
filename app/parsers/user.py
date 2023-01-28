from flask_restful import reqparse

userParser = reqparse.RequestParser()
userParser.add_argument('email', type=str, help='Email should be string')
userParser.add_argument('password', type=str, help='Password should be string')
