from flask_restful import Resource, marshal_with
from flask_jwt_extended import jwt_required
from app.fields.vaccine import resource_vaccine
from app.parsers.product import vaccineParser
from app.models import VaccineModel
from app.models import db

class Vaccine(Resource):
    @marshal_with(resource_vaccine)
    @jwt_required()
    def get(self, vaccine_id):
        if vaccine_id == 777:
            return VaccineModel.query.all()
        vaccine = VaccineModel.query.filter_by(id=vaccine_id).first()
        return vaccine

    @jwt_required()
    def post(self, vaccine_id):
        args = vaccineParser.parse_args()
        vaccine = VaccineModel(name=args['name'], surname=args['surname'], age=args['age'],
                                vaccine_type=args['vaccine_type'],dose=args['dose'],
                                date=args['date'], user_id=args['user_id'])
        db.session.add(vaccine)
        db.session.commit()
        return f'Created vaccinated person with ID {vaccine_id}'

    @jwt_required()
    def put(self, vaccine_id):
        args = vaccineParser.parse_args()
        vaccine =VaccineModel.query.filter_by(id=vaccine_id).first()
        if vaccine == None:
            vaccine = VaccineModel(name=args['name'], surname=args['surname'], age=args['age'],
                                    vaccine_type=args['vaccine_type'], dose=args['dose'],
                                    date=args['date'], user_id=args['user_id'])
        else:
            vaccine.name = args['name']
            vaccine.surname = args['surname']
            vaccine.age = args['age']
            vaccine.vaccine_type = args['vaccine_type']
            vaccine.dose = args['dose']
            vaccine.date = args['date']
            vaccine.user_id = args['user_id']
        db.session.add(vaccine)
        db.session.commit()
        return f"Edited vaccinated person with ID {vaccine_id}"

    @jwt_required()
    def delete(self, vaccine_id):
        if vaccine_id == None:
            return f"Vaccinated person ID {vaccine_id} doesn't exist"
        vaccine = VaccineModel.query.filter_by(id=vaccine_id).first()
        db.session.delete(vaccine)
        db.session.commit()
        return f"Deleted vaccinated person with ID {vaccine_id}"
