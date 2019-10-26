from app import db

class Materia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Nombre_M = db.Column(db.String(64))
    Plan = db.Column(db.String(64))
    Requisitos = db.Column(db.Integer)

    def __repr__(self):
        return '<Materia {}>'.format(self.Materia)

class Requisito(db.Model):  
    id = db.Column(db.Integer, primary_key= True)
    Mat_1 = db.Column(db.Integer)
    Mat_2 = db.Column(db.Integer)
    Mat_3 = db.Column(db.Integer)
    Mat_4 = db.Column(db.Integer)
    Mat_5 = db.Column(db.Integer)

    def __repr__(self):
        return '<Requisito {}>'.format(self.Requisito)

class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key= True) #es su propio id
    CVE_MAT = db.Column(db.Integer, unique= True)
    CVE_HORA = db.Column(db.Integer, unique= True)

    def __repr__(self):
        return '<Grupo {}>'.format(self.Grupo)

class Hora(db.Model):
    id = db.Column(db.Integer, primary_key= True) #es su propio id
    Entrada = db.Column(db.String(5))
    Salida = db.Column(db.String(5))

    def __repr__(self):
        return '<Hora {}>'.format(self.Hora)

class Dias(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    Lunes = db.Column(db.Integer )
    Martes = db.Column(db.Integer )
    Miercoles = db.Column(db.Integer )
    Jueves = db.Column(db.Integer )
    Viernes = db.Column(db.Integer )
    Sabado = db.Column(db.Integer )

    def __repr__(self):
        return '<Dias {}>'.format(self.Dias)

class Salones(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    Lunes = db.Column(db.String(5) )
    Martes = db.Column(db.String(5) )
    Miercoles = db.Column(db.String(5) )
    Jueves = db.Column(db.String(5) )
    Viernes = db.Column(db.String(5) )
    Sabado = db.Column(db.String(5) )

    def __repr__(self):
        return '<Salones {}>'.format(self.Salones)

class Horario(db.Model):
     id = db.Column(db.Integer, primary_key= True)
     CVE_GPO = db.Column(db.Integer)
     CVE_DIAS = db.Column(db.Integer)
     CVE_SALONES = db.Column(db.Integer)

     def __repr__(self):
         return '<Horario {}>'.format(self.Horario)

