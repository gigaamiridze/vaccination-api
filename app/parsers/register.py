from flask_restful import reqparse

registerParser = reqparse.RequestParser()
registerParser.add_argument('email', type=str, required=True, help='Email should be string')
registerParser.add_argument('password', type=str, required=True, help='Password should be string')
