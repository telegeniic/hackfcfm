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
    Mat_1 = db.Column(db.Integer, index=true, unique=true)
    Mat_2 = db.Column(db.Integer, index=true, unique=true)
    Mat_3 = db.Column(db.Integer, index=true, unique=true)
    Mat_4 = db.Column(db.Integer, index=true, unique=true)
    Mat_5 = db.Column(db.Integer, index=true, unique=true)

    def __repr__(self):
        return '<Requisito {}>'.format(self.Requisito)

class Grupo(db.model):
    id = db.Column(db.Integer, primary_key=true) #es su propio id
    CVE_MAT = db.Column(db.Integer, index=true, unique=true)
    CVE_HORA = db.Column(db.Integer, index=true, unique=true)

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
    Lunes = db.Columndb.Integer, index=true)
    Martes = db.Column(db.Integer, index=true)
    Miercoles = db.Column(db.Integer, index=true)
    Jueves = db.Column(db.Integer, index=true)
    Viernes = db.Column(db.Integer, index=true)
    Sabado = db.Column(db.Integer, index=true)

    def __repr__(self):
        return '<Dias {}>'.format(self.Dias)

class Salones(db.model):
    id = db.Column(db.Integer, primary_key=true)
    Lunes = db.Column(db.String(5), index=true)
    Martes = db.Column(db.String(5), index=true)
    Miercoles = db.Column(db.String(5), index=true)
    Jueves = db.Column(db.String(5), index=true)
    Viernes = db.Column(db.String(5), index=true)
    Sabado = db.Column(db.String(5), index=true)

    def __repr__(self):
        return '<Salones {}>'.format(self.Salones)

class Horario(db.model):
     id = db.Column(db.Integer, primary_key=true)
     CVE_GPO = db.Column(db.Integer, index=true)
     CVE_DIAS = db.Column(db.Integer, index=true)
     CVE_SALONES = db.Column(db.integer, index=true)

    def __repr__(self):
        return '<Horario {}>'.format(self.Horario)

