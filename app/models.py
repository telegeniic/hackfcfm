from app import db

class Lunes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Entrada = db.Column(db.Integer)
    Salida = db.Column(db.Integer)
    
    
class Martes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Entrada = db.Column(db.Integer)
    Salida = db.Column(db.Integer)
    
    
class Miercoles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Entrada = db.Column(db.Integer)
    Salida = db.Column(db.Integer)
    
class Jueves(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Entrada = db.Column(db.Integer)
    Salida = db.Column(db.Integer)
    
    
class Viernes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Entrada = db.Column(db.Integer)
    Salida = db.Column(db.Integer)   
    
    
class Sabado(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Entrada = db.Column(db.Integer)
    Salida = db.Column(db.Integer)
    
lunes = db.Table("lunesh",\
                db.Column('horario.id', db.Integer, db.ForeignKey("horario.id"), primary_key = True),\
                db.Column("lunes.id", db.Integer, db.ForeignKey("lunes.id"), primary_key = True)
                )
martes = db.Table("martesh",\
                db.Column('horario.id', db.Integer, db.ForeignKey("horario.id"), primary_key = True),\
                db.Column("martes.id", db.Integer, db.ForeignKey("martes.id"), primary_key = True)
                )
miercoles = db.Table("miercolesh",\
                db.Column('horario.id', db.Integer, db.ForeignKey("horario.id"), primary_key = True),\
                db.Column("miercoles.id", db.Integer, db.ForeignKey("miercoles.id"), primary_key = True)
                )
jueves = db.Table("juevesh",\
                db.Column('horario.id', db.Integer, db.ForeignKey("horario.id"), primary_key = True),\
                db.Column("jueves.id", db.Integer, db.ForeignKey("jueves.id"), primary_key = True)
                )
viernes = db.Table("viernesh",\
                db.Column('horario.id', db.Integer, db.ForeignKey("horario.id"), primary_key = True),\
                db.Column("viernes.id", db.Integer, db.ForeignKey("viernes.id"), primary_key = True)
                )
    
class Horario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    lunes = db.relationship("Lunes", secondary = lunes, lazy="subquery", backref=db.backref("horario", lazy=True))
    martes = db.relationship("Martes", secondary = martes, lazy="subquery", backref=db.backref("horario", lazy=True))
    miercoles = db.relationship("Miercoles", secondary = miercoles, lazy="subquery", backref=db.backref("horario", lazy=True))
    jueves = db.relationship("Jueves", secondary = jueves, lazy="subquery", backref=db.backref("horario", lazy=True))
    viernes = db.relationship("Viernes", secondary = viernes, lazy="subquery", backref=db.backref("horario", lazy=True))

aulas = db.Table("aulasg",\
                db.Column("grupo.id", db.Integer, db.ForeignKey("grupo.id"), primary_key = True), \
                db.Column("aulas.id", db.Integer, db.ForeignKey("aulas.id"), primary_key = True)
                )
materias = db.Table("materiasg",\
                db.Column("grupo.id", db.Integer, db.ForeignKey("grupo.id"), primary_key = True), \
                db.Column("materia.id", db.Integer, db.ForeignKey("materia.id"), primary_key = True)
                )


class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    horario = db.Column(db.Integer, db.ForeignKey('horario.id'), nullable = False)
    aulas = db.relationship("Aulas", secondary = aulas, lazy="subquery", backref=db.backref("grupo", lazy = True))
    materias = db.relationship("Materia", secondary = materias, lazy="subquery", backref=db.backref("grupo", lazy = True))
  


class Aulas(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(5))
    

materia = db.Table("materias", \
    db.Column("materias.id", db.Integer, db.ForeignKey("materia.id"), primary_key = True), \
    db.Column("maestro.id", db.Integer, db.ForeignKey("maestro.id"), primary_key = True) \
    )
                   
class Materia(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(20))
    materia = db.relationship("Maestro", secondary = materia, lazy="subquery", backref=db.backref("materias", lazy = True))
                                          
class Maestro(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(20))