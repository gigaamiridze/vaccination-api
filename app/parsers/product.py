from flask_restful import reqparse

vaccineParser = reqparse.RequestParser()
vaccineParser.add_argument('name', type=str, help='Name should be string')
vaccineParser.add_argument('surname', type=str, help='Surname should be string')
vaccineParser.add_argument('age', type=int, help='Age should be integer')
vaccineParser.add_argument('vaccine_type', type=str, help='Vaccine type should be string')
vaccineParser.add_argument('dose', type=int, help='Dose should be integer')
vaccineParser.add_argument('date', type=str, help='Date should be string')
vaccineParser.add_argument('user_id', type=int, help='User id should be string')
