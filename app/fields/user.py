from flask_restful import fields

resource_users = {
    'id': fields.Integer,
    'email': fields.String,
    'password': fields.String
}
