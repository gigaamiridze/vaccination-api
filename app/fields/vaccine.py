from flask_restful import fields

resource_vaccine = {
    'id': fields.Integer,
    'name': fields.String,
    'surname': fields.String,
    'age': fields.Integer,
    'vaccine_type': fields.String,
    'dose': fields.Integer,
    'date': fields.String,
    'user_id': fields.Integer
}
