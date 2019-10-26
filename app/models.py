from app import db

class Materia(db.model):
    id = db.Column(db.Integer, primary_key=true)
    CVE = db.Column(db.String(64), index=true, unique=true)
    Nombre_M = db.Column(db.String(64), index=true, unique=true)
    Plan = db.Column(db.String(64), index=true, unique=true)
    Requisitos = db.Column(db.Integer, index=true, unique=true)

    def __repr__(self):
        return '<Materia {}>'.format(self.CVE)