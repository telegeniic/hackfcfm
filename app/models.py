from app import db

class Materia(db.model):
    id = db.Column(db.Integer, primary_key=true)
    CVE = db.Column(db.String(64), index=true, unique=true)
    Nombre_M = db.Column(db.String(64), index=true, unique=true)
    Plan = db.Column(db.String(64), index=true, unique=true)
    Requisitos = db.Column(db.Integer, index=true, unique=true)

    def __repr__(self):
        return '<Materia {}>'.format(self.Materia)

class Requisito(db.model):
    id = db.Column(db.Integer, primary_key=true)
    Mat_1 = (db.Integer, index=true, unique=true)
    Mat_2 = (db.Integer, index=true, unique=true)
    Mat_3 = (db.Integer, index=true, unique=true)
    Mat_4 = (db.Integer, index=true, unique=true)
    Mat_5 = (db.Integer, index=true, unique=true)

    def __repr__(self):
        return '<Requisito {}>'.format(self.Requisito)

class Grupo(db.model):
    id = db.Column(db.Integer, primary_key=true) #es su propio id
    CVE_MAT = (db.Integer, index=true, unique=true)
    CVE_HORA = (db.Integer, index=true, unique=true)

    def __repr__(self):
        return '<Grupo {}>'.format(self.Grupo)

class Hora(db.model):
    id = db.Column(db.Integer, primary_key=true) #es su propio id
    Entrada = db.Column(db.String(5), index=true)
    Salida = db.Column(db.String(5), index=true)

    def __repr__(self):
        return '<Hora {}>'.format(self.Hora)

class Dias(db.model):
    id = db.Column(db.Integer, primary_key=true)
    Lunes = (db.Integer, index=true)
    Martes = (db.Integer, index=true)
    Miercoles = (db.Integer, index=true)
    Jueves = (db.Integer, index=true)
    Viernes = (db.Integer, index=true)
    Sabado = (db.Integer, index=true)

    def __repr__(self):
        return '<Dias {}>'.format(self.Dias)

class Salones(db.model):
    id = db.Column(db.Integer, primary_key=true)
    Lunes = (db.String(5), index=true)
    Martes = (db.String(5), index=true)
    Miercoles = (db.String(5), index=true)
    Jueves = (db.String(5), index=true)
    Viernes = (db.String(5), index=true)
    Sabado = (db.String(5), index=true)

    def __repr__(self):
        return '<Salones {}>'.format(self.Salones)

class Horario(db.model):
     id = db.Column(db.Integer, primary_key=true)
     CVE_GPO = (db.Integer, index=true)
     CVE_DIAS = (db.Integer, index=true)
     CVE_SALONES = (db.integer, index=true)

    def __repr__(self):
        return '<Horario {}>'.format(self.Horario)

