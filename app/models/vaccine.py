from app.models import db

class VaccineModel(db.Model):
    __tablename__ = 'vaccinated'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    vaccine_type = db.Column(db.String(30), nullable=False)
    dose = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, name, surname, age, vaccine_type, dose, date, user_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.vaccine_type = vaccine_type
        self.dose = dose
        self.date = date
        self.user_id = user_id

    def __repr__(self):
        return f'User: {self.name} {self.username}'
